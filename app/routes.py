from flask import Blueprint, render_template, request, jsonify
from .chatbot import get_support_response
from .ticketing import create_ticket
from .knowledge_base import fetch_solution

support_routes = Blueprint('support', __name__)


@support_routes.route('/')
def index():
    return render_template('index.html')

@support_routes.route('/ask', methods=['POST'])
def ask():
    user_query = request.form.get('query')
    support_response = get_support_response(user_query)
    if support_response == "need_ticket":
        ticket = create_ticket(user_query)
        return jsonify({"ticket_id": ticket.id, "response": "Your issue has been logged. A support agent will contact you."})
    return jsonify({"response": support_response})

@support_routes.route('/kb', methods=['GET'])
def knowledge_base():
    query = request.args.get('query')
    solution = fetch_solution(query)
    return jsonify({"solution": solution})
