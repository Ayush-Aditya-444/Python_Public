from collections import Counter
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(suits)==suits.count(suits[0]):
            return "Flush"
        dict1=Counter(ranks)
        for x,y in dict1.items():
            if y>=3:
                return "Three of a Kind"
        for x,y in dict1.items():
            if y==2:
                return "Pair"
        return "High Card"