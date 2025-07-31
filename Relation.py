'''if set A = Z+(set of positive integers)
a relation is defined as 
xRy such that 3x+4y is divisibly by 7,
 Program to check if this relation is symmetric'''

def is_relation_symmetric(limit):
    not_symmetric_pairs = []
    
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if (3*x + 4*y) % 7 == 0:  # xRy holds
                if (3*y + 4*x) % 7 != 0:  # check if yRx fails
                    not_symmetric_pairs.append((x, y))
    
    if not not_symmetric_pairs:
        return True
    else:
        return not_symmetric_pairs

# Example: Check first 50 positive integers
result = is_relation_symmetric(10)

if result == True:
    print("The relation is symmetric.")
else:
    print("The relation is not symmetric for these pairs:")
    print(result)
