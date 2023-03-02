function isValid(s) {
  let open = ["(","{","["]
  let close = [")","}","]"]
  let stack = []
  let bracketArr = s.split("")
  
  if(close.includes(bracketArr[0]) === true || open.includes(bracketArr[bracketArr.length-1])){
      return false;
  }
  bracketArr.forEach((v) => {
      if (open.includes(v) === true) {
          stack.push(open.indexOf(v));
      }else {
          if(stack.length > 0 && stack[stack.length - 1] === close.indexOf(v)) {
              stack.pop();
          }else {
              stack.push(close.indexOf(v));
          }
      }
  });
  if (stack.length === 0) return true;
  else return false;
}

function solution(s) {
  let answer = 0;
  for(let i=0; i<s.length; i++){
      let char = s[0];
      s = s.concat(char).slice(1,s.length+1);
      if(isValid(s) === true){
          answer++;
      }
  }
  
  return answer;
}