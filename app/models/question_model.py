"""
question_model.py

Pydantic model for user question requests.
"""

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="User question for the AI chatbot"
    )