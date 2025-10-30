

def sort(width, height, length, mass):
    # Checks for invalid input for values
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return "INVALID_INPUT: Dimensions and mass must all be positive values."
        
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = (
        volume >= 1000000 or 
        width >= 150 or 
        height >= 150 or 
        length >= 150
    )
    
    # Determine if package is heavy
    is_heavy = mass >= 20

    # Sort Stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
        

print("--Test Cases--")
# 1. STANDARD
print(sort(10, 10, 10, 5))      

# 2. SPECIAL (Heavy only)
print(sort(10, 10, 10, 20))   

# 3. SPECIAL (Bulky by Volume only)
print(sort(100, 100, 100, 15)) 

# 4. SPECIAL (Bulky by Dimension only)
print(sort(150, 1, 1, 15))     

# 5. REJECTED (Heavy AND Bulky)
print(sort(150, 1, 1, 20))

#6. INVALID INPUT 
print(sort(0,150,100,20))
