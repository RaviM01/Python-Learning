# Author: Ravi
# Desc: Description of the Test module
# Date: 21/09/2017
import random
print('\033[1m')
'''
Question 1:
Create a guessing game. Allow the user to input a number. Test to see if there guess is right. If it is wrong then ask if they want to guess again. Repeat until they either get the answer the right number or until they say no when asked if they wish to retry.
Type casting may be necessary.
num_1 ="77.77"
num_2= "12.3 4"
total= float( num_1 ) + (float ) num_2
'''
secret = random.randint(1, 10)
allow = 'Y'

while (allow == 'N'):
    print('Guess number between 1 to 10:')
    guess = int(input(''))
    if (guess == secret):
        print('You guessed it correctly')
        break
    else:
        print('Try Again: ')
        print('You want to continue to guess: ')
        allow = input('')

'''
Question 2:
Read in 5  book titles and value s. After each title and value is read in display the values and produce a running total of the cost
BookTitle1 Cost Running Total
'''
bookDetailList = []
for i in range(1,6):
    print('Input Book title:')
    title = input('')
    print('Input cost of the book:')
    cost = float(input(''))
    bookDetailList.append([title, cost])
total_cost = 0.0
print('{0:<75s}{1:<5s} {2:<13s}'.format('Title','Cost', 'Total Cost'))
print('_'*100)
for entry in bookDetailList:
    total_cost +=  entry[1]
    print('{0:<70s}{1:10.2f}{2:10.2f}'.format(entry[0], entry[1], total_cost))
print('_'*100)

