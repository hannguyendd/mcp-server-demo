# MCP Server Demo

A simple demonstration of a Model Context Protocol (MCP) server implementation that provides tool functionality to upgrade applications via a shell script.

## Overview

This project implements a FastMCP server that exposes a custom tool for upgrading applications. The server communicates via stdio transport and can be integrated with MCP-compatible clients.

## Features

- MCP server with a custom tool to upgrade applications
- Command execution via subprocess
- Environment variable configuration
- Stdio transport for client-server communication

## Prerequisites

- Python 3.12 or higher
- uv package manager (for dependency management)
- Environment variables setup (COMMAND_FOLDER_PATH)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mcp-server-demo
   ```

2. Install dependencies using uv:
   ```
   uv pip install -e .
   ```

3. Create a `.env` file in the project root with the following content:
   ```
   COMMAND_FOLDER_PATH=/path/to/your/command/folder
   ```
   Make sure the command folder contains the `update-apps.sh` script.

## Usage

The server can be run directly with Python:

```
python main.py
```

### Using with VS Code MCP Extension

You can use the VS Code MCP extension with the provided `mcp.json` configuration:

1. Install the MCP extension in VS Code
2. Open the project in VS Code
3. Use the "Connect to MCP Server" command and select "commander" server

### Using with MCP Inspector

To test and inspect the MCP server using the MCP Inspector tool:

```bash
npx @modelcontextprotocol/inspector \
  uv \
  --directory ${PWD} \
  run \
  main.py
```

This command runs the Inspector tool which connects to the MCP server and allows you to interact with the available tools for testing purposes.

## Available Tools

### upgrade_apps

This tool executes the `update-apps.sh` script located in the folder specified by the `COMMAND_FOLDER_PATH` environment variable.

Example client usage:
```python
result = await client.upgrade_apps()
print(result)
```

## Project Structure

- `main.py` - Main server implementation
- `pyproject.toml` - Project dependencies and metadata
- `.vscode/mcp.json` - VS Code MCP configuration
- `uv.lock` - Dependency lock file for uv package manager
- `.env` - Environment variables (not included in repository)

## Dependencies

- mcp[cli] (>=1.6.0)
- python-dotenv (required but not explicitly mentioned in pyproject.toml)

## Development

This project uses `uv` for Python package management, which provides faster dependency resolution and installation compared to traditional pip.

To update dependencies:
```
uv pip install -e .
```

## License

[Include license information here]

## Contributing

[Include contribution guidelines here]