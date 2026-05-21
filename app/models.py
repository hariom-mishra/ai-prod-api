from time import timezone
from pydantic import BaseModel, Field
from datetime import datetime

class ChatRequest(BaseModel):
    message: str = Field(min_length=0, max_length=1000, description="user's prompt")
    session_id: str =Field(default="default", description="Conversation thread id")

class ChatResponse(BaseModel):
    response: str
    model_used: str
    session_id: str
    chached:bool = False
    processing_time: float
    timestampt: str = Field(default_factory= lambda: datetime.now(timezone.utc).isoformat())    

class HealthResponse(BaseModel):
    status: str = "OK"
    environment:str
    version:str ="1.0.0"
    checks: dict = {}

class MetricsResponse(BaseModel):
    total_requests: int
    total_error: int
    error_rate: str
    avg_latency_ms: float
    cache_hit_rate: str
    total_input_tokens: int
    total_output_tokens: int

class ErrorResponse(BaseModel):
    error: str
    detail:str | None = None
    requirest_id: str | None = None
    
