# 🧪 Lab 02 - Build an AI Chat Application

## Overview

Welcome to **Lab 02** of the **Agentic AI Workshop**.

In Lab 01, we connected Python to a Large Language Model (LLM) and sent a single prompt.

In this lab, we will build an **interactive AI Chat Application** where users can continuously communicate with the LLM until they choose to exit.

> **Note:** This is still **not an AI Agent**. It is an interactive chat application. In the upcoming labs, we will gradually add Prompt Engineering, Memory, Tool Calling, LangChain, MCP, and Agent capabilities.

---

## Learning Objectives

After completing this lab, you will be able to:

- Build an interactive AI Chat Application
- Accept user input dynamically
- Send multiple prompts to an LLM
- Display AI responses
- Handle user exit conditions
- Implement basic exception handling

---

## Prerequisites

- Completion of Lab 01
- Python 3.11 or later
- Visual Studio Code
- OpenAI API Key
- Internet Connection

---

## Project Structure

```
Lab02_AI_Chat_Application

│── src
│     └── 02_ai_chat_application.py

│── .env
│── .env.example
│── .gitignore
│── requirements.txt
│── README.md
```

---

## Step 1 - Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

---

## Step 2 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 - Configure API Key

Create a file named

```
.env
```

Add

```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Never commit your API key to GitHub.

---

## Step 4 - Run the Application

```bash
python src/02_ai_chat_application.py
```

---

## Expected Output

```
============================================================
🤖 AI Chat Application
Type 'exit' to quit
============================================================

You : Hi

AI :
Hello! How can I help you today?

------------------------------------------------------------

You : Explain LangChain

AI :
LangChain is an open-source framework...

------------------------------------------------------------

You : exit

👋 Thank you! Have a great day.
```

---

## Try These Questions

```
What is Agentic AI?

Explain LangChain.

What is MCP?

Write a Python program to reverse a string.

Explain Machine Learning in simple English.
```

---

## Common Errors

### Invalid API Key

Verify your `.env` file.

---

### Module Not Found

Install dependencies

```bash
pip install -r requirements.txt
```

---

### Internet Connection Error

Verify your internet connection and API access.

---

## Key Takeaways

In this lab, you learned how to:

- Build an interactive AI Chat Application
- Accept user input dynamically
- Send multiple prompts
- Receive AI responses
- Exit the application gracefully
- Handle runtime exceptions

---

## Is This an AI Agent?

**No.**

This application can:

✅ Answer questions

✅ Accept multiple prompts

But it cannot:

❌ Remember previous conversations

❌ Use external tools

❌ Plan tasks

❌ Make autonomous decisions

We will add these capabilities in the upcoming labs.

---

## Next Lab

➡️ **Lab 03 - Prompt Engineering**

---

## Workshop

**Agentic AI Workshop**

Developed by **Teltam.in**

© 2026 MLK Tech. All Rights Reserved.