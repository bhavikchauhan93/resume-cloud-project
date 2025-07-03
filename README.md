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

## 🚀 GitHub Actions + AWS OIDC Deployment

This project uses **GitHub Actions OpenID Connect (OIDC)** to securely deploy website changes to an Amazon S3 bucket **without storing static AWS credentials**.

#### 🔐 Why OIDC?

* No need to store `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY`
* Credentials are temporary and scoped to each workflow run
* Role access is limited to this repo and specific branches only

---

### ✅ How It Works

1. **GitHub OIDC token** is generated when a PR is merged
2. **AWS IAM role** is assumed using that token via [OIDC provider](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
3. The workflow uploads files from `resume-website/` to your S3 bucket using `aws s3 sync`

---

### 🧾 IAM Setup Summary

* OIDC provider added: `token.actions.githubusercontent.com`
* IAM Role trust policy (example):

```json
{
  "Effect": "Allow",
  "Principal": {
    "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
    "StringEquals": {
      "token.actions.githubusercontent.com:sub": "repo:<GitHubOrg/GitHubRepo>:ref:refs/heads/<GitHubBranch>",
      "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
    }
  }
}
```

* Permissions policy example:

```json
{
  "Effect": "Allow",
  "Action": ["s3:PutObject", "s3:DeleteObject", "s3:ListBucket"],
  "Resource": [
    "arn:aws:s3:::<S3-ucket-name>",
    "arn:aws:s3:::<S3-ucket-name>/*"
  ]
}
```

---

### ⚙️ GitHub Secrets

| Secret Name    | Purpose                            |
| -------------- | ---------------------------------- |
| `AWS_ROLE_ARN` | Full ARN of the IAM role to assume |

---

### 🛠️ Workflow Trigger

This workflow runs **after a PR is merged to `master`**, but only if files in `resume-website/` were modified:

```yaml
on:
  pull_request:
    types: [closed]
    branches: [master]
    paths:
      - 'resume-website/**'
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
- [x] CI/CD pipelines using GitHub Actions 

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
- Implemented AWS Lambda function and tested it locally using sam local invoke and sam local start-api
- Gained experience with mocking AWS services using unittest.mock and pytest for Lambda unit tests
- Identified and fixed CI-related issues such as import errors, NoRegionError, and mocking boto3 correctly in GitHub Actions
- Implemented secure, credential-less CI/CD using GitHub OIDC with IAM role-based authentication and scoped trust policies
- Learned best practices around protecting AWS account details (e.g., using GitHub Secrets for role ARNs)
- Configured automated S3 deployment via GitHub Actions triggered only when PRs affecting resume-website/ are merged
- Designed production-safe GitHub Actions workflows using conditional logic, path-based triggers, and permission-scoped job execution

---