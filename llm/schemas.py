from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]

class LLMMessage(BaseModel):
    role: str
    content: str

class LLMResponse(BaseModel):
    message: LLMMessage
    tool_calls: Optional[List[ToolCall]] = None

class Command(BaseModel):
    intent: str
    normalized_text: str
    tool: Optional[str] = None
    params: Dict[str, Any] = {}
    confidence: float = 1.0
