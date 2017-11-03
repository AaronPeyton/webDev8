from flask import Flask, url_for, render_template, request
import os, json

app = Flask(__name__)
#__name__ = "__main__" if this is the file that was run.
#Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    o = "blah, do sumthing w/ this make sure to include the stuff"
    ff = "fun funFact"
    return render_template('index.html', options = o, funFact = ff)

def get_state_options():
    options = ""

    return options

if __name__=="__main__":
    app.run(debug=False, port=54321)
