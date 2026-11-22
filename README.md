## Project
AI-Powered Discretionary Spending analyzer and Improvised simulated Payment System.

## Overview
AI finds the user's discretionary spending by classifying transaction statements into Essential or Discretionary and then provides insights of how much is spent unnecessarily.

Moreover, a unique payment system is made with new featured wallet option where the wallet has 2 compartments: Savings compartment & Spending compartment.
(This doesn't mean 2 accounts but a single one)
While making payments only the Spending compartment's balance is used where the savings compartment's money will be restricted for payment process and will act as a piggy bank. This feature is made to reserve a money as savings within UPI options.
When there is insufficient balance in Spending compartment, the payment will not be done though the savings compartment has enough money.
In case of an emergency, savings money can be used for payment after transferring the money from savings to spending compartment by the user.
Vice-versa transferring of money between the compartments is also possible.

## Key Features
1. AI-Powered Discretionary Spending Classification
2. Digital Wallet Management
3. Simulated Payment Process
4. UPI Spending Analysis

## Requirements

### 1. Software Requirements
- Python
- Visual Studio Code
- Ollama
- Llama 3.2:3b
### 2. Python Packages
-streamlit
-pandas
-requests
-pypdf
-matplotlib

## Installation and Setup

Install Python and Visual Studio Code.

Install Ollama using the official Ollama installer.

Download the Llama 3.2:3b model using Command Prompt:

ollama pull llama3.2:3b

Create and activate a Python virtual environment.

Install the required Python packages:

pip install -r requirements.txt

Start the Ollama service:

ollama serve

Run the application:

streamlit run app.py

## Working Principle

### 1. AI-Powered Discretionary Spending

User uploads a UPI transaction statement PDF.

↓

The application extracts transaction details from the PDF.

↓

The extracted transaction data is cleaned and processed.

↓

Only debit transactions are considered for discretionary spending analysis.

↓

The transaction descriptions are sent to the Llama 3.2:3b model through Ollama along with carefully formulated system prompts.

↓

Llama processes each transaction using its trained knowledge and the classification instructions.

↓

The AI classifies transactions into Essential, Discretionary, or Needs Review categories.

↓

The application displays the classification, AI confidence score, and reason for each transaction.

### 2. Digital Wallet Management

User opens the Wallet section.

↓

The user verifies access using the account number.

↓

The application displays Total Balance, Savings Balance, and Spending Balance.

↓

User chooses to transfer money between Savings and Spending compartments.

↓

The application checks the available balance in the source compartment.

↓

If sufficient funds are available, the transfer is completed and the corresponding wallet balances are updated.

### 3. Simulated Payment Process

User selects the Payments section.

↓

User enters the recipient's mobile number or selects the QR code upload option.

↓

User enters the payment amount.

↓

The application requests password verification.

↓

The application checks the available Balance in Spending Compartment. The amount in Savings compartment is untouched.

↓

If sufficient funds are available in Spending compartment, the payment is processed and the wallet balance is updated.

↓

The payment result is displayed to the user.

### 4. UPI Spending Analysis

User uploads a UPI statement PDF.

↓

The application extracts and cleans transaction details.

↓

The application calculates total spending, total received amount, and other transaction statistics.

↓

Spending summaries, recipient details, and visualizations are displayed.

## Conclusion

This app integrates AI-powered discretionary spending classification with digital wallet management and a simulated payment system. By using the Llama 3.2:3b model, the application helps users understand their spending patterns and distinguish essential expenses from discretionary expenses. The integrated wallet and payment modules provide a structured approach to managing savings, spending, and payments within a single application.
