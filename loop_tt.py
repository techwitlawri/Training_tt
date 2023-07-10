if __name__=='__main__':
     sum_number=0
     while True:

        number=int(input('Enter Number: '))
        if number < 0:
            print(sum_number)
            break
        sum_number+= number