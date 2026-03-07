async function loadHello() {
    const res = await fetch("/api/hello");
    const data = await res.json();
    document.getElementById("apiResponse").innerText = data.message;
}

async function addTask() {
    const input = document.getElementById("taskInput");
    const task = input.value;

    const res = await fetch("/api/add-task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task })
    });

    const data = await res.json();
    input.value = "";
    displayTasks(data.tasks);
}

async function displayTasks(tasks) {
    const list = document.getElementById("taskList");
    list.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerText = task;
        list.appendChild(li);
    });
}

window.onload = async function () {
    const res = await fetch("/api/tasks");
    const data = await res.json();
    displayTasks(data.tasks);
};