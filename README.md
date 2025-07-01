# RAG

this is just prototype for RAG which I will continue use it Ansallah for my graduation project for uni.

## Requirments

- This project was built using python 3.8. It's up to you if you wanna use python 3.8 or later.

#### How you can install python using miniconda

 - Download and install MiniConda form here [https://www.anaconda.com/docs/getting-started/miniconda/main]


#### once you have already donwload conda you will be in base zone. so you need to create enviroment follow these commands:

1) Open VS code then Open terminal from view menu.

2) it will pop up type this command: ``` conda create -n mini-app-rag python-3.8 -y ```

3) now you need to activate your enviorment use this command: ```conda activate mini-rag-app```

### (Optinal) setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the req from requirements.txt
#### using this command: ```pip install -r requirements.txt```


### Set the environment variables

#### for bignners I can upload my .env for you cuz it has secret keys for API or something that secret. so you need to copy my .env.example and fill it with your API keys and use it for you as .env

#### using this command: ```cp .env.example .env```

## Run FastAPI server

### Use this command line: ```uvicorn main:app --reload --host 0.0.0.0 --port 5555```. (About the port you can use wherever you like)

## POSTMAN Collection

### Download the postman collection from this path: ```\assets\mini-rag-app.postman_collection.json```
