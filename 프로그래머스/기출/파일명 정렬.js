// 방법 1
function solution(files) {
    files.sort((a, b) => {
      const first = tokenize(a);
      const second = tokenize(b);
      return fileSort(first, second);
    });
    return files;
  }
  
  function tokenize(file) {
    let startNumIdx; //  처음에 undefined ( undefined는 false )
    let endNumIdx;
    for (let i = 0; i < file.length; i++) {
      if (!startNumIdx && isNumber(file[i])) {
        startNumIdx = i;
      }
      if (startNumIdx && !isNumber(file[i + 1])) {
        endNumIdx = i;
        break;
      }
    }
    const head = file.slice(0, startNumIdx);
    const num = file.slice(startNumIdx, endNumIdx + 1);
    //비교해주기 위해 문자열은 소문자로 숫자string은 숫자로 만들어준다.
    return [head.toLowerCase(), num * 1];
  }
  function isNumber(char) {
    return !isNaN(parseInt(char));
  }
  
  
  function fileSort(first, second) {
    let [firstHead, firstNum] = first;
    let [secondHead, secondNum] = second;
    if (firstHead < secondHead) {
      return -1;
    } else if (firstHead > secondHead) {
      return 1;
    } else return firstNum - secondNum;
  }

// 방법 2
function solution(files) {
    return files.sort((a, b) => {
      const aHead = a.match(/^\D+/)[0].toLowerCase();
      const bHead = b.match(/^\D+/)[0].toLowerCase();
  
      if(aHead < bHead) return -1;
      if(aHead > bHead) return 1;
  
      const aNum = a.match(/\d+/)[0].replace(/^0+/, '');
      const bNum = b.match(/\d+/)[0].replace(/^0+/, '');
  
      return aNum - bNum;
    });
  }

  /**
 ^ : 문자열의 시작
＼D : 숫자가 아닌 문자
+ : 앞의 표현식이 1회 이상 연속으로 반복

＼d : 숫자

*/
