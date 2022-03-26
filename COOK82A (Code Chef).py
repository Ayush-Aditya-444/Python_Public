T=int(input())
for i in range (0,T):
    team=dict(input().split(" ") for x in range(4))
    rm=int(team.get("RealMadrid"))
    b=int(team.get("Barcelona"))
    m=int(team.get("Malaga"))
    e=int(team.get("Eibar"))
    if (rm<m and b>e):
        print("Barcelona")
    else:
        print("RealMadrid")   