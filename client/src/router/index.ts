import { createRouter, createWebHistory } from "vue-router";
import Start from "../views/Start.vue";
import Arena from "../views/Arena.vue";

const routes = [
  { path: "/", name: "Start", component: Start },
  { path: "/arena", name: "Arena", component: Arena }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;