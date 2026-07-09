"""
login_model.py

Pydantic model for user login requests.
"""

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        description="Username"
    )

    password: str = Field(
        ...,
        min_length=4,
        description="Password"
    )