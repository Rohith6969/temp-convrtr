print ("C to F or F to C ? Enter 1 (C to F) or 2 (F to C)")
o = input()

if o=='1':
    print ("Enter amount in Celsius:") 
    
    c = float(input())
    f = (c * 9/5) + 32
    print ( c,"in Fahrenheit is",f  )
    print ("Made by Rohith :-)")
    
    
if o=='2': 
    print ("Enter amount in Fahrenheit:")    
    j = float(input())
    k = ((j - 32)*5)/9
    print ( j,"in Celsius is",k  )
    print ("Made by Rohith :-)")
