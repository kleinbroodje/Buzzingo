<template>
  <button @click="startrecognition">Start</button>
  <h1>{{ trans }}</h1>

</template>

<script setup lang="ts">
import { ref } from 'vue'

const trans = ref<String>("hello");

function startrecognition(): void {
  recog.start();

  recog.onstart = () => {
    console.log("Recognition started");
  };

  recog.onaudiostart = () => {
    console.log("Audio started");
  };

  recog.onspeechstart = () => {
    console.log("Speech detected");
  };

 recog.onerror = (event: any) => {
  console.error("Speech recognition error:", event.error);
  };

  recog.onend = () => {
    console.log("Recognition ended");
  };

  recog.onresult = parseRecognition;
}

function parseRecognition(event: typeof SpeechRecognitionEvent): void {
  const results = Array.from(event.results) as SpeechRecognitionResult[];
  const transcript = results
    .map((result: SpeechRecognitionResult) => result[0])
    .map((result: SpeechRecognitionAlternative) => result.transcript)
    .join("");
  trans.value = transcript;
}

const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
const SpeechRecognitionEvent = (window as any).SpeechRecognitionEvent || (window as any).webkitSpeechRecognitionEvent;

const recog = new SpeechRecognition();
recog.lang = "ja-JP";
recog.interimResults = true;
recog.continuous = true;

</script>

<style scoped>

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

</style>
