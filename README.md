<div align="center">
 <h1>Stock Market Alert</h1>
</div>
<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">A simple script built using Python and Beautiful Soup that scrapes a website for the level of Sensex Stock Exchange, tracks it and sends a notification on your phone via IFTTT webhooks
  and if you plan on being annoying then can play You Suffer by Napalm Death as a Desktop alert .</h3>

  <p align="center">
    <br />
    <a href="https://beautiful-soup-4.readthedocs.io/en/latest/"><strong>Explore the Beautiful Soup docs »</strong></a>
    <br/>
  </p>
</div>

---

**Source Code**: <a href="https://github.com/erabhisheksingh/stock-market-alert" target="_blank">https://github.com/erabhisheksingh/stock-market-alert</a>

---

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. The script also uses Requests module for fetching the webpage and posting an alert to IFTTT Webhook.  

The key features are:

* **Scrapes Continuously**: The script tries to fetch the updated market level every 5 mins.
* **Choice of Level to Track**: The user is given a choice to set the market level to track and laert  
* **Mobile Notifications**: The user gets a Notification on Mobile device
* **System Alert Sound**: The script plays an Alert sound on the system it's running.

---

## 🔧 Technologies & Tools
</br>
<p  align='left'>
<a href="https://github.com/erabhisheksingh/"><img src="https://img.shields.io/badge/-Python-white?logo=python&logoColor=blue&style=flat-square" alt="Python Badge"/></a>&nbsp;&nbsp;

---
## **Requirements**

this script requires Python 3.6+


## Installation

```console
$ python -m venv venv

---> 100%
```

You will need to activate the Virtual environment using the below command

```console
$ source venv/bin/activate 

---> 100%
```

Then install the packages from the requirements.txt

```console
$ pip install -r requirements.txt

---> 100%
```

Then run the script

```console
$ python main.py

```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the MIT license.