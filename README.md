# English Speaking Teacher Bot

Python RESTful API with FastAPI that analyzes audio input for speech improvements in the English language.

### Version
1.0.0

## Table of Contents

- [Technologies Used](#technologies-used)
- [Documentation](#documentation)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributors](#contributors)

## Introduction

Python 3-based bot english-speaking teacher to assist users in training and improving their English language skills. 

## Technologies Used

- [Python 3](https://docs.python.org/3/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI Speech to text](https://platform.openai.com/docs/guides/speech-to-text)
- [Elevenlabs API](https://elevenlabs.io/docs/introduction)

## Documentation

The documentation for this project can be found [here](https://github.com/bemebox/chatgpt-bot-english-speaking-teacher-backend/documentation).

[Speech Improvement API](http://127.0.0.1:8000/docs)

## Getting Started

These instructions will guide you to copy the project from the repository and run it.

### Prerequisites

Make sure you have the following installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bemebox/chatgpt-bot-english-speaking-teacher-backend.git
    cd chatgpt-bot-english-speaking-teacher-backend
    ```
2. Create a new virtual environment:
    ```bash
    python -m venv speechenv
    source speechenv/bin/activate
    ```

3. Install dependencies:

    To use environment variables:
    ```bash
    pip install python-dotenv  
    ```

    To install OpenAI:
    ```bash
    pip install fastapi
    pip install "uvicorn[standard]"
    pip install openai    
    ```

4. Start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```


## Usage

To run the English Speaking Teacher Bot, use the following command:

```bash
    uvicorn main:app --reload
```



## Contributors

* **BEOM &copy; 2024**