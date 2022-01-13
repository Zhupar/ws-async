// Создаёт WebSocket - подключение.

const socket = new WebSocket('ws://localhost:8080');

// Соединение открыто
socket.addEventListener('open', function (event) {
    console.log('opened')
});

// Наблюдает за сообщениями
socket.addEventListener('message', function (event) {
    p.before(event.data)
    console.log('Message from server ', event.data);
});

const sndMsg = () =>{
    socket.send('message');
    console.log('clicked')
};