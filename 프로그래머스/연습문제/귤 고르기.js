function solution(k, tangerine) {
    var answer = 0;
    var numbering = {};
    var sortedValue = []
    var cnt = 0
    
    sortedArr = tangerine.sort((a,b) => a-b)
    
    for (const v of sortedArr) {
        numbering[v] = numbering[v] ? numbering[v] + 1 : 1;
    }
    
    let sorted = Object.entries(numbering).sort((a, b) => b[1] - a[1]);

    for(let element of sorted) {
        if(cnt >= k) {
            return answer
        }
        sortedValue.push(element[0])
        cnt += element[1]
        answer += 1
        // console.log(element[0]+ ": " + element[1]);
    }

    return answer;
}