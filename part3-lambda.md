# Part 3 — AWS Lambda Integration

## 🎯 Objective
Connect BankerBot to an AWS Lambda function so it can run real business logic — validating inputs and returning dynamic (mock) account balances.

---

## ✅ What I Did

### 1. Created the Lambda Function

| Setting | Value |
|---|---|
| Function name | `BankingBotEnglish` |
| Runtime | Python 3.12 |
| Architecture | x86_64 |
| Permissions | Create new role with basic Lambda permissions |

---

### 2. Wrote the Lambda Handler

The function receives an event from Lex, reads the intent name and slots, and returns a structured response.

**Key event structure from Lex:**
```json
{
  "sessionState": {
    "intent": {
      "name": "CheckBalance",
      "slots": {
        "accountType": { "value": { "interpretedValue": "Savings" } },
        "dateOfBirth":  { "value": { "interpretedValue": "1990-01-01" } }
      }
    }
  },
  "invocationSource": "FulfillmentCodeHook"
}
```

**Lambda returns:**
```json
{
  "sessionState": {
    "dialogAction": { "type": "Close" },
    "intent": { "name": "CheckBalance", "state": "Fulfilled" }
  },
  "messages": [
    { "contentType": "PlainText", "content": "Your Savings balance is $4,231.50." }
  ]
}
```

Full code: [`../lambda/lambda_function.py`](../lambda/lambda_function.py)

---

### 3. Two Invocation Sources

Lambda can be called at two points in the Lex conversation:

| Source | When | Purpose |
|---|---|---|
| `DialogCodeHook` | During slot collection | Validate each slot as it's filled |
| `FulfillmentCodeHook` | After all slots confirmed | Execute the final business logic |

---

### 4. Connected Lambda to BankerBot

**Steps:**
1. Amazon Lex Console → **BankerBot**
2. Left sidebar → **Aliases** → **TestBotAlias**
3. Under **Languages** → **English (US)**
4. Set Lambda function: `BankingBotEnglish`
5. Version: `$LATEST`
6. **Save**
7. Rebuild the bot

---

### 5. Enabled Lambda on CheckBalance Intent

1. Open **CheckBalance** intent
2. Scroll to **Fulfillment** section
3. Toggle ON: **Use a Lambda function for fulfillment**
4. Save intent → Rebuild

---

### 6. Tested End-to-End

```
User:  Check my balance
Bot:   For which account — Checking, Savings, or Credit?
User:  Checking
Bot:   What is your date of birth?
User:  March 15 1985
Bot:   Thank you for verifying your identity!
       Your Checking account balance is $1,847.32.
       Is there anything else I can help you with?
```

Lambda log visible in **CloudWatch** → Log Groups → `/aws/lambda/BankingBotEnglish`

---

## 📸 Screenshot Checklist
- [ ] Lambda function creation screen
- [ ] Lambda code editor with handler code
- [ ] Lex alias → Language → Lambda connection
- [ ] Successful test conversation with dynamic balance
- [ ] CloudWatch log showing the Lambda invocation

---

## 💡 Key Concepts Learned

**Lambda function** — Serverless compute that runs your code on demand. No servers to manage.

**Fulfillment hook** — Lambda called after all slots are collected and confirmed. Used for final business logic.

**Dialog hook** — Lambda called during each turn of the conversation. Used to validate slots in real time.

**CloudWatch Logs** — Automatically captures Lambda output. Essential for debugging.

**`$LATEST`** — The most recent unpublished version of a Lambda function. Fine for development; use versioning in production.

---

## 🔗 Resources
- [Lex V2 Lambda Integration](https://docs.aws.amazon.com/lexv2/latest/dg/lambda.html)
- [Lambda Response Format for Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-response-format.html)
- [NextWork Project Part 3](https://link.nextwork.org/projects/aws-ai-lex3)
