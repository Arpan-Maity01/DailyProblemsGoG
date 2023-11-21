class Solution:
    List= [42,11,1,97] 
    def reverse(self, n: int) -> int:
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            n //= 10
        return r

    def countNicePairs(self, nums: List[int]) -> int:
        def mod_pow(a, b, mod):
            result = 1
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % mod
                a = (a * a) % mod
                b //= 2
            return result

        rev_diff_count = defaultdict(int)
        nice_pairs = 0
        mod_value = 10**9 + 7

        for num in nums:
            rev_diff = num - self.reverse(num)
            nice_pairs = (nice_pairs + rev_diff_count[rev_diff]) % mod_value
            rev_diff_count[rev_diff] += 1

        return nice_pairs