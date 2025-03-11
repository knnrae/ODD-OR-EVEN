def check_number(num):
    while True:
        num = int(input('Type any number. The computer will evaluate if it is either even or odd. '))
        if num % 2 == 0:
            print(num, 'is an even number')
        else:
            print(num, 'is an odd number')
            
check_number(18)