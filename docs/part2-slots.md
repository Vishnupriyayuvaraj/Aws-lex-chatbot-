# Part 2 — Custom Slots & CheckBalance Intent

## 🎯 Objective
Build the CheckBalance intent with custom slot types so BankerBot can collect account type and date of birth from the user.

---

## ✅ What I Did

### 1. Created a Custom Slot Type — accountType

Custom slot types define the valid values for a slot.

| Setting | Value |
|---|---|
| Slot type name | `accountType` |
| Values | Checking, Savings, Credit |
| Synonyms | Checking: chequing / Savings: save / Credit: credit card |

> **Why synonyms?** Users say "chequing" or "credit card" — synonyms let Lex map these to the canonical value automatically.

---

### 2. Created CheckBalance Intent

**Sample utterances:**
- What's my balance?
- Check my balance
- How much do I have in my account?
- I want to check my account balance
- What is the balance in my {accountType} account?
- How much money is in my {accountType}?

---

### 3. Added Slots to CheckBalance

#### Slot 1: accountType
| Setting | Value |
|---|---|
| Name | `accountType` |
| Slot type | `accountType` (custom) |
| Required | Yes |
| Prompt | "For which account would you like your balance — Checking, Savings, or Credit?" |

#### Slot 2: dateOfBirth
| Setting | Value |
|---|---|
| Name | `dateOfBirth` |
| Slot type | `AMAZON.Date` (built-in) |
| Required | Yes |
| Prompt | "For security purposes, what is your date of birth?" |

---

### 4. Configured Confirmation Prompt

**Confirm:** "I'll look up the balance for your {accountType} account. Is that correct?"

**Decline:** "No problem. What else can I help you with?"

---

### 5. Closing Response

> "Thank you. I'll retrieve your {accountType} balance now."

*(Note: In Part 3, Lambda takes over actual fulfillment.)*

---

### 6. Build & Test

Test conversation flow:
```
User:  What's my balance?
Bot:   For which account would you like your balance — Checking, Savings, or Credit?
User:  Savings
Bot:   For security purposes, what is your date of birth?
User:  January 1, 1990
Bot:   I'll look up the balance for your Savings account. Is that correct?
User:  Yes
Bot:   Thank you. I'll retrieve your Savings balance now.
```

---

## 📸 Screenshot Checklist
- [ ] accountType slot type with values and synonyms
- [ ] CheckBalance intent with utterances
- [ ] Slots configuration panel
- [ ] Successful test conversation showing slot elicitation

---

## 💡 Key Concepts Learned

**Slot** — A piece of data the bot needs to collect from the user (like a form field).

**Slot type** — Defines what values are valid for a slot. Can be custom (your list) or built-in (AMAZON.Date, AMAZON.Number, etc.).

**Elicitation prompt** — The question the bot asks when it needs a slot value.

**Confirmation prompt** — Asks the user to confirm before fulfilling the intent — reduces errors.

**Built-in slot types** — AWS provides ready-made types like `AMAZON.Date`, `AMAZON.Number`, `AMAZON.EmailAddress` that handle NLU automatically.

---

## 🔗 Resources
- [Built-in Slot Types Reference](https://docs.aws.amazon.com/lexv2/latest/dg/howitworks-builtins-slots.html)
- [NextWork Project Part 2](https://link.nextwork.org/projects/aws-ai-lex2)
