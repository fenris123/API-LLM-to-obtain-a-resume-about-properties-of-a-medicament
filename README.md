# API-LLM-to-obtain-a-resume-about-properties-of-a-medicament


# INTRODUCTION

On this project, we are going to use the API of the Spanish agency for medicines (AEMPS) to obtain a JSON with information about a medicine.
After that, we will pass the information to a local LLM to make a summary of the main specs of the selected medicine, and we will launch an audio reading that summary.

This project is somehow similar to a previous one: https://github.com/fenris123/API-LLM-gTTS-homemade-alexa — but in that one we use a different API to obtain information about the weather.
In addition, we use different libraries for the audio in this project: the reading is better and less "robotic".


## WARNING

DO NOT USE THIS AS A TOOL FOR MEDICAL INFORMATION.

THIS IS MAINLY A PERSONAL PROYECT, MADE JUST FOR FUN, EXPERIMENTATION AND LEARNING.

I think that it works very well but i can't promise that it makes no mistakes.




# FILES

Main file is "archivo_completo". This file contains the full script and can be used alone. It's the only thing that you need if you want to try this script.
In the mentioned project (https://github.com/fenris123/API-LLM-gTTS-homemade-alexa-) we included 3 different files with the different "parts" of the script alone.
If you want to modify or adapt something, you should consider taking a look at that project.


# LIBRARIES

json

requests

re

pyttsx3

gpt4all

sys

# LLM

To keep things simple, we have used the LLM installed by default by gpt4all: mistral-7b-openorca.Q4_0.gguf
It will be downloaded automatically the first time that you use the code.
BE CAREFUL: IT WILL NEED 4 GIGABYTES OF FREE SPACE. THIS IS WHAT HAPPENS ON 21/04/2025.
If you are reading this after that day, I hope they have not changed it.

On my PC, with an Intel 11400, 16GB of RAM and an RTX 6600, the LLM is a little bit slow — about 1 minute to answer.
I have tried faster LLMs like LLAMA, but the quality of the answers for this specific task is really bad.


# SOUND

We use the pyttsx3 library to "read" the resume. It sounds more natural and less robotic than gTTS (at least in Spanish).
It's certainly a little bit more complex than gTTS, but I think the difference is worth it.

