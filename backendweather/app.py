from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule
from database import get_db_connection, setup_database

app = Flask(__name__)

# Set up the database when the app starts
setup_database()

@app.route('/api/rules', methods=['POST'])
def create_rule_api():
    data = request.json
    rule_string = data.get('rule_string')
    rule_name = data.get('name')

    if not rule_string or not rule_name:
        return jsonify({"error": "Missing rule string or name"}), 400

    try:
        create_rule(rule_string)
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO rules (name, rule_string) VALUES (%s, %s) RETURNING id",
                    (rule_name, rule_string)
                )
                rule_id = cur.fetchone()[0]

        return jsonify({"id": rule_id, "message": "Rule created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/evaluate', methods=['POST'])
def evaluate_rules_api():
    data = request.json
    user_data = data.get('user_data')
    rule_ids = data.get('rule_ids')

    if not user_data or not rule_ids:
        return jsonify({"error": "Missing user data or rule IDs"}), 400

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT rule_string FROM rules WHERE id = ANY(%s)",
                    (rule_ids,)
                )
                rules = cur.fetchall()

        if not rules:
            return jsonify({"error": "No rules found"}), 404

        rule_strings = [rule[0] for rule in rules]
        combined_ast = combine_rules(rule_strings)
        result = evaluate_rule(combined_ast, user_data)

        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
