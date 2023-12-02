class Solution:
    def myFunc(self, s: str):
        dc = {}
        for i in s:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1

        return dc
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for i in words:
            check = 0
            cur = self.myFunc(i)
            for j in cur:
                if cur[j] <= chars.count(j):
                    check = 1
                else:
                    check = 0
                    break
            if check == 1:
                result += len(i)
        return result

        