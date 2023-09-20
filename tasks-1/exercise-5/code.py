def calculate_factorial(n):
    fack = 1
    if n == 1:
        return fack
    elif n < 0: 
        return None    
    else: 
        for i in range(n):
            fack *= (i+1)
        return fack
