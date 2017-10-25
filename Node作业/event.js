//订阅事件
//数组apply call bind(功能)
//给文件绑定事件
//添加事件 监听事件
//写一个单次监听函数(移除事件)
//发射事件
//使用ulit继承事件
const EventEmitter = require("events").EventEmitter;
const fs = require("fs")
const util = require("util")
var Msgevent = new EventEmitter();
Msgevent.on("message",function(msg){
	console.log(msg)
})

setInterval(function(){
	Msgevent.emit("message","监听成功")
},1000);

function message(e,msg){
	Msgevent.emit(e,msg);
}


var NewMsg = message.bind(this,"message")
NewMsg.prototypee.emit = function(a,b){
	Msgevent.prototype.emit.call(this)
}
//util.inherits(NewMsg,EventEmitter);
//NewMsg.on("set",function(i){
//	console.log(`${i} 次 set...`)
//})
//console.log(NewMsg);
var i = 0;
setInterval(function(){
	NewMsg("您有新的信息...");
//	NewMsg.emit("set",i)
	i++;
},1500)
