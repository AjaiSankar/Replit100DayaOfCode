
print("EXAM GRADE CALCULATOR")
print("-------------------------")

exam = input("Name of Exam: ")
max = int(input("Maximun Possible marks: "))
mark = float(input("Marks obtained: "))

perc = round((mark/max)*100);

print("Percentage: ",perc)

if perc >= 90 and perc <=100:
  print("Grade: A+")
elif perc >= 80 and perc <=89:
  print("Grade: A")
elif perc >= 70 and perc <=79:
  print("Grade: B")
elif perc >= 60 and perc <=69:
  print("Grade: C")
elif perc >= 50 and perc <=59:
  print("Grade: D")
else:
  print("Grade: U")
