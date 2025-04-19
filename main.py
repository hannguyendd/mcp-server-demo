import os
import subprocess
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
COMMAND_FOLDER_PATH = os.getenv("COMMAND_FOLDER_PATH", "")

if not COMMAND_FOLDER_PATH:
    raise ValueError("COMMAND_FOLDER_PATH environment variable is not set.")
else:
    print(f"COMMAND_FOLDER_PATH: {COMMAND_FOLDER_PATH}")


@mcp.tool()
async def upgrade_apps() -> str:
    """Upgrade all apps by custom command."""

    return _execute_command("update-apps.sh")


def _execute_command(name: str) -> str:
    # Define the command to upgrade apps
    command = f"cd {COMMAND_FOLDER_PATH} && ./update-apps.sh"
    print(f"Executing command: {command}")

    # Execute the command and capture output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    return result.stdout or result.stderr or "No output"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
