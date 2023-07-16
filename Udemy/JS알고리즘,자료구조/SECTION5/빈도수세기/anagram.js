// version 1
function validAnagram(str1, str2) {
  if (str1.length !== str2.length) {
    return false;
  }

  let frequencyObj1 = {};
  let frequencyObj2 = {};

  for (let val of str1) {
    frequencyObj1[val] = (frequencyObj1[val] || 0) + 1;
  }
  for (let val of str2) {
    frequencyObj2[val] = (frequencyObj2[val] || 0) + 1;
  }

  for (let key in frequencyObj1) {
    if (!(key in frequencyObj2)) {
      return false;
    }
    if (frequencyObj2[key] !== frequencyObj1[key]) {
      return false;
    }
  }
  return true;
}

// version 2
function validAnagram(first, second) {
  if (first.length !== second.length) {
    return false;
  }

  const lookup = {};

  for (let i = 0; i < first.length; i++) {
    let letter = first[i];
    lookup[letter] ? (lookup[letter] += 1) : (lookup[letter] = 1);
  }

  for (let i = 0; i < second.length; i++) {
    if (!lookup[letter]) {
      return false;
    } else {
      lookup[letter] -= 1;
    }
  }
  return true;
}

// {a: 0, n: 0, g: 0, r: 0, m: 0, s:1}
validAnagram("anagrams", "nagaramm");
