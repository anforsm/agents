from typing import Any
import httpx
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather_data(location: str) -> str:
    """Fetches weather data for a given location."""
    return json.dumps({
        "location": location,
        "temperature": 25.0,
        "humidity": 60.0,
        "wind_speed": 10.0,
        "wind_direction": "NW"
    })

if __name__ == "__main__":
    mcp.run(transport='stdio')
