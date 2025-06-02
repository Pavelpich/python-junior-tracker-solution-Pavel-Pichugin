<template>
  <div
    class="flex items-center justify-between bg-white p-4 rounded shadow mb-2 hover:bg-gray-50"
  >
    <div class="flex items-center gap-2">
      <input
        type="checkbox"
        :checked="task.completed"
        @change="onToggle"
        class="h-5 w-5 text-blue-600 border-gray-300 rounded"
      />
      <span :class="{ 'line-through text-gray-400': task.completed }">
        {{ task.title }}
      </span>
    </div>
    <button @click="onDelete" class="text-red-500 hover:text-red-700">
      Удалить
    </button>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import type { Task } from "@/api";

const props = defineProps<{ task: Task }>();
const emit = defineEmits<{
  (e: "delete", id: number): void;
  (e: "toggle", task: Task): void;
}>();

function onDelete() {
  if (props.task.id !== undefined) {
    emit("delete", props.task.id);
  }
}

function onToggle() {
  if (props.task.id !== undefined) {
    emit("toggle", { ...props.task, completed: !props.task.completed });
  }
}
</script>
