// https://leetcode.com/problems/longest-common-prefix/
function longestCommonPrefixOfTwoStrings(a, b) {
  let prefix = "";

  let i = 0;
  while (i < a.length && i < b.length) {
    if (a[i] === b[i]) {
      prefix += a[i];
    } else {
      return prefix;
    }
    i += 1;
  }
  return prefix;
}

function longestCommonPrefix(strs) {
  if (strs.length == 1) {
    return strs[0];
  }

  let currentLongestPrefix = longestCommonPrefixOfTwoStrings(strs[0], strs[1]);
  for (let i = 2; i < strs.length; i++) {
    currentLongestPrefix = longestCommonPrefixOfTwoStrings(
      currentLongestPrefix,
      strs[i]
    );
  }
  return currentLongestPrefix;
}

console.log(longestCommonPrefix(["dog"]));
