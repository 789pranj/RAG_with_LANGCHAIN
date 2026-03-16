from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, List, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

class Review(BaseModel):
    summary: Annotated[str, Field(description="Short 1–2 sentence summary of the review")]
    sentiment: Annotated[str, Field(description="Overall sentiment: positive, negative or mixed")]
    rating: Annotated[Optional[float], Field(description="Product rating from 1 to 5 stars")] = None
    key_points: Annotated[List[str], Field(description="Bullet points summarizing the review")] = []
    pros: Annotated[Optional[List[str]], Field(description="Optional pros list")] = None
    cons: Annotated[List[str], Field(description="Cons or weaknesses highlighted")] = []

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
This laptop is excellent for performance and multitasking.
The screen is great and speakers are loud. 
However, the battery drains quickly and the body heats up during gaming.
""")

print(result)
