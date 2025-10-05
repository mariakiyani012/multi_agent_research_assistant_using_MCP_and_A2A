from src.agents.base import BaseAgent
from src.agents.web_searcher.tools import search_web

class WebSearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("web_searcher", "Searches web for relevant articles")
    
    def register_tools(self) -> None:
        # TODO: Register search_web tool with MCP server
        pass
    
    async def initialize(self) -> None:
        # TODO: Initialize HTTP session, API clients
        pass
    
    async def cleanup(self) -> None:
        # TODO: Cleanup resources
        pass

if __name__ == "__main__":
    import asyncio
    agent = WebSearcherAgent()
    asyncio.run(agent.run())

