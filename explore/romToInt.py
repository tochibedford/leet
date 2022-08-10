class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        standard = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        modifiers = ['C', 'X', 'I']

        for index, char in enumerate(s):
            if char in modifiers:
                if index != len(s)-1 and standard[s[index+1]] > standard[char]:
                    total -= standard[char]
                else:
                    total += standard[char]
            else:
                total += standard[char]

            # if char == 'M':
            #     total += 1000
            # if char == 'D':
            #     total += 500
            # if char == 'C':
            #     if index != len(s)-1:
            #         if standard[s[index+1]] > standard['C']:
            #             total -= 100
            #         else:
            #             total += 100
            #     else:
            #         total += 100
            # if char == 'L':
            #     total += 50
            # if char == 'X':
            #     if index != len(s)-1:
            #         if standard[s[index+1]] > standard['X']:
            #             total -= 10
            #         else:
            #             total += 10
            #     else:
            #         total += 10
            # if char == 'V':
            #     total += 5
            # if char == 'I':
            #     if index != len(s)-1:
            #         if standard[s[index+1]] > standard['I']:
            #             total -= 1
            #         else:
            #             total += 1
            #     else:
            #         total += 1
            # now simplify

        return total

        '''
        how i interpret in my head
        I know some standard figures like: I, V, X, L and so on
        then I break the roman script into its smaller components
        I then convert these individual components and say the total

        5, 50, 500 and so on can have 'modifiers'
        '''

print(Solution().romanToInt('MCM'))

print(Solution().romanToInt('III'))

print(Solution().romanToInt('LVIII'))

print(Solution().romanToInt('VIII'))

print(Solution().romanToInt('MCMXCIV'))


# what i realized, and statements short circuit the if statement so if the first evaluation is false everything after the and doesn't even evaluate
# basically no need to nest the if statements unnecessarily