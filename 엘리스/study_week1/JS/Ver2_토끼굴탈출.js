const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = []; 

rl.on("line", function (x) {
  input.push(x);   
 
// rl.close();
}).on("close", function () {
    let n = parseInt(input[0]);
    let str = input[1]; 
    let arr = str.split(''); 

    let upperCnt = 0; 
    let lowerCnt = 0; 
    let digitCnt = 0; 
    let newStr = '';

   arr.forEach(el => {
       if(!isNaN(el)){      // 문자열의 요소가 숫자타입이라면 
           digitCnt += 1;   // 숫자카운트 1 증가 
       }else {              // 문자열의 요소가 숫자타입이 아니라면
           newStr += el;    // 숫자를 제외한 새로운 스트링 생성 
       }
   })
    
    let newArr = newStr.split(''); 

    newArr.forEach(el => {    //forEach는 배열에서만 사용 가능하다 
        if(el === el.toUpperCase()){  
            upperCnt += 1 
        }else if(el === el.toLowerCase()){
            lowerCnt += 1 
        }
    })

    console.log(upperCnt,lowerCnt,digitCnt)
 
  process.exit();
});
