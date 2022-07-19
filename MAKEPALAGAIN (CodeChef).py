input_str1="aabbaa"
input_str1=list(input_str1)
count1=0
for i in range(len(input_str1)):
    if input_str1.count(input_str1[i])%2==0:
        continue
    elif input_str1.count(input_str1[i])%2==1:
        count1+=1
if count1>=2:
    print("NO")
else:
    print("YES")