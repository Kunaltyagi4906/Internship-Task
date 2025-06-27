from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}
@app.route('/')
def home():
    return "Welcome to Task 4 - Flask REST API 🎉"

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify({username: user}), 200
    return jsonify({"error": "User not found"}), 404

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = data
    return jsonify({"message": "User created", "user": data}), 201


@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[username].update(data)
    return jsonify({"message": "User updated", "user": users[username]}), 200

# Route to delete a user
@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    del users[username]
    return jsonify({"message": f"User {username} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
