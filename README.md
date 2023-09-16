# Guide-Rover

Guiding Rover: An AI-Powered Mobility Solution for the Visually Impaired. Hack the North 2023 Project

# Installation

1. Clone the repository

```
git clone git@github.com:htn-2023/Guide-Rover.git
cd Guide-Rover
```

2. Create virtual environment

```
virtualenv venv
source venv/bin/activate
```

3. Install dependencies and set configs

```
bash setup.sh
```

4. Enter your OpenAI/Cohere API key in `.env`

```
# .env
OPEN_AI_API = '...'
COHERE_API = '...'
```

5. Run the server

```
flask run
```

# Usage

The folder `vision` is the main folder for the computer vision model (YOLO). The folder `communication` is the main folder for the connection between wisper voice model and gpt.
