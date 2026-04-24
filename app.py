import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🔍 Network Log Analyzer")

logs = st.text_area("Paste router logs")

def analyze_logs(logs):
    prompt = f"""
You are a network QA expert.

Analyze logs:
{logs}

Give:
- Summary
- Root cause
- Validation commands
- Fix suggestions
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

if st.button("Analyze"):
    if logs:
        result = analyze_logs(logs)
        st.write(result)