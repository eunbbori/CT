// function solution(n,input,m){
//     console.log(n);
//     console.log(input);
//     console.log(m);
// }

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (x) {
    input.push(x)
 // rl.close();
}).on("close", function () {
   let n = parseInt(input[0]);
   let list = input[1].split(' ').map( (el) => parseInt(el)); 
   let m = parseInt(input[2]);
  // solution(n,list,m); 

  
let cnt = 0; 

list.forEach(el => {
    if(el === m) {
        cnt += 1; 
    } 
})
console.log(cnt)


  process.exit();
});


