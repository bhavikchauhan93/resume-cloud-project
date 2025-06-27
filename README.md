# 🌩️ Cloud Resume Challenge – Bhavik Chauhan

This repository contains an attempt at the [Cloud Resume Challenge](https://cloudresumechallenge.dev/), a hands-on project that brings together multiple AWS services and frontend/backend integration in a cloud-native architecture.

The project emphasizes real-world infrastructure skills using AWS, Infrastructure as Code, serverless computing, and secure content delivery — while also reinforcing local development workflows and best practices.

---

## 🧠 Project Overview

A serverless resume website built with:

- Static hosting on AWS S3, served securely via Amazon CloudFront
- A dynamic visitor counter using:
  - JavaScript on the frontend
  - AWS API Gateway + Lambda backend
  - DynamoDB for persistent storage
- All infrastructure deployed using **AWS SAM templates**
- Credentials and access managed securely with `aws-vault`
- Local testing performed with `sam local` and CLI tools

---

## 🛠️ Technologies Used

### ⚙️ Infrastructure
- Amazon S3 (static hosting)
- Amazon CloudFront (CDN with HTTPS and OAC)
- AWS SAM (Infrastructure as Code)
- IAM (least-privilege roles and policies)
- [aws-vault](https://github.com/99designs/aws-vault) (secure credentials management in development environment)

### ☁️ Serverless Backend
- AWS Lambda (Python)
- API Gateway (HTTP GET endpoint)
- DynamoDB (NoSQL data store)
- CloudWatch (logs and metrics)

### 💻 Frontend
- HTML/CSS Resume Site
- JavaScript `fetch()` call to API
- Hosted via S3 and served through CloudFront

---

## 🔄 Development Workflow

- `make build` – builds infrastructure and code
- `make deploy-infra` – deploys S3 + CloudFront stack
- `make deploy-site` – uploads static website files
- `make deploy-lambda` – deploys Lambda + setup Api Gateway + DynamoDB stack
- `sam local invoke` – tests Lambda function locally
- `sam local start-api` – tests API locally

Infrastructure is modularized into two separate SAM templates for easier testing, maintenance, and deployment.

---

## 🧪 Unit Testing

Basic unit tests have been added for the Lambda function using `pytest` and `unittest.mock`. These tests simulate interaction with DynamoDB by mocking `boto3` calls, ensuring safe and repeatable testing without deploying to AWS.

**Test Coverage:**
- ✅ Verifies counter logic: reads the current value, increments, and writes back
- ✅ Ensures Lambda returns the correct HTTP response format
- ✅ Uses `patch` to mock the DynamoDB `table` object

**Run Tests Locally:**

```
pytest [path to test file] -v -s
```

**Install Dependencies:**

```
pip install -r requirements.txt
# or manually:
pip install pytest boto3
```

---

## ✅ Features Implemented

- [x] Static website deployed to S3
- [x] CloudFront distribution with Origin Access Control
- [x] Lambda function for tracking page views
- [x] API Gateway integration with Lambda
- [x] DynamoDB table to store visitor count
- [x] JavaScript-based dynamic view counter
- [x] Local development workflow using `sam` CLI and `aws-vault`
- [x] Lambda function unit testing
- [ ] CI/CD pipelines using GitHub Actions 

---

## 🔗 Live Website

Hosted via AWS CloudFront  
URL: _https://d13cnsrxlrqrrl.cloudfront.net_

---

## 💡 Key Learnings

- Gained hands-on experience with serverless architecture using AWS SAM
- Learned to separate infrastructure components into modular stacks
- Understood the importance of local testing before deploying to avoid costly redeploys
- Encountered and resolved real-world issues with packaging, API Gateway formatting, IAM permissions, and secure S3 hosting

---