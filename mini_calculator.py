
import math
print ("="*25)
print("__________________mini calculator____________")
print ('='*25)
print('1.addition')
print('2.substract')
print('3.multiply')
print('4.division')
print('5. factor')
print('6. lcm')
print("7. hcf")
print('8. square')
print('9.power')
print('10. square root')
num = int(input('enter your choice'))
if num == 1 :
    a = int(input('enter a number '))  
    b = int(input(' enter a second number'))
    print('sum is ', a+b)
elif num == 2 :
    a = int(input('enter a number '))  
    b = int(input(' enter a second number'))   
    print('sub is  ', a- b) 

elif num == 3 :
    a = int(input('enter a number '))  
    b = int(input(' enter a second number'))
    print('mul is ', a*b)
elif num == 4 :
    a = int(input('enter a number '))  
    b = int(input(' enter a second number'))    
    if b == 0:
        print('cannot divide by zero')
    else :    
          print('div is ', a/b)
elif num == 5:
    a = int(input('enter number to find factor'))   
    print(f'factor is {math.factorial(a)}')
elif num == 6:
    a = int(input('enter a number to find lcm'))       
    b = int(input('enter  anumber'))    
    print(f"lcm is{math.lcm(a,b)}")
elif num == 7:
    a = int(input('enter a number to find hcf'))
    b = int(input('enter a number ')) 
    print(f'hcf is {math.gcd(a,b)}')
elif  num == 8:
    a = int(input('enter a number to find square'))  
    print("sqaure is ", a*a)
elif num == 9:
    a = int(input('enter a number to find power')) 
    b = int(input('enter a power '))   
    print(f'power is {math.pow(a,b)}')
elif num == 10:
    a = int(input('entern a number'))
    print(f'square root is {math.sqrt(a)}')


