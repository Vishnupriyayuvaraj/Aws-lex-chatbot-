# Part 4 — TransferFunds Intent & CloudFormation Deployment

## 🎯 Objective
Add a TransferFunds intent to BankerBot, then deploy the complete chatbot infrastructure using AWS CloudFormation (Infrastructure as Code).

---

## ✅ What I Did

### 1. Added TransferFunds Intent

**Sample utterances:**
- I want to transfer money
- Transfer funds
- Move money from my account
- I need to transfer {transferAmount} from {sourceAccount} to {targetAccount}
- Send {transferAmount} from {sourceAccount} to {targetAccount}

---

### 2. Configured Three Slots

#### Slot 1: sourceAccount
| Setting | Value |
|---|---|
| Name | `sourceAccount` |
| Slot type | `accountType` (custom) |
| Required | Yes |
| Prompt | "Which account would you like to transfer money FROM — Checking, Savings, or Credit?" |

#### Slot 2: targetAccount
| Setting | Value |
|---|---|
| Name | `targetAccount` |
| Slot type | `accountType` (custom) |
| Required | Yes |
| Prompt | "Which account would you like to transfer money TO — Checking, Savings, or Credit?" |

#### Slot 3: transferAmount
| Setting | Value |
|---|---|
| Name | `transferAmount` |
| Slot type | `AMAZON.Number` |
| Required | Yes |
| Prompt | "How much would you like to transfer?" |

---

### 3. Test TransferFunds Flow

```
User:  Transfer money
Bot:   Which account would you like to transfer FROM — Checking, Savings, or Credit?
User:  Savings
Bot:   Which account would you like to transfer TO — Checking, Savings, or Credit?
User:  Checking
Bot:   How much would you like to transfer?
User:  500
Bot:   Done! I've transferred $500.00 from your Savings to your Checking account.
       Is there anything else I can help you with?
```

---

### 4. AWS CloudFormation Deployment

CloudFormation lets you define your entire infrastructure in a YAML/JSON template and deploy it with one click.

**What CloudFormation deployed:**
- BankerBot (complete Lex bot with all intents)
- Lambda function (BankingBotEnglish V2)
- All IAM roles and permissions
- Bot alias configuration

**Deployment steps:**
1. AWS Console → **CloudFormation** → **Create Stack**
2. Upload `bankerbot-template.yaml`
3. Stack name: `BankerBotStack`
4. Review → **Create Stack**
5. Wait for `CREATE_COMPLETE` status (~2 minutes)

---

### 5. Compared Manual vs CloudFormation

| Aspect | Manual | CloudFormation |
|---|---|---|
| Time to deploy | ~1 hour | ~2 minutes |
| Reproducibility | Error-prone | Identical every time |
| Team sharing | Hard | Share the YAML file |
| Version control | Not possible | Git-trackable |
| Rollback | Manual | One-click rollback |

---

### 6. Explored the Visual Builder

The Visual Builder in Amazon Lex provides a drag-and-drop flow diagram of your bot's conversation paths. Useful for:
- Visualizing complex conversation flows
- Presenting bot design to non-technical stakeholders
- Spotting gaps in conversation logic

---

### 7. Resource Cleanup ⚠️

To avoid ongoing AWS charges, deleted all resources:

**Amazon Lex:**
- Bots → BankerBot → Delete

**AWS Lambda:**
- Functions → BankingBotEnglish → Delete

**CloudWatch:**
- Log Groups → `/aws/lambda/BankingBotEnglish` → Delete

**CloudFormation (if deployed):**
- Stacks → BankerBotStack → Delete

---

## 📸 Screenshot Checklist
- [ ] TransferFunds intent with all 3 slots
- [ ] Successful TransferFunds test conversation
- [ ] CloudFormation stack in CREATE_COMPLETE state
- [ ] CloudFormation-deployed bot in Lex console
- [ ] Visual Builder flow diagram
- [ ] Resource deletion confirmations

---

## 💡 Key Concepts Learned

**CloudFormation** — AWS service that provisions infrastructure from a template file. Enables Infrastructure as Code (IaC).

**Stack** — A collection of AWS resources managed as a single unit in CloudFormation.

**IaC (Infrastructure as Code)** — Managing infrastructure through code/config files instead of manual console clicks. Enables version control, repeatability, and automation.

**Visual Builder** — A graphical interface in Lex for designing and viewing conversation flows visually.

**Resource cleanup** — Always delete unused AWS resources to avoid unexpected charges. CloudFormation makes this easy — delete the stack and all resources are removed.

---

## 🔗 Resources
- [AWS CloudFormation Docs](https://docs.aws.amazon.com/cloudformation/)
- [Lex V2 Visual Builder](https://docs.aws.amazon.com/lexv2/latest/dg/visual-builder.html)
- [NextWork Project Part 4](https://link.nextwork.org/projects/aws-ai-lex4)
