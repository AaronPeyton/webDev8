from flask import Flask, render_template, request, Markup, flash
import os, json

with open('county_demographics.json') as demographics_data:
    counties = json.load(demographics_data)

app = Flask(__name__)
#__name__ = "__main__" if this is the file that was run.
#Otherwise, it is the name of the file (ex. webapp)

if __name__=="__main__":
    app.run(debug=False, port=54321)


@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    if 'State' in request.args:
        selected_state = request.args["State"]
        return render_template('index.html', response_options = get_state_options(counties), response_population = get_RS(counties, selected_state), response_state = selected_state)
    return render_template('index.html', response_options = get_state_options(counties))

def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def get_RS(counties, selected_state):
    RS = 0
    for c in counties:
        if c["State"] == selected_state:
            RS += c["Sales"]["Retail Sales"]
    return str(RS)
