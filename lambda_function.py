import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Items')  # change if your table name is different

def lambda_handler(event, context):
    try:
        print("Incoming Event:", json.dumps(event))  # Debug log

        # Handle different event formats (REST vs HTTP API)
        body = event.get("body")
        if body and isinstance(body, str):
            body = json.loads(body)
        elif not body:
            body = {}

        method = event.get("requestContext", {}).get("http", {}).get("method") \
                 or event.get("httpMethod")

        path = event.get("rawPath") or event.get("path", "")

        if method == "POST" and path.endswith("/items"):
            item_id = str(uuid.uuid4())
            item = {
                "id": item_id,
                "name": body.get("name", "unknown"),
                "value": body.get("value", "0")
            }
            table.put_item(Item=item)
            return response(200, {"message": "Item created", "item": item})

        elif method == "GET" and path.endswith("/items"):
            result = table.scan()
            return response(200, result.get("Items", []))

        elif method == "GET" and "id" in event.get("pathParameters", {}):
            item_id = event["pathParameters"]["id"]
            result = table.get_item(Key={"id": item_id})
            return response(200, result.get("Item", {}))

        elif method == "PUT" and "id" in event.get("pathParameters", {}):
            item_id = event["pathParameters"]["id"]
            table.update_item(
                Key={"id": item_id},
                UpdateExpression="set #n = :name, #v = :value",
                ExpressionAttributeNames={"#n": "name", "#v": "value"},
                ExpressionAttributeValues={
                    ":name": body.get("name", "unknown"),
                    ":value": body.get("value", "0")
                }
            )
            return response(200, {"message": "Item updated"})

        elif method == "DELETE" and "id" in event.get("pathParameters", {}):
            item_id = event["pathParameters"]["id"]
            table.delete_item(Key={"id": item_id})
            return response(200, {"message": "Item deleted"})

        else:
            return response(400, {"msg": "Invalid Request"})

    except Exception as e:
        print("Error:", str(e))
        return response(500, {"message": "Internal Server Error", "error": str(e)})

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
