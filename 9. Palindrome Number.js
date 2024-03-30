//leetcode.com/problems/palindrome-number/description/

https: function isPalindrome(x) {
  if (x < 0) return false;

  const number = x;
  let number_reversed = 0;

  while (x > 0) {
    number_reversed = number_reversed * 10 + (x % 10);
    x = parseInt(x / 10);
  }
  // console.log(number, number_reversed);
  return number === number_reversed;
}

console.log(isPalindrome(1221));
