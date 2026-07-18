#!/usr/bin/env python3
"""
Cross-platform pi package installer.
Installs a standard set of pi packages from a hardcoded list.
"""
import subprocess
import sys
import shutil
import os
import shlex

PACKAGES = [
    "npm:pi-btw",
    "git:github.com/obra/superpowers",
    "npm:pi-setup-custom-providers",
    "npm:pi-mcp-adapter",
]


def find_pi_command():
    """Find the pi executable, checking various common locations.
    
    Returns a list of command parts suitable for subprocess.run().
    """
    # Check if 'pi' is directly available
    pi_path = shutil.which("pi")
    if pi_path:
        return [pi_path]
    
    # On Windows, try npm-based invocation
    if sys.platform == "win32":
        # Try npx first
        npx_path = shutil.which("npx")
        if npx_path:
            # Use 'npx pi' to run pi through npx
            return [npx_path, "pi"]
        
        # Fall back to npm exec
        npm_path = shutil.which("npm")
        if npm_path:
            return [npm_path, "exec", "--", "pi"]
    
    return None


def main():
    pi_cmd = find_pi_command()
    
    if pi_cmd is None:
        print("Error: 'pi' command not found in PATH.", file=sys.stderr)
        print("Please ensure pi is installed and in your PATH.", file=sys.stderr)
        print()
        print("On Windows, try: npm install -g @earendil-works/pi-cli", file=sys.stderr)
        print("On macOS/Linux, try: npm install -g @earendil-works/pi-cli", file=sys.stderr)
        sys.exit(1)
    
    print(f"Using pi command: {' '.join(pi_cmd)}")
    
    for pkg in PACKAGES:
        print(f"Installing {pkg}...")
        cmd = pi_cmd + ["install", pkg]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"Warning: Failed to install {pkg}", file=sys.stderr)


if __name__ == "__main__":
    main()