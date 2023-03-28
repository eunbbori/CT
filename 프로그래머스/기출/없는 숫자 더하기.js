function solution(numbers) {
    let sum = 0; 
    for(let i=0; i<numbers.length; i++){
        sum += numbers[i]
    }

    return 45-sum;
}


// 풀이 2
function solution(numbers) {
    return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}

//풀이 3
function solution(numbers) {
    let answer = 0;

    for(let i = 0; i <= 9; i++) {
        if(!numbers.includes(i)) answer += i;
    }

    return answer;
}