#Boolean Funtions 

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
      return False
    
is_divisible(6,4) #-->False
is_divisible(6,3) #--True

def is_divisible(x,y):
    return x % y == 0
  
    if is_divisible(x,y):
       print('x is divisible by y')
        
    if is_divisible(x,y) == True:
       print('x is divisible by y')
