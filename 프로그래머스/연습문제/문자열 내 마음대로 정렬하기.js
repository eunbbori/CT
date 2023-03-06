// 테스트만 통과 
function solution(strings, n) {
    var answer = [];
    var newArr = [];
    for(let i=0; i<strings.length; i++){
        let word = strings[i]
        let key = word[n]
        let newWords = {
            [key]:word
        }
        newArr.push(newWords)
        let sortedByKey = newArr.sort((a,b) =>  Object.keys(a) < Object.keys(b)? -1 : Object.values(a) < Object.values(b)? -1 : 1)
    }
    for(let i=0; i<newArr.length; i++){
        answer.push(Object.values(newArr[i])[0])
    }
    return answer;
}

// 정답 1
function solution(strings, n) {
    return strings.sort((a, b) => {
      // 인덱스 n번째 글자를 기준으로 오름차순 정렬
      if (a[n] > b[n]) return 1;
      else if (a[n] < b[n]) return -1;
      // 인덱스 n번째 글자가 같으면 사전순 정렬
      else return a > b ? 1 : -1;
    });
  }

// 정답 2
function solution(strings, n) {
    // strings 배열
    // n 번째 문자열 비교
    return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}