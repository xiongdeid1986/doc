var n = 100;
console.log(n.toString(2))
console.log(n.toString(8))
console.log(n.toString(16))
console.log(n.toString(10))

//2,8,10转10进制
var binary = 100100;
var octnary = n.toString(8);
var sixteen = 0x77;

console.log(parseInt(binary,"2"))
console.log(parseInt(octnary,"8"))
console.log(parseInt(sixteen,"16"))

var bf1 = new Buffer("abc","utf-8");
bf1[2] = 02;
const string_decoder = require("string_decoder").StringDecoder;
const Decoder = new string_decoder("utf-8")
console.log(bf1)
console.log(Decoder.write(bf1))
var bf2 = new Buffer()
console.log(bf2.byteLenght("okokjkjojijiojfdsf","utf-8"))

