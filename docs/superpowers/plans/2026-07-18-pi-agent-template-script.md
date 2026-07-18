# Pi Agent Template & Script Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a simple Python script that installs a standard set of pi packages from a hardcoded list.

**Architecture:** Single Python script with a static `PACKAGES` list, loops through each and runs `pi install <pkg>` via subprocess.

**Tech Stack:** Python 3, subprocess module

---

### Task 1: Create install-packages.py script

**Files:**
- Create: `scripts/install-packages.py`

**Interfaces:**
- Produces: `scripts/install-packages.py` executable script

- [ ] **Step 1: Create scripts directory**

```bash
mkdir -p scripts
```

- [ ] **Step 2: Create the Python script**

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

- [ ] **Step 3: Make executable**

```bash
chmod +x scripts/install-packages.py
```

- [ ] **Step 4: Verify syntax**

```bash
python3 -m py_compile scripts/install-packages.py
```

- [ ] **Step 5: Commit**

```bash
git add scripts/install-packages.py
git commit -m "feat: add pi-agent-install script"
```

---

**Plan complete.** Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent for the task, review before/after

**2. Inline Execution** — Execute directly in this session

Which approach?