
if __name__=='__main__':
  products=["Gucci" ,"Dior", "Burberry", "Chanel", "Fendi", "Ysl"]
  price_tags=[ "\u20A6 7000", "\u20A6 9000" ,"\u20A6 4000", "\u20A6 5000", "\u20A6 8000" ,"\u20A6 10000 "]
  quantities = [2,7,6,9,3,8]
  bag = []
  price_tag = []
  quantity =0
  total = 0

  
  print("Welcome to 'Loreal Store' ")
  print('products available are as follow: Gucci, Dior, Burberry, Chanel, Fendi, Ysl')
  item = True
  while item ==True:

    brand = input('Enter a Brand: ').capitalize()
    if brand == "Gucci":
      bag.append(products[0])
      price_tag.append(price_tags[0])
      quantity=quantity +1
      
      
    elif brand =="Dior":
      bag.append(products[1])
      price_tag.append(price_tags[1])
      quantity=quantity +1
     
    
    elif brand == "Burberry":
      bag.append(products[2])
      price_tag.append(price_tags[2])
      quantity= quantity +1
     
    elif brand == "Chanel":
      bag.append(products[3])
      price_tag.append(price_tags[3])
      quantity= quantity +1
      
    elif brand == "Fendi" :
      bag.append(products[4])
      price_tag.append(price_tags[4])
      quantity=quantity +1
      
    elif brand == "Ysl":
      bag.append(products[5])
      price_tag.append(price_tags[5])
      quantity= quantity +1
      
    else:
      print('Sorry not availiable')
    done = input("Are you done? : ('y for yes or n for no : ')")
    if done == 'n':
      item = True
    else: 
      item = False
    print("   ")
    print("item" + str(bag))
    print("cost" + str (price_tag))
    print(quantity)
    print("Thank you for shoping with us!!!")
    print(total)