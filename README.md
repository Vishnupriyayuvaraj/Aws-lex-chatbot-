# 🤖 BankerBot — AI Chatbot with Amazon Lex

> An AI-powered banking assistant built on AWS Amazon Lex V2, integrated with AWS Lambda and deployed via CloudFormation.

![AWS](https://img.shields.io/badge/AWS-Amazon_Lex_V2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![CloudFormation](https://img.shields.io/badge/AWS-CloudFormation-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📌 Project Overview

**BankerBot** is a conversational AI chatbot that simulates a bank's virtual assistant. Customers can:
- ✅ Check their account balance
- ✅ Transfer money between accounts
- ✅ Get personalized responses using AWS Lambda backend logic

This project was built as a 4-part series following the [NextWork](https://nextwork.org) AWS curriculum, covering Amazon Lex V2 from zero to a fully deployed, Lambda-integrated chatbot.

---

## 🗂️ Project Structure

```
aws-lex-chatbot/
├── README.md                     # You are here
├── lambda/
│   └── lambda_function.py        # Lambda backend for BankerBot
├── cloudformation/
│   └── bankerbot-template.yaml   # CloudFormation stack (Part 4)
├── docs/
│   ├── part1-setup.md            # Part 1 walkthrough notes
│   ├── part2-slots.md            # Part 2 walkthrough notes
│   ├── part3-lambda.md           # Part 3 walkthrough notes
│   └── part4-cloudformation.md   # Part 4 walkthrough notes
└── screenshots/                  # Add your own screenshots here
    └── .gitkeep
```

---

## 🧩 Architecture

```
User Input
    │
    ▼
Amazon Lex V2 (BankerBot)
    │   ├── Intent: WelcomeIntent
    │   ├── Intent: CheckBalance
    │   │       └── Slots: accountType, dateOfBirth
    │   ├── Intent: TransferFunds
    │   │       └── Slots: sourceAccount, targetAccount, transferAmount
    │   └── Intent: FallbackIntent
    │
    ▼
AWS Lambda (BankingBotEnglish)
    │   └── Validates slots, returns mock balance data
    │
    ▼
Response → User
```

---

## 📚 Series Breakdown

### Part 1 — Create Your First Lex Bot
- Set up Amazon Lex V2 in AWS Console
- Created **BankerBot** from scratch
- Added **WelcomeIntent** with sample utterances
- Configured **FallbackIntent** for unrecognized input
- Built and tested the bot in the Lex console

**Key concepts:** Intents, Utterances, Bot aliases, Test console

---

### Part 2 — Custom Slots & CheckBalance Intent
- Created a custom slot type: **accountType** (Checking, Savings, Credit)
- Built **CheckBalance** intent with two slots:
  - `accountType` — what type of account
  - `dateOfBirth` — for identity verification
- Configured confirmation prompts and slot elicitation prompts
- Tested the full balance-checking conversation flow

**Key concepts:** Slot types, Slot elicitation, Confirmation prompts

---

### Part 3 — AWS Lambda Integration
- Created **BankingBotEnglish** Lambda function (Python 3.12)
- Wrote handler logic to validate slots and return mock balance data
- Connected Lambda to BankerBot via the **TestBotAlias**
- Tested end-to-end: Lex → Lambda → response back to user

**Key concepts:** Lambda fulfillment, Lex-Lambda integration, Event parsing

---

### Part 4 — CloudFormation & TransferFunds Intent
- Added **TransferFunds** intent with 3 slots
- Used **AWS CloudFormation** to deploy infrastructure as code
- Deployed a pre-built bot stack and compared with manual build
- Explored the **Visual Builder** for flow-based bot design
- Cleaned up all AWS resources to avoid charges

**Key concepts:** CloudFormation, IaC, Visual Builder, Resource cleanup

---

## 🛠️ Setup & Deployment

### Prerequisites
- AWS Account (Free Tier works)
- IAM permissions for Lex, Lambda, CloudFormation, CloudWatch
- Basic Python knowledge

### Step 1 — Deploy the Lambda Function
1. Go to **AWS Lambda** → Create function
2. Name it `BankingBotEnglish`, Runtime: **Python 3.12**
3. Paste the code from [`lambda/lambda_function.py`](./lambda/lambda_function.py)
4. Deploy the function

### Step 2 — Create the Lex Bot
1. Go to **Amazon Lex** → Create bot
2. Name: `BankerBot`, IAM: Create new role
3. Add intents: `WelcomeIntent`, `CheckBalance`, `TransferFunds`, `FallbackIntent`
4. Configure slots as described in the [docs](./docs/)

### Step 3 — Connect Lambda to Lex
1. In Lex console → your bot → Aliases → TestBotAlias
2. Under **Languages** → English → set Lambda function to `BankingBotEnglish`
3. Rebuild the bot and test

### Step 4 — (Optional) Deploy via CloudFormation
```bash
# Upload the template in AWS CloudFormation Console
# Stack name: BankerBotStack
# Review and Create Stack
```

---

## 💻 Lambda Function

The Lambda function handles fulfillment for the **CheckBalance** intent. It validates the `accountType` slot and returns a mock balance.

See full code: [`lambda/lambda_function.py`](./lambda/lambda_function.py)

```python
# Sample response structure
def close(intent_request, session_attributes, fulfillment_state, message):
    intent_request['sessionState']['intent']['state'] = fulfillment_state
    return {
        'sessionState': {
            'sessionAttributes': session_attributes,
            'dialogAction': { 'type': 'Close' },
            'intent': intent_request['sessionState']['intent']
        },
        'messages': [message],
        ...
    }
```

---

## 🧹 Resource Cleanup

To avoid AWS charges after completing the project:

1. **Amazon Lex** → Bots → Select BankerBot → Delete
2. **AWS Lambda** → Functions → Delete `BankingBotEnglish`
3. **CloudWatch** → Log groups → Delete `/aws/lambda/BankingBotEnglish`
4. **CloudFormation** → Stacks → Delete `BankerBotStack` (if deployed)

---

## 📸 Screenshots

Add your own screenshots to the `/screenshots` folder documenting:
- Bot creation in Lex console
- Intent and slot configuration
- Test conversation results
- Lambda function setup
- CloudFormation stack deployment

---

## 🏷️ Tags

`AWS` `Amazon Lex` `Chatbot` `Lambda` `CloudFormation` `NLP` `AI` `Python` `Serverless` `Cloud Computing` `NextWork`

---

## 📄 License

This project is for educational purposes. Built following the [NextWork](https://nextwork.org) AWS curriculum.
