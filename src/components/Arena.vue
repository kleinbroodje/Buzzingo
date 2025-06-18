<template>
    <div class="display">
        <h1>Klik als Leo een poepie is</h1>
    </div>
    <button @click="onClick" class="buzzer"/>
</template>

<script lang="ts" setup>
import buzzer from '../assets/sfx/buzzer.wav';
const audio = new Audio(buzzer);

function onClick() {
    audio.play();
}
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
  width: 200px;
  height: 200px;
  background-color: #fa3434;
  border-radius: 50%;
  cursor: pointer;
  border: none;

  &:hover
  {
    background-color: rgb(198, 57, 57);
  }

  &:active
  {
    scale: 0.9;
  }
}

.display {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  border: white 1px solid;
  border-radius: 10px;
  padding: 20px;
}
</style>