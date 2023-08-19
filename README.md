# Deep-Learning Chatbot in TensorFlow. 


## Introduction

In this project, I build a chatbot that can carry out conversations with users using natural language processing that can generate human-like responses to given prompts. We will be integrating the chatbot with Flask, a popular Python web framework, to create a web application that can communicate with users via a chat interface.

For the frontend of our application, we will be using HTML, CSS, and JavaScript to create a visually appealing and interactive chat interface. Additionally, we will be using jQuery to handle the HTTP requests that are made to the backend server.

 
### Motivation

Build a chatbot to provide customer support, increased efficincy, enhanced customer expirence and cost reduction


### Objectives:

It helps in catering a huge amount of target audience at the same time 24/7 and once trained, you will be able to communicate with your target audience in their language, saving you from investing much on hiring different languages resources. The bot can entertain your customers anywhere in the world, while you are asleep


### Project Organization

To get started follow the steps below:

1. Install a virtual environment by runnning the following
```
virtualenv chatbotenv
source chatbotenv/bin/activate
```

2. Install all the required libraries 
```
pip install nltk
pip install numpy
pip install keras
pip install tensorflow
pip install flask
```

Run the chatbot.py file to create the model
```
python chatbot.py
```

Run the APP to create a Flask front end on port 8888 (or any port the app is pointing to)
```
python app.py
```

## Customize
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
