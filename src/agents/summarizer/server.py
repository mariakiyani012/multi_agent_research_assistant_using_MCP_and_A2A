from src.agents.base import BaseAgent
from src.agents.summarizer.tools import summarize_articles

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__("summarizer", "Summarizes article content")
    
    def register_tools(self) -> None:
        # TODO: Register summarize_articles tool
        pass
    
    async def initialize(self) -> None:
        # TODO: Initialize OpenAI client
        pass
    
    async def cleanup(self) -> None:
        # TODO: Cleanup resources
        pass

if __name__ == "__main__":
    import asyncio
    agent = SummarizerAgent()
    asyncio.run(agent.run())
