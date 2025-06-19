<template>
  <div class="arena">
    <div class="text">
      <h1>{{ currentWord }}</h1>
    </div>
    <button @click="onClick" class="buzzer"/>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useSocket} from "../composables/useSocket";
import buzzer from '../assets/sfx/buzzer.wav';
const audio = new Audio(buzzer);

let currentWord = ref("");

function onClick() {
    audio.play();
}

useSocket().onMessage("new", (data: string) => {
    currentWord.value = data;
});

</script>

<style lang="scss" scoped>
@font-face {
    font-family: Winky Sans;
    src: url('src/assets/fonts/WinkySans-VariableFont_wght.ttf');
}

h1 {
    font-family: 'Winky Sans';
    font-size: 40px;
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
  transform: translate(-50%, -50%);
  top: 50%;

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
  border: white 1px solid;
  border-radius: 10px;
  padding: 20px;
  left: 50%;
  transform: translateX(-50%);
  top: 15%;
  width: 100px;
}

.arena {
  position: relative;
  height: 100%;
  width: 100%;
}
</style>