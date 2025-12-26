# © 2025 Douglas "Dum2601" Barbosa
# MIT License

from pathlib import Path
import json

# Shows which is the current directory
def current_dir() -> str:
    return str(Path.cwd())

# List the files and packages from chosen path and return JSON-compatible data
def list_items_dir(dir: str) -> list[dict]:
    path = Path(dir)
    items = []

    for item in path.iterdir():
        if item.is_file():
            items.append({
                "type": "file",
                "name": item.stem,
                "extension": item.suffix
            })
        elif item.is_dir():
            items.append({
                "type": "directory",
                "name": item.name
            })

    return items


# Example: show packages and extensions of the current directory as JSON
data = list_items_dir(current_dir())
json_output = json.dumps(data, indent=4)

print(json_output)
