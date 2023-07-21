 
x = int(input("Enter an integer: ")) 
y = int(input("Enter an integer: ")) 
if(x + y == 0): 
    print("Division by zero error. |(x - y)| / (x + y) can't be evaluated.") 
else: 
    print("|(x - y)| / (x + y) = ", abs(x - y) / (x + y))

    
