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

//다른 풀이 
function solution(s) {
  const hash = {};

  return [...s].map((v,i) => {
    let result = hash[v] !== undefined ? i-hash[v] : -1;
    hash[v] = i;
    return result;
  });
}

//다른 풀이 
const solution = (s) =>
  [...s].map((char, i) => {
    const count = s.slice(0, i).lastIndexOf(char);
    return count < 0 ? count : i - count;
  });