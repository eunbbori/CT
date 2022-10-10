const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});


let inputList = []
rl.on("line", function (item) {
   inputList =  item.split(' ').map((e) => parseInt(e)); 

  rl.close();
}).on("close", function () {  
  let N = inputList[0]
  let B = inputList[1]

  console.log(N.toString(B))
  process.exit();
});
