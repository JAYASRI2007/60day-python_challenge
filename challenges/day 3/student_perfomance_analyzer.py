original_marks =[]
updated_marks = []
valid_count = 0
fail_count = 0
reg = int(input("enter your registration number :"))
if reg % 2 == 0 :
    bonus = 2
else:
    bonus = 1
n = int(input ("enter number of students :"))
for i in range(n):
    mark_input=int(input("enter marks :"))
    original_marks = original_marks + [mark_input]
for mark in original_marks:
        if mark<0 or mark>100:
           category = "Invalid"
           updated_marks = updated_marks + [mark]
        else:
          valid_count = valid_count +1
          processed_mark = mark+bonus 
          updated_marks = updated_marks + [processed_mark]
          if processed_mark >= 90:
            category = "Execellent"
          elif processed_mark >= 75:
            category = " Very Good"
          elif processed_mark >= 60:
            category = "Good "
          elif processed_mark >= 40:
            category = "Averange"
          else:
            category = "Fail"
            fail_count = fail_count + 1
        print("Mark : " ,(mark),  ":" , category)
print("Original Marks List :", original_marks )
print( "updated Marks List :" ,updated_marks )
print("Total Valid students :", valid_count )
print("Total Failed students :", fail_count)

 