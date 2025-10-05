
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from enum import Enum

class CitationFormat(str, Enum):
    APA = "apa"
    MLA = "mla"
    CHICAGO = "chicago"

class SearchResult(BaseModel):
    """Search result from web searcher agent"""
    url: HttpUrl
    title: str
    snippet: str
    content: Optional[str] = None

class ArticleSummary(BaseModel):
    """Summarized article from summarizer agent"""
    url: HttpUrl
    title: str
    summary: str
    key_points: List[str] = Field(default_factory=list)

class ResearchReport(BaseModel):
    """Final compiled research report"""
    query: str
    report: str
    citations: List[str]
    word_count: int
    format: CitationFormat = CitationFormat.APA

class AgentResponse(BaseModel):
    """Generic agent response wrapper"""
    agent_name: str
    success: bool
    data: Any
    error: Optional[str] = None

