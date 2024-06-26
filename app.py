from flask import Flask, render_template, request, redirect, url_for, flash, jsonify # type: ignore
import json
import pandas as pd
import random
import string
import secrets
from datetime import datetime
import requests
import mysql.connector

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para el uso de flash messages


@app.route('/')
def hello_world():
    return 'conexión con bbdd!'

if __name__ == '__main__':
    app.run()
