<template>
    <button id="s" class="sideBarButton" :style="sideBarButtonStyle" @click="toggled = !toggled">{{ toggled ? ">>" : "<<" }}</button>
    <div id="playerList" class="sideBar" :style="sideBarStyle">
        <h2>Players:</h2>
        <hr>
        <p v-for="player in usePlayerList().get()">{{ player }}</p>
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useSocket, usePlayerList } from "../composables/useSocket";

let toggled = ref(true);

const sideBarStyle = computed(() => ({
    width: toggled.value ? "300px" : "0px",
}));
const sideBarButtonStyle = computed(() => ({
    marginRight: toggled.value ? "300px" : "0px",
}));

useSocket().onMessage("player_list", (data: any) => {
    usePlayerList().set(data);
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

    display: flex;
    flex-direction: column;
    align-items: flex-start;

    h2 {
        margin: 10px;
    }
    
    hr {
        width: 100%;
    }

    p {
        margin: 10px;
        margin-left: 35px;
        left: 0%;
    }
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