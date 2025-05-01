from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    expression = data.get('expression')
    try:
        # Safely evaluate the math expression
        result = eval(expression, {"__builtins__": None}, {})
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': 'Invalid Expression'}), 400

if __name__ == '__main__':
    app.run(debug=True)
