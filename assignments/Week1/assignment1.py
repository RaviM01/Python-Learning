'''
Question 1:
Store the following statement in a variable named python_mission.
The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers

    Count the number of appearances of the letter s.
    Find the second instance of the word Python which occurs somewhere after position 25.
    Selection structures and loops should not be used. Your answer should only use string methods.
    What value is returned from the statement
    print(The word returned is: {}.format(python_mission[25:34]))
    Find out if the word 'diverse' is in the mission statement using two different methods
    Check if the string 12345 is a number
    Print out the following directory structure as a string
    C:\\users\\rlennon\\python3\\python-3.5.1\\bin
    '''
python_mission= '''The mission of the Python Software Foundation is to promote, protect,
and advance the Python programming language, and to support and facilitate
the growth of a diverse and international community of Python programmers'''
print('\033[1m')
print('python_mission = '+python_mission)
print('')
print('Question 1:')

print ('\t number of appearances of the letter s: ' + str(python_mission.count('s')))
index = python_mission.find('Python', 25)
print('\t The second instance of the word Python occurs at index: '+ str(index))
print('\t "The word returned is: {}".format(python_mission[25:34])) is evaluated as: '+'The word returned is: {}'.format(python_mission[25:34]))
print('\t Word diverse existence check using find(): '+str(python_mission.find('diverse')))
print('\t Word diverse existence check using index(): '+str(python_mission.index('diverse')))
print('\t\t Note: index() method throws error if target string is not exists')
print('\t 12345 is a Number: '+ str('12345'.isnumeric()))
print('\t '+ r'C:\users\rlennon\python3\python-3.5.1\bin')


'''
Question 2:
From the python_mission string indicated in the previous question find the last instance of the word
Python. Use only string methods and variables to carry out this task. Do not use loops or selection
structures.
'''
print('')
print('Question 2:')
print('\t last instance of the word Python in python_mission strings is : '+ str(python_mission.rfind('Python')))

'''
Question 3:
Given the variable suffix_no with a value of 1122. Build an LYIT student number. The number should
begin with an L and be followed by 8 digits. Where the suffix_no is less than 8 the string should be
padded with zero’s to a final size of 8. Use only string methods and variables to carry out this task. Do
not use loops or selection structures. Modify your answer to take in the suffix_no from the user.
'''

print('')
print('Question 3:')
print('\t Input student number:')
#suffix_no='1234'
suffix_no = input('')
suffix_no = suffix_no.rjust(8, '0').rjust(9,'L')
print('\t LYIT student number: '+suffix_no)


'''
Question 4:
Assume that the following is a single line taken from a *Nix password file. Separate out each field into
the appropriate variables using the slice operator.
rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash
Repeat the process using the split operator
'''
print('')
print('Question 4:')
record= 'rlennon:x:1234:1001:Ruth Lennon:/users/rlennon:/bin/bash'
print('\t Separating the fields using slicing operator:')
username= record[0:7]
id_1 = record[8:9]
id_2 = record[10:14]
id_3 = record[15:19]
full_name = record[20:31]
user_home = record[32:46]
user_bin = record[47:]
print('\t ' + username+ '\t ' + id_1+ '\t ' + id_2+'\t ' + id_3+ '\t ' + full_name+ '\t ' + user_home+'\t ' + user_bin)
print('\t Separating the fields using split operator:')
username,id_1,id_2, id_3,full_name,user_home,user_bin = record.split(':')
print('\t ' + username+ '\t ' + id_1+ '\t ' + id_2+'\t ' + id_3+ '\t ' + full_name+ '\t ' + user_home+'\t ' + user_bin)
