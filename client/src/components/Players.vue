<template>
    <div class="side_bar">
        <ul>
            <li v-for="player in playerList">{{ player }}</li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useSocket} from "../composables/useSocket";

let playerList = ref([]);

useSocket().onMessage("player_list", (data: any) => {
  playerList.value = data;
});
</script>

<style lang="scss" scoped>
.side_bar {
    width: 300px;
    height: 100%;
    background-color: #0f0e0e;
    color: rgb(0, 0, 0);
}
</style>