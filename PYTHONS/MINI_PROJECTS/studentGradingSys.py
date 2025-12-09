name = str(input("enter the name of student:"))
symbol_no = int(input("enter the symbol number:"))
ds = float(input("enter marks in discrete structure:"))
oop = float(input("enter marks in OOPS:"))
mp = float(input("enter marks in Microprocessor:"))
math = float(input("enter marks in Mathematics:"))
stats = float(input("enter marks in Statistics:"))
def marks(mark):
    percent = float(mark/60)*100
    if percent>=85:
        return 4.0
    elif percent<85 and percent>=80:
        return 3.7
    elif percent<80 and percent>=75:
        return 3.3
    elif percent<75 and percent>=70:
        return 3.0
    elif percent<70 and percent>=65:
        return 2.7
    elif percent<65 and percent>=60:
        return 2.3
    elif percent<60 and percent>=55:
        return 2.0
    elif percent<55 and percent>=50:
        return 1.7
    elif percent<50 and percent>=45:
        return 1.3
    elif percent<45 and percent>=40:
        return 1.0
    else:
        return 0
    
marks_ds = marks(ds)

marks_oop = marks(oop)

marks_mp = marks(oop)

marks_math = marks(math)

marks_stats = marks(stats)

weightedGPA_ds = marks_ds*3
weightedGPA_oop = marks_oop*3
weightedGPA_mp = marks_mp*3
weightedGPA_math = marks_math*3
weightedGPA_stats = marks_stats*3

total_weighted = weightedGPA_ds + weightedGPA_oop + weightedGPA_mp + weightedGPA_math + weightedGPA_stats

total_credit = 15

print("------------result--------------")

print(f"Name: {name}")
print(f"Symbol_no.: {symbol_no}")

print(f"subject\t\t\tGPA\t\tCredit_Hr\t\tWeighted_gpa")

print(f"Discrete structure\t{marks_ds}\t\t3\t\t\t{weightedGPA_ds:.2f}")

print(f"OOPs\t\t\t{marks_oop}\t\t3\t\t\t{weightedGPA_oop:.2f}")

print(f"Microprocessor\t\t{marks_mp}\t\t3\t\t\t{weightedGPA_mp:.2f}")

print(f"Mathematics\t\t{marks_math}\t\t3\t\t\t{weightedGPA_math:.2f}")

print(f"Statistics\t\t{marks_stats}\t\t3\t\t\t{weightedGPA_stats:.2f}\n")

SGPA = (total_weighted/total_credit)
print(f"the total cgpa {name} obtained is {SGPA:.2f}")
percentage = ((ds+oop+mp+math+stats)/300)*100
print(f"total percentage is {percentage:.2f}")

