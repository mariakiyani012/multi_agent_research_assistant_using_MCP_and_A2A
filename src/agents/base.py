from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
import logging

class BaseAgent(ABC):
    """Base class for all MCP agents"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.server = Server(name)
        self.logger = logging.getLogger(f"agent.{name}")
        self._setup_logging()
        
    def _setup_logging(self) -> None:
        """Configure agent-specific logging"""
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            f'[{self.name}] %(asctime)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    @abstractmethod
    def register_tools(self) -> None:
        """Register MCP tools for this agent"""
        pass
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize agent resources"""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup agent resources"""
        pass
    
    async def run(self) -> None:
        """Start the MCP server"""
        self.logger.info(f"Starting {self.name} agent...")
        await self.initialize()
        self.register_tools()
        
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )
    
    def get_server(self) -> Server:
        """Get the MCP server instance"""
        return self.server


