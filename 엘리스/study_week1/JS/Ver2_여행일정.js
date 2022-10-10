const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputStr; 

rl.on("line", function (s) {
  inputStr = s ; 
  rl.close();
}).on("close", function () {
   dateArr = inputStr.split('-');
   let MM_31 = [1,3,5,7,8,10,12];
   let MM_30 = [4,6,9,11];

   let year = parseInt(dateArr[0]);
   let month = parseInt(dateArr[1]);
   let date = parseInt(dateArr[2]);

   trueMonth = month >= 1 && month <= 12 
   YoonYear  = (year%4 === 0 && year % 100 !== 0 ) || (year % 400 === 0)

   if(!trueMonth || (MM_31.includes(month) && date > 31) || (MM_30.includes(month) && date > 30) || 
   (month === 2 && YoonYear && date > 29 ) || (month === 2 && !YoonYear && date > 28) || date <= 0 ) {
       console.log(0)
   }else {
       console.log(1)
   }



  process.exit();
});
