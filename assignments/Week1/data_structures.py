# Author: Ravi
# Desc: Data structures
# Date: 28/09/2017

# Lists
print ('List data structure')
print('-'*80)
student_details_list=[]
#student_name, staudent_grade
student_details_list.append(['Ravi', 75.00])
student_details_list.append(['Sankar', 80.00])
for student_detail in student_details_list[0:len(student_details_list)]:
    print('{0} {1}'.format(student_detail[0], student_detail[1]))
    student_detail[0] = str(student_detail[0]).upper()
for index in range(0, len(student_details_list)):
    print('{0} {1}'.format(student_details_list[index][0], student_details_list[index][1]))
print (list(map (lambda rec: {str(rec[0]).upper()}, student_details_list)))
print('-'*80)
print ('Tuple data structure')
print('-'*80)
# Tuples
student_details_list=(('Ravi', 75.00),('Sankar', 80.00))
#student_name, staudent_grade
for student_detail in student_details_list[0:len(student_details_list)]:
    print('{0} {1}'.format(student_detail[0], student_detail[1]))
    #student_detail[0] = str(student_detail[0]).upper()
for index in range(0, len(student_details_list)):
    print('{0} {1}'.format(student_details_list[index][0], student_details_list[index][1]))
print('-'*80)
print ('List nested inside Tuple data structure')
print('-'*80)
student_details_list=(['Ravi', 75.00],['Sankar', 80.00])
#student_name, staudent_grade
for student_detail in student_details_list[0:len(student_details_list)]:
    print('{0} {1}'.format(student_detail[0], student_detail[1]))
    student_detail[0] = str(student_detail[0]).upper()
for index in range(0, len(student_details_list)):
    print('{0} {1}'.format(student_details_list[index][0], student_details_list[index][1]))

print('-'*80)
print ('Tuple nested inside List data structure')
print('-'*80)
student_details_list=[]
#student_name, staudent_grade
student_details_list.append(('Ravi', 75.00))
student_details_list.append(('Sankar', 80.00))
for student_detail in student_details_list[0:len(student_details_list)]:
    print('{0} {1}'.format(student_detail[0], student_detail[1]))
    #student_detail[0] = str(student_detail[0]).upper()
for index in range(0, len(student_details_list)):
    print('{0} {1}'.format(student_details_list[index][0], student_details_list[index][1]))
print (list(map (lambda rec: {str(rec[0]).upper()}, student_details_list)))
print('-'*80)
print('Shallow Copy')
print('-'*80)
