function solution(t, p) {
    var answer = 0;
    for(let i=0; i<=t.length-p.length; i++){
        slicedString = t.slice(i,i+p.length)
        if (Number(slicedString) <= Number(p)) {
            answer ++ 
        }
    }
    return answer;
}