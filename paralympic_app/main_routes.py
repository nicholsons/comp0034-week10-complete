from flask import render_template, Blueprint
from paralympic_app.utilities import get_event, get_events

# Define the Blueprint
main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Returns the home page"""
    response = get_events()
    return render_template("index.html", event_list=response)


@main_bp.route("/display_event/<event_id>")
def display_event(event_id):
    """Returns the event detail page"""
    ev = get_event(event_id)
    return render_template("event.html", event=ev)
