// const http = require('http');
// const WebSocket = require('ws');
// import WebSocket from 'websocket';

let socket = new WebSocket("ws://echo.websocket.org");

socket.send("hehehehe");

socket.onmessage = function(event){
    console.log(`data received - ${event.data}`);
}