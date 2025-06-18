<template>

    <h1>Enter your username:</h1>
    <input type="text" v-model="username">
    <button @click="enterLobby">Enter lobby</button>

</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { io } from "socket.io-client";

const router = useRouter();
const socket = io("http://localhost:5000");

const username = ref("");

function enterLobby() {
  if (username.value.trim()) {
    // localStorage.setItem('username', username.value);
    router.push("/arena");
  }
}
</script>