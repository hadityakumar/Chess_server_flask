from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/random_move', methods=['POST'])
def random_move():
    fen = request.json['fen']
    result = subprocess.run(['python', 'chess_random_engine.py', fen], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return "Error processing move", 500
    return jsonify({'bestMove': result.stdout.decode('utf-8').strip()})

@app.route('/stockfish_move', methods=['POST'])
def stockfish_move():
    fen = request.json['fen']
    result = subprocess.run(['python', 'stockfish_engine.py', fen], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return "Error processing move", 500
    return jsonify({'bestMove': result.stdout.decode('utf-8').strip()})

@app.route('/ml_move', methods=['POST'])
def ml_move():
    fen = request.json['fen']
    result = subprocess.run(['python', 'ml_model.py', fen], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return "Error processing move", 500
    return jsonify({'bestMove': result.stdout.decode('utf-8').strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
