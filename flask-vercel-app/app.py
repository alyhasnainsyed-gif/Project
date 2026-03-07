from flask import Flask, render_template, request, jsonify

# Flask will look for "static" and "templates" directories next to this file by default,
# but we can be explicit so the behavior remains correct after reorganizing.
app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates",
)

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

# Vercel's Python builder expects a variable named `app` at the module level.
# The line below is redundant now that we haven't reassigned `app`, but it's harmless and
# left here for clarity if the code is refactored later.
app = app