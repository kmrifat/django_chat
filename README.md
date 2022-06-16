# Django Chat App

![](https://github.com/kmrifat/django_chat/blob/master/django-chat-app.gif?raw=true)

A private messaging and calling application build using Django, Django Channel and Peer.js (WebRTC).
The front end has been build in Vue.js and I use Django Rest Framework for communicate with Backend and Frontend.  

PyWebsocket is been used inside Django Channel Wrapper for realtime communication. 
WebRTC is been used for Video and Audio calling.


# Architecture

![](https://github.com/kmrifat/django_chat/blob/master/chat_app.drawio.png?raw=true)

# Installation
```
git clone https://github.com/kmrifat/django_chat.git
```

### FrontEnd Installation
```
cd frontend
npm install
npm run dev
```

### Backend Installation
```
cd server
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver
```
Spacial Thanks to <img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg" width="50px" alt="JetBrains Logo (Main) logo."> For Awesome IDE support.
