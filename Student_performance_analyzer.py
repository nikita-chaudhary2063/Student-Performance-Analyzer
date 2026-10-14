'''Write a Python program that analyzes students' marks and prints a complete report
Requirements
1. Print every student's marks using a loop.
2. Count how many students passed (marks >= 40) and failed (marks < 40).
3. Calculate the total marks.
4. Calculate the average marks.
5. Find the highest and lowest marks without using max() or min().
6. Count how many students scored above the average.
7. Count how many students scored even marks and odd marks using %.
8. Count how many students scored at least 80.
9. Print the final report in a clean format.'''

marks = [78, 35, 92, 40, 56, 28, 85, 67]
count_passed=0
count_failed=0

for i in marks:
    if i>=40:
        count_passed+=1
    elif i<40:
        count_failed+=1

total_marks=0
average_marks=0 
for i in marks:
    total_marks+=i
    average_marks=total_marks/len(marks)

highest_marks=marks[0]
lowest_marks=marks[0]
for i in marks:
    if i>highest_marks:
        highest_marks=i
    elif i<lowest_marks:
        lowest_marks=i

count_above_average=0
count_below_average=0
for i in marks:
    if i>average_marks:
        count_above_average+=1
    elif i<average_marks:
        count_below_average

count_even_numbers=0
count_odd_numbers=0
for i in marks:
    if i%2==0:
        count_even_numbers+=1
    else:
        count_odd_numbers+=1

count_atleast_80marks=0
for i in marks:
    if i>=80:
        count_atleast_80marks+=1

print("Total students:",len(marks))
print("Total passed students:",count_passed)
print("Total failed students:",count_failed)
print("Total marks:",total_marks)
print("Average marks:",average_marks)
print("Highest marks:",highest_marks)
print("Lowest marks:",lowest_marks)
print("Student who scored above average:",count_above_average)
print("Student who scored below average:",count_below_average)
print("Even marks:",count_even_numbers)
print("Odd marks:",count_above_average)
print("Student who scores above or atleast 80:",count_atleast_80marks)