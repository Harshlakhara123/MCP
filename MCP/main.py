import random
from fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def get_random_number(n_dice: int) -> int:
    """Get a random number between 1 and n_dice."""
    return random.randint(1, n_dice)

if __name__ == "__main__":
    mcp.run()
