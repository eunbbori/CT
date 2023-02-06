function solution(s) {
  var answer = [];
  
  for(let i=0; i<s.length; i++){
      if(i === 0) {answer.push(-1)}
      else {
        sliced = s.slice(0,i)
        if(!sliced.includes(s[i])){
           answer.push(-1)
        }else {
           newIdx = i - sliced.lastIndexOf(s[i]) 
            answer.push(newIdx)
           }
      }
  }
  
  return answer;
}