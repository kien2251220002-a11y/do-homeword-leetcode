class Solution:
    def reformatNumber(self, number: str) -> str:
        digit = number.replace(" ", "").replace("-","")

        result = []
        i = 0 
        n = len(digit)

        while n - i > 4:
            result.append(digit[i:i+3])
            i += 3

        remaining = n - i

        if remaining == 4:
            result.append(digit[i:i+2])    
            result.append(digit[i+2:i+4])

        else:
            result.append(digit[i:])

        return "-".join(result)        