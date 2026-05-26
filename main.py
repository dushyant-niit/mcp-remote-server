import random
from fastmcp import FastMCP
import json

# Create instance of FastMCP Server
mcp = FastMCP(name="Simple Calculator Server")

@mcp.tool
def random_number(min_val: int = 1, max_val:int =100) -> int:
    """Generate random number within range"""
    return random.randint(min_val,max_val)

@mcp.tool
def add_numbers(a: int,b: int) -> int:
    """Add two numbers"""
    return a + b

# Resource server information

@mcp.resource("info://server")
def server_info() -> str:
    """Get the information about this server"""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with maths tools",
        "tools" :["add","random_number"],
        "author" : "mr abc"
    }

    return json.dumps(info, indent =2 )

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
