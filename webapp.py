from flask import Flask, url_for, render_template, request
import os, json

app = Flask(__name__)
#__name__ = "__main__" if this is the file that was run.
#Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    o = get_state_options()
    ff = get_fun_fact()
    return render_template('index.html', options = o, funFact = ff)

def get_state_options():
    options = ""
    s = "cars"
    options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options

def get_fun_fact():
    ff = "random fun funFact"
    return ff

if __name__=="__main__":
    app.run(debug=False, port=54321)
