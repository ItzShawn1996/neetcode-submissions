class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)    #mapping char count to list of anagrams

        for str in strs:
            count = [0] * 26

            for c in str:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(str)

        return list(res.values())