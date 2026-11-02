from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Frequency count array for 'a' through 'z'
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Tuples are immutable and can be used as dictionary keys
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())