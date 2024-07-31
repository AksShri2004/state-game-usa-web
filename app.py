from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("50_states.csv")
states = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    request_data = request.get_json()
    user_state = request_data.get('state', '').title()

    if user_state == "Exit":
        miss_states = [state for state in data['state'] if state not in states]
        return jsonify({"missed": miss_states, "score": len(states)})

    if user_state in data['state'].values and user_state not in states:
        current_state = data[data.state == user_state].iloc[0]
        states.append(user_state)
        return jsonify({
            "correct": True,
            "state": user_state,
            "x": int(current_state['x']),
            "y": int(current_state['y']),
            "score": len(states)
        })
    return jsonify({"correct": False})


if __name__ == '__main__':
    app.run(debug=True)
