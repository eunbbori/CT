function solution(n,a,b)
{
    let cnt = 1;
    while(Math.ceil(a/2) !== Math.ceil(b/2)){
        a = Math.ceil(a/2);
        b = Math.ceil(b/2);
        cnt++;
    }

    return cnt;
}

// 다른 풀이 
function solution(n,a,b)
{
    let answer = 0;

    while(n > 1) {
        ++answer;
        n = n / 2;        
        a = Math.round(a / 2);
        b = Math.round(b / 2);

        if( a === b ) {
            break;   
        }
    }

    return answer;
}