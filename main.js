// Создаёт WebSocket - подключение.
let news = ''
const socket = new WebSocket('ws://localhost:8080');

// Соединение открыто
socket.addEventListener('open', function (event) {
    console.log('opened');
    socket.send('message');
});

// Наблюдает за сообщениями
let fromServer = socket.addEventListener('message', function (event) {
    news += '<blockquote>Latest news: '+ new Date() + "\n\n" + event.data +'</blockquote>';
    document.querySelector("#p").innerHTML = news;
    console.log('Message from server ', event.data);
});


