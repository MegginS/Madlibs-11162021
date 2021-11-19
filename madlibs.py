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
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


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
    # game_interest = request.args.get("game_interest")

    # if game_interest == "on":
    #     return render_template("game_form.html")
    # else:
    #     return render_template("goodbye.html")

@app.route("/game_play", methods=["POST"])
def show_madlib_result():

    color = request.form.get("color")

    noun = request.form.get("noun")

    person_madlib = request.form.get("person_madlib")

    adjective = request.form.get("adjective")

    animal = request.form.get("animal")

    shape = request.form.get("shape")

    sound = request.form.get("sound")

    place = request.form.get("place")
    
    return render_template(choice(['game.html', 'game1.html']), color=color, noun=noun, person_madlib=person_madlib, adjective=adjective, animal=animal, shape=shape, sound=sound, place=place)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
