import random
import os
import time

if __name__=='__main__':
   
   number_of_guesses= 5
   score = 0
   money = 100
   print('''This is a guessing game,
         All you have to do guess a number, 
         and if you guess correctly,
         you win a point.''')
   print(' let play!!!')

   while True:
   
      secret_number = random.randint(1, 10)
      
      guess_number= int(input('Enter The Secret Number: '))
  
    
      if guess_number == secret_number:
         score += 1
         print(f'you guessed it right score is {score}')
         print(f'You just earned \u20A6{money:.2f}')
         option = input(f'''Guess again to earn \u20A6{money * 3:.2f}
   type yes to guess again or no to end and walk away with {money}
   input: ''')
        
         if option.lower() == 'yes':
            continue
         elif option.lower()=='no':
            print('Goodbye🤨🤔🙄')
            print(f'You went home with\u20A6{money:.2f}')
            break
         else:
            print('Are you dumb?')
            break
      else:
         if number_of_guesses == 0:
            print('you did not win the game')
            break
         
         
         number_of_guesses -= 0
         print('You guessed wrong')
         print(f'Your score is {score}')
         print(f'You earned {money - 100:.2f}')

      time.sleep(2)
      os.system('cls')
         
        
    
    