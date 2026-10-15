from datetime import datetime
from flask import Flask, abort, render_template
from flask import Flask, render_template

FAVORITES = [
    {"id": 1, "title": "Offensive Memes", "why": "I like Offensive memes because they make people uncomfortable"},
    {"id": 2, "title": "Dank Memes", "why": "L33T, SNOOP DAWG, MOM GET TH CAMERA!"},
    {"id": 3, "title": "2007 MEMES", "why": "rawr xd, ALL YOUR BASE ARE BELONG TO USE,i CAN HAZ CHEEZBURGER, etc."},
]


def create_app():
    app = Flask(__name__)
    setup_routes(app)
    return app

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorites.html", favorite=favorite)
    abort(404)


def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)

def index():
    return render_template(
        "index.html",
        name="Daniel Gonzalez",
        hobby="Posting Memes",
        hours_per_week=100,
        hour=datetime.now().hour,
        show_counter=False,
        favorites=FAVORITES,
        fun_fact="I spend more time on memes than most people spend on homework.",
    )


def run_app(debug: bool = True) -> None:
    app = create_app()
    app.run(debug=debug)


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
