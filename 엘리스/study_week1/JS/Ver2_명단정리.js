const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = []; 
rl.on("line", function (x) {
    input.push(x);
  //rl.close();
}).on("close", function () {
    let n = parseInt(input[0]);
    let result = []; 
    
    for(let i=0; i<n; i++){
        let cnt = 0;  //cnt 초기화 주의 ! 
        
        str = input[i+1]; 
        strUpper = str.toUpperCase(); 

        for(let i=0; i<str.length; i++){
            if(str[i] === strUpper[i]){
            cnt  += 1; 
            if(cnt === 2){
                result.push(str.slice(i))
                break; 
            }
        }
        }
    }

    console.log(result.join('\n'))

  process.exit();
});
