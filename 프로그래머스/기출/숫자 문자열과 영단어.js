function solution(s) {
  var answer = 0;
  var words = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
  
  for(var key in words) {
      if(s.includes(key)) {
          wordNum = words[key]
          s = s.replaceAll(key,wordNum)
      }
  }
  answer = Number(s)
  
  return answer;
}

//다른 방법
function solution(s) {
    let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    var answer = s;

    for(let i=0; i< numbers.length; i++) {
        let arr = answer.split(numbers[i]);
        answer = arr.join(i);
    }

    return Number(answer);
}