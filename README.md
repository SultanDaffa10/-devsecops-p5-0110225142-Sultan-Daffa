
# SecureTask Manager

SecureTask Manager is a simple command-line application for
managing personal tasks. Users can add tasks, view their task
list, and mark tasks as completed.

## Technology Stack

- Python 3.12
- pytest for unit testing
- Bandit for Static Application Security Testing (SAST)
- GitHub Actions for CI automation

## Features

- Add tasks with titles and descriptions
- Display all tasks and their status
- Mark tasks as completed
- Validate task titles and task indexes

## Requirements

- Python 3.12 or compatible Python 3 version
- pip

## How to Run

Clone the repository and enter its directory:

```bash
git clone https://github.com/YOUR-USERNAME/devsecops-p5-0110225142.git
cd devsecops-p5-0110225142
```

Create a virtual environment and install development dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python -m app.main
```

## Running Unit Tests

```bash
python -m pytest -v
```

## Running SAST

```bash
bandit -r app
```

## CI/CD Pipeline Overview

The GitHub Actions workflow is defined in
`.github/workflows/devsecops.yml`.

The pipeline is triggered by pushes to the `main` branch and
pull requests targeting `main`.

It contains two jobs:

1. **Build and Unit Test:** Installs dependencies and runs pytest.
2. **SAST Scan and Quality Gate:** Runs Bandit after the build
   succeeds and checks whether HIGH-severity, HIGH-confidence
   findings exist.

The security report is uploaded as a GitHub Actions artifact.

The Quality Gate fails when the configured security threshold
is exceeded or when the scan report cannot be validated.
