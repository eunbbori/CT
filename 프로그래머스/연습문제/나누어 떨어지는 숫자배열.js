function solution(arr, divisor) {
    var answer = [];
    answer = arr.filter(el => el % divisor === 0)
    sortedAnswer = answer.sort((a,b) => a-b)
    if (sortedAnswer.length === 0) {
        sortedAnswer.push(-1)
    }
    return sortedAnswer;
}

// 더 간단히 
function solution(arr, divisor) {
    var answer = arr.filter(v => v%divisor == 0);
    return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}