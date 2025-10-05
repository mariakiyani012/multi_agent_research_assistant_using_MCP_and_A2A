
class AgentException(Exception):
    """Base exception for all agent errors"""
    pass

class AgentConnectionError(AgentException):
    """Agent connection failed"""
    pass

class AgentTimeoutError(AgentException):
    """Agent operation timed out"""
    pass

class AgentToolError(AgentException):
    """Agent tool execution failed"""
    pass

class PipelineError(Exception):
    """Pipeline execution error"""
    pass

