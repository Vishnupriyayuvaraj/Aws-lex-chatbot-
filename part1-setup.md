# Part 1 — Create Your First Amazon Lex Bot

## 🎯 Objective
Set up an Amazon Lex V2 chatbot from scratch. By the end of this part, BankerBot can greet users and handle unrecognized input.

---

## ✅ What I Did

### 1. Navigated to Amazon Lex
- Opened the AWS Console → searched for **Amazon Lex**
- Clicked **Create bot**

### 2. Bot Configuration
| Setting | Value |
|---|---|
| Bot name | `BankerBot` |
| Description | AI-powered banking assistant |
| IAM permissions | Create a new role with basic Amazon Lex permissions |
| COPPA | No |
| Idle session timeout | 5 minutes |

### 3. Language Setup
- Language: **English (US)**
- Voice interaction: **Joanna** (Amazon Polly)
- Intent classification confidence score threshold: `0.40`

### 4. WelcomeIntent
Created the first intent so BankerBot can greet users.

**Sample utterances added:**
- Hi
- Hello
- I need help
- Can you help me?
- What can you do?

**Closing response:**
> "Hi! I'm BankerBot, your virtual banking assistant. How can I help you today?"

### 5. FallbackIntent
Configured the built-in fallback for anything the bot doesn't understand.

**Closing response:**
> "Sorry, I'm having trouble understanding. Could you please rephrase that?"

### 6. Build & Test
- Clicked **Build** (took ~30 seconds)
- Tested in the **Test** panel on the right
- Confirmed: "Hi" → BankerBot responds with welcome message
- Confirmed: Random text → FallbackIntent fires

---

## 📸 Screenshot Checklist
- [ ] Bot creation form filled out
- [ ] WelcomeIntent with utterances
- [ ] Test panel showing a successful greeting
- [ ] FallbackIntent response in test

---

## 💡 Key Concepts Learned

**Intent** — A goal or action the user wants to accomplish (e.g., greet the bot, check balance).

**Utterance** — A sample phrase a user might say to trigger an intent. Lex uses NLU to match variations too.

**FallbackIntent** — A built-in intent that fires when no other intent matches with enough confidence.

**Bot alias** — A pointer to a specific bot version. `TestBotAlias` is automatically created for testing.

---

## 🔗 Resources
- [Amazon Lex V2 Documentation](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)
- [NextWork Project Part 1](https://link.nextwork.org/projects/aws-ai-lex1)
