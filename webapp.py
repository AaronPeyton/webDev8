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
    o = get_state_options()
    ff = get_fun_fact()
    return render_template('index.html', options = o, funFact = ff)

def get_state_options():
    states = get_states(counties)
    for s in states:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options

def get_fun_fact(state):
    ff = "random fun funFact"
    return ff

def get_states(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    #Find the state in the dictionary with the most counties
    #Return the state with the most counties
    states = {}

    ## dictionarying states and counties
    for c in counties:
        # print c["State"], c["County"]
        state = str(c["State"])
        county = str(c["County"])

        if state in states:
            states[state].append(county)
        else:
            states[state] = [county]
        return states.sort()
