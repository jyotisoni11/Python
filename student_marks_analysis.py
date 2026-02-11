#student_marks_analysis.py
#this program analyzes student marks and calculates:
# average, highest, lowest, pass count, and pass percentage.

marks = [34,50,89,76,89]
def avg_marks(data):
    """calculate average marks."""
    return sum(data) /len(data)
  

def find_max(data):
    """find highest marks."""
    return max(data)


def find_min(data):
    """find lowest marks."""
    return min(data)


def pass_count(data):
    """count number of student who passed(>=50)."""
    count = 0
    for m in data:
        if m >= 50:
            count += 1
    return count


def pass_percentage(data):
    """calculate pass percentage."""
    passed = 0
    for m in data:
        if m >= 50:
            passed += 1
    return (passed /len(data)) *100        


#  ---- taking input from user -----

marks= []
n = int(input("enter number of student: "))

for i in range(n):
    mark = int(input(f"enter marks for student {i+1}:"))
    marks.append(mark)

# ----Display Result -----
print("-----student marks analysis ----")    
print("Average marks: ", avg_marks(marks))
print("Highest marks: ",find_max(marks))
print("Lowest marks: ",find_min(marks))
print("passed student: ",pass_count(marks))
print("pass percentage: ",pass_percentage(marks),"%")




































































