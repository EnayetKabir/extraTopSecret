///Parse data
var Parse = require('node-parse-api').Parse;
var APP_ID = "GyUfmGoQbBBvBCKyH9r7qGK1GgWo6kYKLdi4MPjA";
var MASTER_KEY = "2ngE8d2O6S1ZliNAXyAM8EDXgSk3b7fV1MrIB1WL";
var appParse = new Parse(APP_ID, MASTER_KEY);

var bodyParser = require('body-parser');
var express = require("express");
var app = express();
var port = 8000;
var url='localhost';
var server = app.listen(port);
// WebSockets work with the HTTP server
var io = require('socket.io').listen(server);


///create server
app.use(express.static(__dirname + ''));
console.log('Simple static server listening at '+url+':'+port);

app.get('', function (req, res) {
  res.setHeader('Content-Type', 'text/plain; charset=utf-8');
  res.end('YOUR SERVER IS RUNNING');
})


// WebSocket Portion:-


// Register a callback function to run when we have an individual connection
io.sockets.on('connection',
  // We are given a websocket object in our function
  function (socket) {
  
    console.log("We have a new client: " + socket.id);
  
    // When this user emits, client side: socket.emit('otherevent',some data);
    socket.on('checkPass',
      function(data) {
        // Data comes in as whatever was sent, including objects
        console.log("Received: 'Password' " + data.passkey);
        //Search Parse for password
        appParse.find('passcodes', {where: {passcode: data.passkey}}, function (err, response) {
          var dataFromParse = response;
          console.log(dataFromParse);
          if (dataFromParse != undefined) {
          socket.emit('weGood',{ ParseData: dataFromParse });
          //UPDATE USE CASES
            appParse.update('passcodes', dataFromParse.results[0].objectId, {numOfUses: dataFromParse.results[0].numOfUses + 1} , function (err, response) {
            console.log(response);
            });
          }
        });
      }
    );
    
    
//DISCONNECT
    socket.on('disconnect', function() {
      console.log("Client has disconnected");
    });
  }
//close socket  
);