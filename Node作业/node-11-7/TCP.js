const net  = require("net");
const util = require("util");

var server = net.createServer({allowHalfOpen:false},function(socket){
	socket.on("data",function(data){
		console.log(data);
	});
});

server.listen(8899,function(err){
	if(err)console.log(err);
})