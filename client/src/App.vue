<template>
  <div class="main">
    <router-view style="width: 100%;"/>
    <Players />
  </div>
</template>

<script setup lang="ts">
import Players from './components/Players.vue';
</script>

<style lang="scss">
.main {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
}
</style>