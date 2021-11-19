"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("gotohello.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)
    # return render_template("compliment.html", person=player, compliment=compliment)

    game_interest = request.args.get("game_interest")

    if game_interest == "on":
        return render_template("game_form.html")
    else:
        return render_template("goodbye.html", person=player, compliment=compliment)

@app.route("/game")
def  show_madlib_form():
    """asks if wants to play game"""

    return render_template("game_form.html")

@app.route("/game_play")
def show_madlib_result():

    color = request.args.get("color")

    noun = request.args.get("noun")

    person_madlib = request.args.get("person_madlib")

    adjective = request.args.get("adjective")

    animal = request.args.get("animal")

    shape = request.args.get("shape")

    sound = request.args.get("sound")

    place = request.args.get("place")
    
    return render_template(choice(['game.html', 'game1.html', 'game2.html']), color=color, noun=noun, person_madlib=person_madlib, adjective=adjective, animal=animal, shape=shape, sound=sound, place=place)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
