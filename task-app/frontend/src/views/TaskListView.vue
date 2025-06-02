<template>
  <div>
    <div v-if="loading" class="text-center text-gray-500">Загрузка задач...</div>
    <div v-else>
      <TaskItem
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @delete="onDelete"
        @toggle="onToggle"
      />
      <div v-if="tasks.length === 0" class="text-center text-gray-500">
        Нет задач. Добавь первую!
      </div>
    </div>

    <!-- Форма добавления задачи снизу -->
    <TaskCreateView @created="onCreated" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import TaskItem from "@/components/TaskItem.vue";
import TaskCreateView from "@/views/TaskCreateView.vue";
import type { Task } from "@/api";
import { fetchTasks, deleteTask } from "@/api";

const tasks = ref<Task[]>([]);
const loading = ref<boolean>(true);

async function loadTasks() {
  try {
    loading.value = true;
    tasks.value = await fetchTasks();
  } catch (e) {
    console.error("Ошибка при загрузке задач:", e);
  } finally {
    loading.value = false;
  }
}

async function onDelete(id: number) {
  try {
    await deleteTask(id);
    await loadTasks();
  } catch (e) {
    console.error("Ошибка при удалении задачи:", e);
  }
}

async function onToggle(updated: Task) {
  // Здесь можно добавить updateTask, если потребуется. Пока просто перезагружаем
  await loadTasks();
}

function onCreated(newTask: Task) {
  // Просто добавляем в массив, чтобы не перезагружать всё
  tasks.value.push(newTask);
}

onMounted(loadTasks);
</script>
