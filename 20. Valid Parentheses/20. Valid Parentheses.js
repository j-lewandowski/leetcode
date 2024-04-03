// https://leetcode.com/problems/valid-parentheses/description/

function isValid(s) {
  let amounts = {
    "(": 0,
    ")": 0,
    "{": 0,
    "}": 0,
    "[": 0,
    "]": 0,
  };

  for (let i = 0; i < s.length; i++) {
    amounts[s[i]] += 1;
  }

  for (let i = 0; i < Object.keys(amounts).length; i = i + 2) {
    if (
      amounts[Object.keys(amounts)[i]] !== amounts[Object.keys(amounts)[i + 1]]
    ) {
      return false;
    }
  }
  return true;
}

console.log(isValid("([)]"));
