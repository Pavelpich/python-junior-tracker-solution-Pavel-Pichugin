const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api/tasks";
export async function fetchTasks() {
    const res = await fetch(`${BASE_URL}`);
    if (!res.ok)
        throw new Error(`Failed to fetch tasks: ${res.status}`);
    return (await res.json());
}
export async function createTask(task) {
    const res = await fetch(`${BASE_URL}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task),
    });
    if (!res.ok)
        throw new Error(`Failed to create task: ${res.status}`);
    return (await res.json());
}
export async function deleteTask(id) {
    const res = await fetch(`${BASE_URL}/${id}`, {
        method: "DELETE",
    });
    if (![200, 204].includes(res.status))
        throw new Error(`Failed to delete task: ${res.status}`);
}
//# sourceMappingURL=api.js.map
