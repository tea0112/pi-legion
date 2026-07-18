# Pi Agent Template & Script — Spec

## Overview

A minimal Python script that installs a standard set of pi packages from a hardcoded list.

## Script

**Location:** `scripts/install-packages.py`

```python
#!/usr/bin/env python3
import subprocess

PACKAGES = [
    "npm:pi-btw",
    "git:github.com/obra/superpowers",
    "npm:pi-setup-custom-providers",
    "npm:pi-mcp-adapter",
]

def main():
    for pkg in PACKAGES:
        print(f"Installing {pkg}...")
        subprocess.run(["pi", "install", pkg])

if __name__ == "__main__":
    main()
```

## Behavior

- Iterates over `PACKAGES` list
- Runs `pi install <package>` for each entry
- Prints progress to stdout

## Maintenance

Edit `PACKAGES` directly in the script to add/remove/update packages.

## Files

- `scripts/install-packages.py` — executable Python script