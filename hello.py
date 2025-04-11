from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from datetime import datetime

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

@mcp.tool()
async def is_weekend():
    """ Check if today is a weekend """
    # Get the current day of the week
    current_day = datetime.now().weekday()
    
    # Check if the day is a weekend (Saturday or Sunday)
    return current_day >= 5

@mcp.tool()
async def fibonacci(n: int) -> int:
    """ Calculate the nth Fibonacci number
    Args:
        n: Position in Fibonacci sequence (starting from 0)
    Returns:
        The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    # Run the server (defaults to host "127.0.0.1" and port 8000)
    mcp.run(transport='stdio')
