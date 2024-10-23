# app.py

from flask import Flask, request, jsonify
from ast_engine import create_rule, combine_rules, evaluate_rule
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('rules.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for creating a rule
@app.route('/api/create_rule', methods=['POST'])
def api_create_rule():
    rule_string = request.json.get('rule_string')
    ast = create_rule(rule_string)

    conn = get_db_connection()
    conn.execute('INSERT INTO rules (rule, ast_repr) VALUES (?, ?)', (rule_string, repr(ast)))
    conn.commit()
    conn.close()

    return jsonify({"ast": repr(ast)})

# Route for combining rules
@app.route('/api/combine_rules', methods=['POST'])
def api_combine_rules():
    rules = request.json.get('rules')
    combined_ast = combine_rules(rules)

    return jsonify({"combined_ast": repr(combined_ast)})

# Route for evaluating a rule
@app.route('/api/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    ast_repr = request.json.get('ast')
    user_data = request.json.get('user_data')

    combined_ast = eval(ast_repr)  # For simplicity (unsafe for production)
    result = evaluate_rule(combined_ast, user_data)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
