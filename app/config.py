from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #llm config
    open_ai_api_key: str
    primary_model: str = "gpt-4o-mini"
    fallback_model: str = "gpt-4o-mini"

    #langsmith
    langchain_tracing_v2: bool = True
    langchain_api_key: str
    langchain_project: str = "prod-api"
    
    #app
    app_env: str = "development"
    log_level: str = "INFO"
    rate_limit: str ="20/minute"
    max_retries: int = 3
    
    model_config =  {"env_file": ".env", "extra": "ignore"}

    @property
    def isProduction(self) ->bool:
        return self.app_env =="production"

@lru_cache()
def get_settings() -> Settings:
    return Settings()