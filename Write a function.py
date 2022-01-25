def is_leap(year):
    if year%4==0 and year%100!=0:
        leap=True
    elif year%400==0:
        leap=True
    else:
        leap = False
    # Write your logic here
    
    return leap

year = int(input())