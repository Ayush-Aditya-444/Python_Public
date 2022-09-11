class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
		
        for word in strs:
            curr = ''.join(sorted(word))
            mapp[curr].append(word)
			
        res = []
        for k,v in mapp.items():
            res.append(v)

        return res