import { ref } from "vue";
import { io, Socket } from "socket.io-client";

let socket: Socket | null = null;

export function useSocket() {
  if (!socket) {
    socket = io("http://localhost:3000");
  }

  const connected = ref(false);

  socket.on("connect", () => {
    connected.value = true;
    console.log("Socket connected:", socket?.id);
  });

  socket.on("disconnect", () => {
    connected.value = false;
    console.log("Socket disconnected");
  });

  function sendMessage(event: string, payload: any) {
    socket?.emit(event, payload);
  }

  function onMessage(event: string, callback: (...args: any[]) => void) {
    socket?.on(event, callback);
  }

  return { connected, sendMessage, onMessage, socket };
}
