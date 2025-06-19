import { io, Socket } from "socket.io-client";

let socket: Socket | null = null;

export function useSocket() {
  if (!socket) {
    socket = io("http://localhost:5000");
  }

  socket.on("connect", () => {
    console.log("Socket connected:", socket?.id);
  });

  socket.on("disconnect", () => {
    console.log("Socket disconnected");
  });

  function sendMessage(event: string, payload: any) {
    socket?.emit(event, payload);
  }

  function onMessage(event: string, callback: (...args: any[]) => void) {
    socket?.on(event, callback);
  }

  return { sendMessage, onMessage, socket };
}
