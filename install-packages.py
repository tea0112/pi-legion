#!/usr/bin/env python3
"""
Cross-platform pi package installer.
Installs a standard set of pi packages from a hardcoded list.
"""
import subprocess
import sys
import shutil
import os

PACKAGES = [
    "npm:pi-btw",
    "git:github.com/obra/superpowers",
    "npm:pi-setup-custom-providers",
    "npm:pi-mcp-adapter",
]


def find_pi_command():
    """Find the pi executable, checking various common locations."""
    # Check if 'pi' is directly available
    if shutil.which("pi"):
        return "pi"
    
    # On Windows, try npm-based invocation
    if sys.platform == "win32":
        if shutil.which("npx"):
            return "npx pi"
        if shutil.which("npm"):
            # npm should be able to run globally installed packages
            return "npm exec -- pi"
    
    return None


def main():
    pi_cmd = find_pi_command()
    
    if pi_cmd is None:
        print("Error: 'pi' command not found in PATH.", file=sys.stderr)
        print("Please ensure pi is installed and in your PATH.", file=sys.stderr)
        print("On Windows, try: npm install -g @earendil-works/pi-cli", file=sys.stderr)
        sys.exit(1)
    
    for pkg in PACKAGES:
        print(f"Installing {pkg}...")
        # Split pi_cmd if it contains spaces (e.g., "npx pi")
        cmd = pi_cmd.split() + ["install", pkg]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"Warning: Failed to install {pkg}", file=sys.stderr)


if __name__ == "__main__":
    main()