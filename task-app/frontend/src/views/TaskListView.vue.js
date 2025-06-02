import { ref, onMounted } from "vue";
import TaskItem from "@/components/TaskItem.vue";
import TaskCreateView from "@/views/TaskCreateView.vue";
import { fetchTasks, deleteTask } from "@/api";
const tasks = ref([]);
const loading = ref(true);
async function loadTasks() {
    try {
        loading.value = true;
        tasks.value = await fetchTasks();
    }
    catch (e) {
        console.error("Ошибка при загрузке задач:", e);
    }
    finally {
        loading.value = false;
    }
}
async function onDelete(id) {
    try {
        await deleteTask(id);
        await loadTasks();
    }
    catch (e) {
        console.error("Ошибка при удалении задачи:", e);
    }
}
async function onToggle(updated) {
    // Здесь можно добавить updateTask, если потребуется. Пока просто перезагружаем
    await loadTasks();
}
function onCreated(newTask) {
    // Просто добавляем в массив, чтобы не перезагружать всё
    tasks.value.push(newTask);
}
onMounted(loadTasks);
debugger; /* PartiallyEnd: #3632/scriptSetup.vue */
const __VLS_ctx = {};
let __VLS_components;
let __VLS_directives;
__VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
if (__VLS_ctx.loading) {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
        ...{ class: "text-center text-gray-500" },
    });
}
else {
    __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({});
    for (const [task] of __VLS_getVForSourceType((__VLS_ctx.tasks))) {
        /** @type {[typeof TaskItem, ]} */ ;
        // @ts-ignore
        const __VLS_0 = __VLS_asFunctionalComponent(TaskItem, new TaskItem({
            ...{ 'onDelete': {} },
            ...{ 'onToggle': {} },
            key: (task.id),
            task: (task),
        }));
        const __VLS_1 = __VLS_0({
            ...{ 'onDelete': {} },
            ...{ 'onToggle': {} },
            key: (task.id),
            task: (task),
        }, ...__VLS_functionalComponentArgsRest(__VLS_0));
        let __VLS_3;
        let __VLS_4;
        let __VLS_5;
        const __VLS_6 = {
            onDelete: (__VLS_ctx.onDelete)
        };
        const __VLS_7 = {
            onToggle: (__VLS_ctx.onToggle)
        };
        var __VLS_2;
    }
    if (__VLS_ctx.tasks.length === 0) {
        __VLS_asFunctionalElement(__VLS_intrinsicElements.div, __VLS_intrinsicElements.div)({
            ...{ class: "text-center text-gray-500" },
        });
    }
}
/** @type {[typeof TaskCreateView, ]} */ ;
// @ts-ignore
const __VLS_8 = __VLS_asFunctionalComponent(TaskCreateView, new TaskCreateView({
    ...{ 'onCreated': {} },
}));
const __VLS_9 = __VLS_8({
    ...{ 'onCreated': {} },
}, ...__VLS_functionalComponentArgsRest(__VLS_8));
let __VLS_11;
let __VLS_12;
let __VLS_13;
const __VLS_14 = {
    onCreated: (__VLS_ctx.onCreated)
};
var __VLS_10;
/** @type {__VLS_StyleScopedClasses['text-center']} */ ;
/** @type {__VLS_StyleScopedClasses['text-gray-500']} */ ;
/** @type {__VLS_StyleScopedClasses['text-center']} */ ;
/** @type {__VLS_StyleScopedClasses['text-gray-500']} */ ;
var __VLS_dollars;
const __VLS_self = (await import('vue')).defineComponent({
    setup() {
        return {
            TaskItem: TaskItem,
            TaskCreateView: TaskCreateView,
            tasks: tasks,
            loading: loading,
            onDelete: onDelete,
            onToggle: onToggle,
            onCreated: onCreated,
        };
    },
});
export default (await import('vue')).defineComponent({
    setup() {
        return {};
    },
});
; /* PartiallyEnd: #4569/main.vue */
//# sourceMappingURL=TaskListView.vue.js.map
