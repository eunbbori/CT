const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = []

rl.on("line", function (x) {
  input.push(x)

  //rl.close();
}).on("close", function () {
    let n = parseInt(input[0])
    let result = []

    for(let i=0; i<n; i++){
        let list = input[i+1].split(' ').map((el) => String(el));
        let A = list[0];
        let B = list[1];

        let EliceSum = parseInt(A.split('').reverse().join("")) + parseInt(B.split('').reverse().join("")); //reverse 사용 주의 
        let answer = String(EliceSum).split('').reverse().join("")

        result.push(answer)

    }
    console.log(result.join('\n'))

  process.exit();
});
