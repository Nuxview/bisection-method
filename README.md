# Bisection Method Implementation

This repository contains a Python implementation of the Bisection Method, developed as part of a numerical analysis coursework.

## Project Structure

- `main.py`: The core script containing the implementation of the bisection algorithm and visualization logic.
- `pyproject.toml` & `uv.lock`: Configuration and dependency management files using `uv`.

## Setup Process

This project uses `uv` for dependency management. To set up and run the script:

1. **Ensure `uv` is installed**: If you don't have it, follow the instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).
2. **Sync Dependencies**: Navigate to the repository directory and sync the environment:
   ```bash
   uv sync
   ```
3. **Run the Script**: Execute the main Python file:
   ```bash
   uv run main.py
   ```

The script will compute the root and display a plot of the function using `matplotlib`.
