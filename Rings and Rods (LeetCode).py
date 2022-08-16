class Solution:
    def countPoints(self, rings: str) -> int:
        blue=[]
        green=[]
        red=[]
        for i in range(len(rings)):
            if "B"==rings[i]:
                blue.append(rings[i+1])
            elif "R"==rings[i]:
                red.append(rings[i+1])
            elif "G"==rings[i]:
                green.append(rings[i+1])
        blue=set(blue)
        green=set(green)
        red=set(red)
        count1=blue.intersection(red)
        count2=count1.intersection(green)
        return len(count2)