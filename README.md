# XMeme-REST-API : API for XMEME APP

This app was a part of the Crio Externship program. I have Django-Rest-Framework to build the REST API 


<img src="screenshots/Meme Api – Django REST framework 28-02-2021 19-45-27.png" align="center" width="1080" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 


#### 💻 Xmeme-api handles the requests made from the xmeme-frontend application.📰🔥 This repository contains the REST APIs of Xmeme application.✨


Deployed Backend app link : [XmemeBackend App](https://xmemebackendapp.herokuapp.com/memes/)

Checkout the frontend app also : [XmemeFrontend App](https://github.com/sukanta-nandi/XMEME-Frontend)

---

# Instructions to run xmeme-backend locally :

1. Clone the repo

```
git clone https://github.com/sukanta-nandi/XMEME-Backend.git
```

2. Install python3 and vitualenv. cd into the cloned folder and create a virtual env. Activate your virtual env

```
pip3 install virtualenv
python3 -m venv <name of your venv>

# for linux
source <name of your venv>/bin/activate

#for windows
source <name of your venv>/scripts/activate
```

3. Install the requirements using requirements.txt for both backend and frontend

```
pip install -r XMEME-Backend/requirements.txt

```

4. Run the backend
Note : make sure run backend and front end on different port when running locally.

For first time run
```
cd XMEME-Backend
python manage.py makemigrations
python manage.py migrate
```
