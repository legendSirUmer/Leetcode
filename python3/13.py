

def romanToInt(self, s: str) -> int:
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    print(dic.items())
    for i in range(len(s)):
        if s[i] in dic:
            if i + 1 < len(s) and dic[s[i]] < dic[s[i + 1]]:
                total -= dic[s[i]]
            else:
                total += dic[s[i]]

    return total



print(romanToInt(None, "MCMXCIV")  )
     