from datetime import datetime

from dotenv import find_dotenv, load_dotenv
from flask import Flask, abort, render_template

from azure_web_app import auth, db
from azure_web_app._constants import SECRET_ENV_FILE


FAVORITES = [
    {"id": 1, "title": "Offensive Memes", "why": "I like Offensive memes because they make people uncomfortable"},
    {"id": 2, "title": "Dank Memes", "why": "L33T, SNOOP DAWG, MOM GET TH CAMERA!"},
    {"id": 3, "title": "2007 MEMES", "why": "rawr xd, ALL YOUR BASE ARE BELONG TO USE,i CAN HAZ CHEEZBURGER, etc."},
]

MEME_ERAS = [
    {
        "name": "Early Internet",
        "years": "1990s-2000s",
        "year": 2007,
        "description": "All Your Base Are Belong to Us, dancing babies, and the first viral image macros.",
        "format": "Image macros",
    },
    {
        "name": "Rage Comics",
        "years": "2008-2012",
        "year": 2010,
        "description": "Forever Alone, Trollface, and comics that turned everyday frustrations into jokes.",
        "format": "Comic strips",
    },
    {
        "name": "Reaction Images",
        "years": "2012-2016",
        "year": 2014,
        "description": "A perfectly timed screenshot or GIF could say everything without a reply.",
        "format": "GIFs and screenshots",
    },
    {
        "name": "Short-Form Video",
        "years": "2017-today",
        "year": 2020,
        "description": "Remixes, sounds, and short videos that spread from one feed to the next.",
        "format": "Short videos",
    },
]


def create_app():
    load_dotenv(find_dotenv(SECRET_ENV_FILE))
    app = Flask(__name__)
    db.setup_for_app(app)
    auth.setup_auth(app)
    setup_routes(app)
    return app

def favorite_detail(favorite_id: int):
    for favorite in FAVORITES:
        if favorite["id"] == favorite_id:
            return render_template("favorites.html", favorite=favorite)
    abort(404)


def memes_page():
    return render_template("memes.html", meme_eras=MEME_ERAS)


def setup_routes(app):
    app.route("/")(index)
    app.route("/favorites/<int:favorite_id>")(favorite_detail)
    app.route("/memes")(memes_page)


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
