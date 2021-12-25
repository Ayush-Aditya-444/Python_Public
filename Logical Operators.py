print("Logical Operators In Python:-")
print("Example:-")
Has_High_Income=True
Has_Good_Credits=True
Has_A_Criminal_Record=False

if Has_High_Income and Has_Good_Credits:
    print("He Is Eligible For Loan")
elif Has_High_Income or Has_Good_Credits:
    print("May Be He Is Not Eligible For Loan")
if Has_High_Income and not Has_A_Criminal_Record:
    print("He Is Eligible For Loan")