<template>
    <button id="s" class="sideBarButton" @click="toggleSideBar"><<</button>
    <div id="playerList" class="sideBar">
        <p v-for=" player in playerList">{{ player }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useSocket} from "../composables/useSocket";

let playerList = ref([]);

useSocket().onMessage("player_list", (data: any) => {
  playerList.value = data;
});

let toggled = ref(false);
function toggleSideBar() {
    if (!toggled.value) {
        document.getElementById("playerList")!.style.width = "300px";
        document.getElementById("s")!.style.marginRight = "300px";
    }
    else {
        document.getElementById("playerList")!.style.width = "0";
        document.getElementById("s")!.style.marginRight = "0";
    }
    toggled.value = !toggled.value;

}
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