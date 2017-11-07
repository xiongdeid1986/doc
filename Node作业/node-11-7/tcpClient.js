const fs = require("fs");
const util = require("util");
const net = require("net");

var socket = new net.Socket({allowHalfOpen:true});
socket.setEncoding("utf-8");
socket.connect(8089,"localhost",function(){
	socket.write("hello?");
	socket.on("data",function(data){
		console.log(data);
	})
});
