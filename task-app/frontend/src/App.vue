<template>
  <div class="min-h-screen bg-gray-100">
    <div class="container mx-auto py-8">
      <h1 class="text-3xl font-bold text-center mb-6">Task App</h1>
      <TaskListView />
    </div>
  </div>
</template>

<script setup lang="ts">
import TaskListView from "./views/TaskListView.vue";
</script>
