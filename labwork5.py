print('Welcome to the quiz game')
print('Answer the following questions')
score = 0
# question_one
print('''what is the name of your instrutor?
1) Mr Solomon
2) Mr David''')
answer1=input('Enter answer: ')
if answer1 == '1':
  print('Correct')
  score += 1
  print(f'your score {score}')
else:
  print('incorrect')
# question_two
print('''What is the Capital of Lagos? 
1) Ikeja
2) ayobo''')
answer2= input('Enter Answer: ')
if answer2 == 'Ikeja':
  print('correct')
  score += 1
  print(f'your score{score}')
else:
  print('incorrect') 
  #  question_three
print('How many eyes do you have? ')
answer3= input('Enter Answer: ')
if answer3== 'Two' or '2' :
    print('correct')
    score += 1
else:
  print('incorrect')
  #question_four
print('how many colours are there in the rainbom?')
answer4= input('Enter answer: ')
if answer4=='7':
    print('correct')
    score += 1
else:
    print('incorrect')

print(score)
print('Thank You For Playing!!!')
