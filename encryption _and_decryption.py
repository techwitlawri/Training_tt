import string
def encrypt():
  letter= ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"]
  key = string.punctuation + " "
  letter = list(letter)
  key= list(string.punctuation)
  encrypted_message =' '
  
  # print(f"letter: {letter}")
  # print(f"char: {key}")
#Encrypt
    

  try:
      text=input('Enter Message to Encrypt: ')

      encrypted_message=' '
      for letter in text:
          
          encrypted_message +=key(letter)
          print(f"original message: {text}")
          print( f'Encrypted message: {encrypted_message}')
          
         
         
          decryted_message = ""
          for letter in text:
          
           decryted_message == encrypted_message
           
           print( f'Encrypted message: {encrypted_message}')
          

  except:
      print('nothing')
  
if __name__=='__main__':
       encrypt()
                                                                                                                                                                                                                                                                                                                                                              
     
 
            

    
