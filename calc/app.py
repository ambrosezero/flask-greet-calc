from flask import Flask, request
from operations import add, sub, mult, div
# Put your app in here.

@app.route("/add")
def app_add(a,b):
    my_args = request.args
    a = my_args[a]
    b = my_args[b]
    add(a,b)

@app.route("/sub")
def app_sub(a,b):
    my_args = request.args
    a = my_args[a]
    b = my_args[b]
    sub(a,b)

@app.route("/mult")
def app_mult(a,b):
    my_args = request.args
    a = my_args[a]
    b = my_args[b]
    mult(a,b)

@app.route("/div")
def app_div(a,b):
    my_args = request.args
    a = my_args[a]
    b = my_args[b]
    div(a,b)