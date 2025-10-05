from typing import List
from src.models.schemas import SearchResult, ArticleSummary

async def summarize_articles(articles: List[SearchResult]) -> List[ArticleSummary]:
    # TODO: Implement summarization with OpenAI
    pass