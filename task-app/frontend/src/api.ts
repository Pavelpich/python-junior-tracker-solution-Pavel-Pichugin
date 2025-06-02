export interface Task {
  id?: number;
  title: string;
  completed: boolean;
}

const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api/tasks";

export async function fetchTasks(): Promise<Task[]> {
  const res = await fetch(`${BASE_URL}`);
  if (!res.ok) throw new Error(`Failed to fetch tasks: ${res.status}`);
  return (await res.json()) as Task[];
}

export async function createTask(task: Task): Promise<Task> {
  const res = await fetch(`${BASE_URL}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task),
  });
  if (!res.ok) throw new Error(`Failed to create task: ${res.status}`);
  return (await res.json()) as Task;
}

export async function deleteTask(id: number): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, {
    method: "DELETE",
  });
  if (![200, 204].includes(res.status)) throw new Error(`Failed to delete task: ${res.status}`);
}
