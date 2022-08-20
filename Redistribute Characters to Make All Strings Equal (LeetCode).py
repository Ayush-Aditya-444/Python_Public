from collections import Counter
def ayush(words):
    str1="".join(words)
    str1=list(str1)    
    dict1=Counter(str1)
    int1=dict1[str1[0]]
    for x,y in dict1.items():
        if y!=int1:
            return False
    return True
words = ["abc","aabc","bc"]
a=ayush(words)
print(a)