import requests 
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
from scraper_correios import tracking_info

from twilio import twilio_msg


app = Flask("Correio")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/enviado')
def enviado():

    cod = request.args.get('code')
    to_phone = request.args.get('cellphone')
    body = tracking_info(cod)
    twilio_msg(to_phone, body)

    return render_template("send.html")


app.run(host="0.0.0.0")