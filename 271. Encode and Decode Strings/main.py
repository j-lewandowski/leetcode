# https://neetcode.io/problems/string-encode-and-decode
class Solution:
  """
  @param: strs: a list of strings
  @return: encodes a list of strings to a single string
  """
  def encode(self, strs):
    result = ""
    for s in strs:
      result += str(len(s)) + "#" + s

    return result
  
  """
  @param: str: a single string
  @return: decodes a single string to a list of strings
  """
  def decode(self, str):
    result = []
    i = 0
    length = 0
    while i < len(str):
      j = i
      while str[j] != '#':
        j += 1
      length = int(str[i:j])
      result.append(str[j+1:j+1+length])
      i = j + 1 + length
    return result