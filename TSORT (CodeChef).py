# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

lis=[]
t=int(input())
while t>0:
    n=int(input())
    lis.append(n)
    t-=1
lis.sort()
for i in range(0,len(lis)):
    print(lis[i])



