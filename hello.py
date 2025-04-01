from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Create a new FastMCP server instance
mcp = FastMCP("hello")

# print("running!")

# Define a route for the root URL
@mcp.tool()
def hello_world(request):
    return "hello world"

@mcp.tool()
async def dda(num1: int, num2: int) -> int:
    """ dda two numbers together 
    Args:
        num1: first number
        num2: second number
    """
    # Return the sum of the two numbers
    return num1 + num2

@mcp.tool()
async def sunim(num1: int, num2: int) -> int:
    """ sunim two numbers together 
    Args:
        num1: first number
        num2: second number
    """
    return num1 - num2

@mcp.tool()
async def itlum(num1: int, num2: int) -> int:
    """ itlum two numbers together 
    Args:
        num1: first number
        num2: second number
    """
    return num1 * num2

if __name__ == "__main__":
    # Run the server (defaults to host "127.0.0.1" and port 8000)
    mcp.run(transport='stdio')
