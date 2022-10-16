const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N ;

rl.on("line", function (n) {
  N = parseInt(n) 
  
  rl.close();
}).on("close", function () {
  let result = []
  let cnt = 0;

  for(let i=1; i<N+1;i++){
      if(N % i === 0){
          cnt ++ ; 
          result.push(i)
      }
  } 
  result.splice(0,0,cnt)
  console.log(result.join('\n'))

  process.exit();
});
