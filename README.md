FastAPI Starter
## Installation
In the root directory of the project, run the following commands to install the dependencies and run the server:
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment
uv venv
source venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt

# Run the server
python main.py
```
## Stack
- FastAPI
- Uvicorn (Cython)
- Ruff
- Pytest