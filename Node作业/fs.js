const fs = require("fs")
fs.readFile("./a.txt",{
	flag:"r",
	encoding:"utf8"
},function(e,d){
	console.log(d.toString())
})

fs.writeFile("./a.txt","写一行进入",function(e){
	if(e){
		console.log(e)
	}
})
