# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World! how are you? Are you fine. do u play roblox ???</p>"

if __name__=='__main__':
    app.run()
