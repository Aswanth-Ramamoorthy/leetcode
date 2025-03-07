from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list = defaultdict(list)
        for i in strs:
            sorted_strs = ''.join(sorted(i))
            anagrams_list[sorted_strs].append(i)
        return list(anagrams_list.values())
        