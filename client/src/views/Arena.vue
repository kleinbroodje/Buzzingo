<template>
  <div class="text">
    <h1>{{ stateToText }}</h1>
  </div>
  <button @click="onClick" class="buzzer"/>
</template>

<script setup lang="ts">

import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useSocket, usePlayerList } from "../composables/useSocket";
import buzzer_path from '../assets/sfx/buzzer.wav';
import duel_path from '../assets/sfx/duel.mp3';

const buzzer = new Audio(buzzer_path);
const duel = new Audio(duel_path);
duel.volume = 0.4;

const router = useRouter();

onMounted(() => {
  if (sessionStorage.getItem("username") === null) {
    router.push("/")
  } else {
    useSocket().sendMessage("set_username", sessionStorage.getItem("username"));
  }
})

const lobbyState = ref("waiting");
let remainingTime = ref(0);
let currentWord = ref("");

const stateToText = computed(() => {
  if (lobbyState.value === "waiting") {
    return waitingText.value;
  } else if (lobbyState.value === "countdown") {
    return countdownText.value;
  } else if (lobbyState.value === "word") {
    return currentWord.value;
  } else {
    return "Error";
  }
})

const waitingText = computed(() => {
  return `Waiting for players (${usePlayerList().get().length} / 2)`;
})

const countdownText = computed(() => {
  return `${remainingTime.value}`;
})

function onClick() {
  buzzer.play();
}

useSocket().onMessage("new", (data: string) => {
  currentWord.value = data;
});

useSocket().onMessage("countdown", (time: number | string) => {
  lobbyState.value = "countdown";
  remainingTime.value = time as number;
  if (typeof time !== "number") {
    duel.play()
  }
})

</script>

<style lang="scss" scoped>
h1 {
  font-size: 50px;
  color: white;
}

.buzzer {
  position: absolute;
  width: 200px;
  height: 200px;
  background-color: #fa3434;
  border-radius: 50%;
  cursor: pointer;
  border: none;
  margin:auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;

  &:hover
  {
    background-color: rgb(198, 57, 57);
  }

  &:active
  {
    scale: 0.9;
  }
}

.text {
  position: absolute;
  color: white;
  // border: white 1px solid;
  border-radius: 10px;
  padding: 20px;
  left: 50%;
  transform: translateX(-50%);
  top: 15%;
}
</style>