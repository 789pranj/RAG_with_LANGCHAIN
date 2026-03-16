from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)


review_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "Short 1–2 sentence summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "mixed"],
            "description": "Overall sentiment of the review"
        },
        "rating": {
            "type": "number",
            "minimum": 1,
            "maximum": 5,
            "description": "Rating between 1–5 stars"
        },
        "key_points": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Key points extracted from the review"
        },
        "pros": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Positive aspects mentioned"
        },
        "cons": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Negative aspects mentioned"
        }
    },
    "required": ["summary", "sentiment", "key_points"]
}

# Attach schema
structured_model = model.with_structured_output(schema=review_schema)

result = structured_model.invoke("""
This laptop is excellent for performance and multitasking.
The screen is great and speakers are loud. 
However, the battery drains quickly and the body heats up during gaming.
""")

print(json.dumps(result, indent=4))
