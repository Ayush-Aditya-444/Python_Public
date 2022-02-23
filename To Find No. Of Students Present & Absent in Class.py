a=int(input("Total No. Of Students In Class: "))
print("""For Every Student Present Press "P" & For Absent Press "A" """)
c=0
d=0
for i in range(a):
    b=input()
    if b=="P":
        c+=1
    else:
        d+=1
print(f"No. Of Students Present {c} & No. Of Students Absent {d}")