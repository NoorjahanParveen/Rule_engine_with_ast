from flask import Blueprint, render_template, request, jsonify
from rule_engine import RuleEngine  # Import your rule engine logic
from models import db_session, Rule  # Import your database model
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    return "Welcome to the Rule Engine!"  # Simple response or render a template

@main.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        data = request.json
        rule_string = data.get('rule')
        
        if not rule_string:
            return jsonify({"error": "Rule string is required"}), 400
        
        ast = RuleEngine.create_ast(rule_string)
        new_rule = Rule(rule=rule_string, ast=ast.to_json())
        db_session.add(new_rule)
        db_session.commit()
        return jsonify(ast.to_json()), 201  # HTTP 201 Created
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # HTTP 500 Internal Server Error

@main.route('/combine_rules', methods=['POST'])
def combine_rules():
    try:
        data = request.json
        rules = data.get('rules')
        
        if not rules or not isinstance(rules, list):
            return jsonify({"error": "A list of rules is required"}), 400
        
        combined_ast = RuleEngine.combine_asts(rules)
        return jsonify(combined_ast.to_json()), 200  # HTTP 200 OK
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # HTTP 500 Internal Server Error

@main.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    try:
        data = request.json
        user_data = json.loads(data.get('userData', '{}'))  # Default to empty JSON if not provided
        rule_string = data.get('rule')
        
        if not rule_string:
            return jsonify({"error": "Rule string is required"}), 400
        
        is_eligible = RuleEngine.evaluate_rule(user_data, rule_string)
        return jsonify({"isEligible": is_eligible}), 200  # HTTP 200 OK
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid user data format"}), 400  # HTTP 400 Bad Request
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # HTTP 500 Internal Server Error
