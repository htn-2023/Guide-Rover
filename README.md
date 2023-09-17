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

5. RoboMaster set-up

```
Go to https://github.com/dji-sdk/robomaster-sdk
Download the repo and run the executable file named “VisualCppRedist_AIO_20200707.exe”.

Important! Please keep the executable running in the background while using the RoboMaster.

Go to the (physical) RoboMaster. Turn on the robot by pressing and holding the power button. 
Once the RoboMaster is online, ensure the connection method is in “direct connection mode”. 
Lastly, connect to the Robot through WiFi connection. 

The Wifi name is: “RMEP-21abe4” and the password is “12341234”
```

6. Run the server

```
flask run
```

# Usage

The folder `vision` is the main folder for the computer vision model (YOLO). The folder `communication` is the main folder for the connection between wisper voice model and gpt.
