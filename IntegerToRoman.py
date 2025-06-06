class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        conversion = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]
        result = ''
        for key, val in conversion:
            while num >= val:
                result += key
                num -= val
        return result

example = Solution()
print(example.intToRoman(num=3749))
print(example.intToRoman(num=58))
print(example.intToRoman(num=1994))