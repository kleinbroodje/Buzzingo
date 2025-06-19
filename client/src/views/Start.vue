<template>

    <h1>Enter your username:</h1>
    <input type="text" v-model="username" @keyup.enter="enterLobby">
    <button @click="enterLobby">Enter lobby</button>

</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useSocket } from "../composables/useSocket";

onMounted(() => {
  sessionStorage.removeItem("username");
})

const router = useRouter();
const username = ref("");

useSocket().init();

function enterLobby() {
  if (username.value.trim()) {
    sessionStorage.setItem("username", username.value);
    router.push("/arena");
    useSocket().sendMessage("set_username", username.value);
  }
}
</script>