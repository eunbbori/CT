// 1) 

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputCnt = 0;
let inputIterCnt = 0;
let strArr = [];

rl.on("line", function (x) {
  if(inputCnt === 0) {
    inputIterCnt = parseInt(x);
  }
  else {
      strArr.push(x);
  }
  if (inputCnt === inputIterCnt) {
      rl.close();
  }
  inputCnt += 1;
}).on("close", function () {
    strArr.forEach(val => {
        console.log(val.toLowerCase().charAt(0).toUpperCase() + val.toLowerCase().slice(1));
    })
  process.exit();
});

// 2) 
    /*
    const readline = require('readline');

    const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    });
    let inputs = [];
    let inputCount = 0;
    let iterationCount = 0;

    rl.on('line', function (x) {
    if (inputCount === 0) {
        iterationCount = parseInt(x) + 1;
        inputCount++;
    } else {
        inputs.push(x);
        inputCount++;
    }

    if (inputCount === iterationCount) {
        rl.close(inputs);
    }
    }).on('close', function () {
    let result = inputs.reduce((acc, str, index) => {
        let filterResult = [];
        //첫글자 커리 및 전체 소문자 처리
        [...str].forEach((s, index) =>
        index === 0
            ? (filterResult[index] = s.toUpperCase())
            : (filterResult[index] = s.toLowerCase())
        );
        return [...acc, filterResult.join('')];
    }, []);
    result.forEach(str => console.log(str));
    process.exit();
    });
    */