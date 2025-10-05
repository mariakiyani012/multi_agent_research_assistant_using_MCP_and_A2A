
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Global application settings"""
    
    # API Keys
    openai_api_key: str
    serpapi_key: Optional[str] = None
    
    # Agent Configuration
    web_searcher_host: str = "localhost"
    web_searcher_port: int = 5001
    summarizer_host: str = "localhost"
    summarizer_port: int = 5002
    compiler_host: str = "localhost"
    compiler_port: int = 5003
    
    # Pipeline Configuration
    max_search_results: int = 5
    summary_max_tokens: int = 500
    pipeline_timeout: int = 300
    
    # OpenAI Configuration
    openai_model: str = "gpt-4"
    openai_temperature: float = 0.7
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
