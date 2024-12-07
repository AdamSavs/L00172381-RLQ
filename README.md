# L00172381-RLQ


Regional Lore Quest: Quests that involve gathering stories from villagers about local history, unlocking unique items or rewards related to the lore.

## Development Environment Setup

```bash
# Create the virtualenv
python3 -m venv .venv
# Install dependencies
source .venv/bin/activate
pip install -U pip setuptools
pip install -e .[dev]
# Run the program
python3 -m lorequest
# Build a package (.whl)
python3 -m build

```

## Installation

Requires python 3.10 or newer.

```bash
pip install dist/lorequest-*.whl
lorequest --help
```
