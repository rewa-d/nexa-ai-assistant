
from collections.abc import Callable

from src.tools.calculator import calculate
from src.tools.date_time import get_current_datetime
from src.tools.file_search import search_files
from src.tools.app_launcher import open_application


AVAILABLE_TOOLS: dict[str, Callable] = {
    "calculate": calculate,
    "get_current_datetime": get_current_datetime,
    "search_files": search_files,
    "open_application": open_application
}


def get_tool_definitions() -> list[Callable]:
    """Return approved functions available to Ollama."""
    return list(AVAILABLE_TOOLS.values())


def execute_tool(name: str, arguments: dict) -> str:
    """Execute an approved tool."""

    tool = AVAILABLE_TOOLS.get(name)

    if tool is None:
        return f"Unknown tool: {name}"

    if not isinstance(arguments, dict):
        return "Tool error: arguments must be a dictionary."

    try:
        result = tool(**arguments)
        return str(result)

    except (ValueError, TypeError) as error:
        return f"Tool error: {error}"
