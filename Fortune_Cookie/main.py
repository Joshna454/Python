import random 

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number==1:
    fortune_text = 'You will have a great day!'
if fortune_number==2:
    fortune_text = 'You will have a tough day!'
if fortune_number==3:
    fortune_text = 'you will be successfull!'

print(f'{fortune_text} Your lucky number is: {lucky_number}')




#expected_output
#you will be successfull! Your lucky number is: 90
#You will have a great day! Your lucky number is: 67
