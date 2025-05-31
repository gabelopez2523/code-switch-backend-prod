from pydantic import BaseModel
from typing import Optional

class EmailRequest(BaseModel):
    user_input: str
    scenario_context: Optional[str] = None
    tone: Optional[str] = "professional"
    language: Optional[str] = "english"

class EmailResponse(BaseModel):
    enhanced_email: str