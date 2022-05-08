import math
T=int(input())
for i in range(T):
    N,V1,V2=map(int,input().split())
    Elevator_Distance=N*2
    Stairs_Distance=N*math.sqrt(2)
    Time_Elevator=Elevator_Distance/V2
    Time_Stairs=Stairs_Distance/V1
    if Time_Stairs>Time_Elevator:
        print('Elevator')
    else:
        print('Stairs')