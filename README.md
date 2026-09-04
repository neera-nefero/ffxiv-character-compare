# FFXIV Character compare
## Description
This tool allows to **search and select** characters, then it will compare them according the **jobs**, **mounts**, **minions** and **achievements**. It will print the result in console.

## Requirements
- Python >=3.14.
- [UV](https://docs.astral.sh/uv/).

## Python libraries used
- requests
- beautifulsoup4

## Installation
Install dependencies:
```bash
uv sync
```

## Usage
Execute the search and compare process:
```bash
uv run ffxiv-character-compare
```
**Optional** arguments:
- `-h --help`: Prints the help manual.
- `-r --refresh`: Force character and world cache refresh.