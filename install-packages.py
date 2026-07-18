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