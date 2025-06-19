<template>

    <h1>Enter your username:</h1>
    <input type="text" v-model="username">
    <button @click="enterLobby">Enter lobby</button>

</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useSocket} from "../composables/useSocket";

const router = useRouter();
const username = ref("");

useSocket()

function enterLobby() {
  if (username.value.trim()) {
    // localStorage.setItem('username', username.value);
    router.push("/arena");
    useSocket().sendMessage("set_username", username.value);
  }
}
</script>