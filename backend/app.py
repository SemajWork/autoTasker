from flask import Flask, request, jsonify
from flask_cors import CORS
from handleInstruction import exceute_instructions as execute_instructions
from aiInterpreter import aiInterpreter

app = Flask(__name__)
cors_origins = ["http://localhost:5173/"]

CORS(app,origins=cors_origins)

@app.route('/api/sendInstruction',method=['POST'])
def send_instruction():
    try:
        data = request.get_json()
        instructions = aiInterpreter(data.get('instruction'))
        execute_instructions(instructions)

        return jsonify
    except Exception as e:
        return jsonify({"error":str(e)}),401
