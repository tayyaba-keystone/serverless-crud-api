# Serverless CRUD Application 🚀

This is a Serverless CRUD Demo Application built using **AWS Lambda, API Gateway, DynamoDB, and S3 (for hosting index.html)**.  
It demonstrates how to Create, Read, Update, and Delete (CRUD) items in DynamoDB table using a simple web UI.

---

## Features ✨
- Create new items with name and value.  
- Read all items or fetch a single item by ID.  
- Update existing items.  
- Delete items.  
- Hosted frontend (index.html) with API Gateway integration.  

---

## Technologies Used 💻
- **AWS Lambda**  
- **Amazon DynamoDB**  
- **Amazon API Gateway**  
- **Amazon S3**  
- **python, HTML**  

---

## 1. DynamoDB Table Created
Created DynamoDB table **Items** with `id` as the Primary Key.  
<img width="975" height="275" alt="Image" src="https://github.com/user-attachments/assets/3f2748a3-9746-4f95-81b0-773db7764726" />
---

## 2. API Gateway Setup
Configured API Gateway with methods for CRUD operations:  
- **POST** → Add Item  
- **GET** → Get Items  
- **PUT** → Update Item  
- **DELETE** → Delete Item  
<img width="975" height="372" alt="Image" src="https://github.com/user-attachments/assets/d0cff964-1c91-407e-bce2-ee9ad8a428a5" />
---

## 3. Lambda Function
Lambda function written in **Python** to handle CRUD logic.  
<img width="975" height="397" alt="Image" src="https://github.com/user-attachments/assets/35e097c6-f660-4cdb-9245-aa48954e35d9" />
---

## 4. S3 Bucket Hosting index.html
Frontend hosted on **S3 static website bucket** with public access.  
<img width="975" height="322" alt="Image" src="https://github.com/user-attachments/assets/5d45fbb7-4d2d-48e2-94c8-8034db332ea2" />
---

## 5. Application Home Page
User can interact with the CRUD app through `index.html` hosted on S3.  
<img width="975" height="484" alt="Image" src="https://github.com/user-attachments/assets/b517f508-257c-4416-b07b-8e0054490de3" />
---

## 6. Adding Items (POST)
Click on **"Add Item"** to insert new data into DynamoDB via API Gateway & Lambda.  
<img width="975" height="581" alt="Image" src="https://github.com/user-attachments/assets/b3a5b2af-86e7-46fd-8d14-5bfaaa4ae1ca" />
---

## 7. Viewing Items (GET)
Click on **"Get Items"** to fetch and display items from DynamoDB.  
<img width="975" height="133" alt="Image" src="https://github.com/user-attachments/assets/ebe35841-b069-41a4-b86f-e8aeb1931b88" />
---

## 8. Updating Items (PUT)
Update existing item details using the **"Update"** button (PUT request).  
<img width="975" height="175" alt="Image" src="https://github.com/user-attachments/assets/0f81fce2-ba55-451f-b4ba-d00486840d43" />
---

## 9. Deleting Items (DELETE)
Remove items by clicking the **"Delete"** button (DELETE request).  
<img width="975" height="124" alt="Image" src="https://github.com/user-attachments/assets/6cc9c35d-37ee-4eec-b004-5f3982f4c8f1" />
---

## 10. Exploration of Items in DynamoDB Table
All items can be explored directly from the **DynamoDB console** after CRUD operations.  
<img width="975" height="362" alt="Image" src="https://github.com/user-attachments/assets/ab85d64e-ff22-40ba-8c76-1966a9c3e5ba" />
---
