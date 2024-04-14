class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        r = {}
        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted in r:
                r[word_sorted].append(word)
            else:
                r[word_sorted] = [word]
        return list(r.values())
