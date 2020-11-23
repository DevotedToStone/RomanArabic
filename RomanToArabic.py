class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        try:
            j = 0
            for i in range(0, len(s) - 1):
                if roman[s[i]] < roman[s[i + 1]]:
                    j -= roman[s[i]]
                else:
                    j += roman[s[i]]
            return j + roman[s[-1]]
        except KeyError:
            return None

    def checklenght(self, s: str):
        if 1 <= len(s) <= 15:
            return True
        else:
            return False


R = Solution()
print('Введите римское число:')
s = input()
if R.checklenght(s) == True:
    print(R.romanToInt(s))
else:
    print('Недопустимая длина числа')
