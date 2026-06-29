import json
import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def recommend_careers(subjects: list, interests: str, strengths: str):
    """
    Uses Groq to recommend 3 career paths based on user inputs.
    Returns (top_careers, career_info) in the format expected by app.py.
    """

    prompt = f"""
You are an expert career counsellor for students aged 13–25.

Based on the student profile below, recommend exactly 3 career paths.

Student Profile:
- Favourite Subjects: {', '.join(subjects) if subjects else 'Not specified'}
- Interests: {interests or 'Not specified'}
- Strengths: {strengths or 'Not specified'}

Respond ONLY with a valid JSON object. No explanation, no markdown, no backticks.

The JSON must follow this exact structure:
{{
  "careers": [
    {{
      "name": "Career Title",
      "score": 85,
      "powers": ["Skill 1", "Skill 2", "Skill 3", "Skill 4"],
      "mission": "A specific first action the student can take this week to start this career path.",
      "journey": "A 2-3 sentence description of the educational and professional journey for this career.",
      "obstacle": "The single biggest challenge they will face on this path."
    }},
    {{
      "name": "Career Title",
      "score": 78,
      "powers": ["Skill 1", "Skill 2", "Skill 3"],
      "mission": "A specific first action the student can take this week.",
      "journey": "A 2-3 sentence educational/professional journey.",
      "obstacle": "The biggest challenge they will face."
    }},
    {{
      "name": "Career Title",
      "score": 72,
      "powers": ["Skill 1", "Skill 2", "Skill 3"],
      "mission": "A specific first action the student can take this week.",
      "journey": "A 2-3 sentence educational/professional journey.",
      "obstacle": "The biggest challenge they will face."
    }}
  ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=1500,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    data = json.loads(raw)

    careers = data["careers"]

    # Build outputs in the format app.py expects
    top_careers = [(c["name"], c["score"]) for c in careers]

    career_info = {
        c["name"]: {
            "powers":   c["powers"],
            "mission":  c["mission"],
            "journey":  c["journey"],
            "obstacle": c["obstacle"],
        }
        for c in careers
    }

    return top_careers, career_info
