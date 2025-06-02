class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    skip = False
    for index, letter in enumerate(s):
      if skip:
        skip = False
        continue

      if letter == 'I' and index < len(s) - 1:
        if s[index + 1] == 'V':
          result += 4
        elif s[index + 1] == 'X':
          result += 9
        else:
          result += 1
          continue
        skip = True

      elif letter == 'I':
        result += 1

      elif letter == 'V':
        result += 5

      elif letter == 'X' and index < len(s) - 1:
        if s[index + 1] == 'L':
          result += 40
        elif s[index + 1] == 'C':
          result += 90
        else:
          result += 10
          continue
        skip = True

      elif letter == 'X':
        result += 10

      elif letter == 'L':
        result += 50

      elif letter == 'C' and index < len(s) - 1:
        if s[index + 1] == 'D':
          result += 400
        elif s[index + 1] == 'M':
          result += 900
        else:
          result += 100
          continue
        skip = True

      elif letter == 'C':
        result += 100

      elif letter == 'D':
        result += 500

      elif letter == 'M':
        result += 1000

      print(letter, result)
    return result

example = Solution()
print(example.romanToInt('III'))
print(example.romanToInt('LVIII'))
print(example.romanToInt('MCMXCIV'))
print(example.romanToInt('DCXXI'))