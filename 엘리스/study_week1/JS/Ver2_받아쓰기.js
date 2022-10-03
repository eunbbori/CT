const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input =[]; 
rl.on("line", function (x) {
    input.push(x)
  //console.log(x);
  //rl.close();
}).on("close", function () {
    let list = input[0].split(' ').map( (el) => parseInt(el)); 
    let strA = input[1]; 
    let strB = input[2]; 
    // let n = list[0]
    // let m = list[1]
    if(strB.includes(strA)){
        console.log('1')
    }else console.log('0')
    

  process.exit();
});
