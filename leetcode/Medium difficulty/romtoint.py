class Solution:
    def RomanToInt(self, _string):
        book = {"I": 1, "X": 10, "V": 5, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for num in range(len(_string)):
            if num == len(_string) - 1:
                total += book[_string[num]]
            elif book[_string[num]] < book[_string[num + 1]]:
                total -= book[_string[num]]
            else:
                total += book[_string[num]]
        return total


x = Solution()
print(x.RomanToInt("LIV"))
