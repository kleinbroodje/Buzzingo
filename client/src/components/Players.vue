<template>
    <button id="s" class="sideBarButton" :style="sideBarButtonStyle" @click="toggled = !toggled">{{ toggled ? ">>" : "<<" }}</button>
    <div id="playerList" class="sideBar" :style="sideBarStyle">
        <p v-for="player in playerList">{{ player }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useSocket } from "../composables/useSocket";

let playerList = ref([]);
let toggled = ref(false);

const sideBarStyle = computed(() => ({
    width: toggled.value ? "300px" : "0px",
}));
const sideBarButtonStyle = computed(() => ({
    marginRight: toggled.value ? "300px" : "0px",
}));

useSocket().onMessage("player_list", (data: any) => {
  playerList.value = data;
});

</script>

<style lang="scss" scoped>
$bgcolor: #323030;

.sideBar {
    position: fixed;
    width: 0;
    height: 100%;
    overflow-x: hidden; 
    transition: 0.5s; 
    background-color: $bgcolor;
    color: rgb(248, 248, 248);
    right: 0;
    top: 0;
    z-index: 1;
    font-size: 30px;
}

.sideBarButton {
    position: fixed;
    top: 20px;
    right: 25px;
    font-size: 36px;
    border: none;
    color: white;
    background-color: $bgcolor;
    right: 0;
    cursor: pointer;
    transition: margin-right .5s
}
</style>