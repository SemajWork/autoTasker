from flask import Flask, request, jsonify
from flask_cors import CORS
from handleInstruction import execute_instructions
from aiInterpreter import interpret_instruction
import os

app = Flask(__name__)
Frontend_Domain = os.getenv("MYDOMAIN") or " "

cors_origins = ["http://localhost:5173"]

if len(Frontend_Domain) > 0:
    cors_origins.append(Frontend_Domain)

CORS(app, origins=cors_origins)

@app.route('/api/sendInstruction', methods=['POST'])
def send_instruction():
    try:
        data = request.json
        search_type = data.get('send_type')
        result = execute_instructions(search_type)
        return jsonify({"success": True, "result": result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
