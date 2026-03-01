from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask API 👋"})

@app.route("/api/add-task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    if task:
        tasks.append(task)
        return jsonify({"status": "success", "tasks": tasks})
    return jsonify({"status": "error"}), 400

@app.route("/api/tasks")
def get_tasks():
    return jsonify({"tasks": tasks})