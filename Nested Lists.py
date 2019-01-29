#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format

#The first line contains an integer, , the number of students. 
#The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

#Constraints

#There will always be one or more students having the second lowest grade.


marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))



##CONCLUSION##
#There are  students in this class whose names and grades are assembled to build the following list:
#python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
