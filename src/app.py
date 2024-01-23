from flask import Flask, jsonify, request
app = Flask(__name__)

# new_todo = []

todos = [
    { "label": "Hacer tarea", "done": False },
    { "label": "Lavar platos", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_json = jsonify(todos)
    return todos_json


@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = request.get_json()
    todos.append(body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # body_delete = position
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)