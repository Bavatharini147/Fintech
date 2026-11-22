
import requests
import json
import streamlit as st


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


@st.cache_data(show_spinner=False)
def classify_transaction(description):

    prompt = f"""
You are a strict financial transaction classifier.

Classify the transaction using ONLY the merchant or transaction
description provided.

Choose exactly one category:

1. Essential
2. Discretionary
3. Needs Review

STRICT CLASSIFICATION RULES:

ESSENTIAL:
- Grocery Store
- Medical shops and pharmacies
- Electricity bills
- Water bills
- Mobile Recharge
- Metro, bus, train and public transport

DISCRETIONARY:
- Swiggy
- Zomato
- Restaurants
- Food delivery
- Cafes
- Movies and entertainment
- Gaming and leisure activities

NEEDS REVIEW:
- Amazon
- Flipkart
- Uber
- Book Store
- Unknown merchant names
- Transactions whose purpose is unclear

IMPORTANT:
- Swiggy and Zomato MUST be Discretionary.
- Restaurants MUST be Discretionary.
- Grocery Store MUST be Essential.
- Metro MUST be Essential.
- Mobile Recharge MUST be Essential.
- Never classify Swiggy as an electricity bill.
- Never use the same reason for unrelated transactions.
- Do not invent the purpose of a transaction.
- If uncertain, select Needs Review.
- The reason must explain the actual merchant description.


Transaction Description: {description}

Return ONLY valid JSON:
{{
    "classification": "Essential",
    "confidence": 0.95,
    "reason": "Short explanation based on the transaction."
}}
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0
                }
            },
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        ai_output = json.loads(result["response"])

        classification = ai_output.get("classification")

        if classification not in [
            "Essential",
            "Discretionary",
            "Needs Review"
        ]:
            classification = "Needs Review"

        confidence = ai_output.get("confidence", 0)

        try:
            confidence = float(confidence)
        except (ValueError, TypeError):
            confidence = 0

        confidence = max(0.0, min(1.0, confidence))

        reason = str(ai_output.get("reason", "No explanation provided."))

        return {
            "classification": classification,
            "confidence": confidence,
            "reason": reason
        }

    except requests.exceptions.RequestException:
        return {
            "classification": "Needs Review",
            "confidence": 0.0,
            "reason": "Could not connect to the Ollama AI service."
        }

    except (ValueError, KeyError, TypeError):
        return {
            "classification": "Needs Review",
            "confidence": 0.0,
            "reason": "AI returned an invalid response."
        }
