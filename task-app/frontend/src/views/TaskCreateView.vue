<template>
  <div class="mt-6 flex gap-2">
    <input
      v-model="title"
      type="text"
      placeholder="Новая задача"
      class="flex-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
      @keyup.enter="onSubmit"
    />
    <button
      @click="onSubmit"
      class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
    >
      Добавить
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type { Task } from "@/api";
import { createTask } from "@/api";

const title = ref<string>("");
const emit = defineEmits<{
  (e: "created", task: Task): void;
}>();

async function onSubmit() {
  if (!title.value.trim()) return;
  try {
    const newTask = await createTask({ title: title.value, completed: false });
    emit("created", newTask);
    title.value = "";
  } catch (e) {
    console.error("Ошибка при создании задачи:", e);
  }
}
</script>
