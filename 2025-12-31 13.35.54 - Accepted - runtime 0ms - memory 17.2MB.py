class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        multiplier = 1
        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * multiplier)
            n //= 10
            multiplier *= 10
        return result[::-1]  # Reverse for descending order