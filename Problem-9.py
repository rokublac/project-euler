
"""
PROJECT EULER - PROBLEM 9 - Special Pythagorean Triplet

https://projecteuler.net/problem=9
"""

def checkPythagorean(a,b,c):
    if (a**2) + (b**2) == c**2:
        return True
    return False

def main():
    result = 1000
    
    for i in range(1,1000):
        for j in range(i+1,1000): 
            c = result - (i + j)
            if checkPythagorean(i,j,c):
                print (i*j*c)
                print (i,j,c)
                break

main()

    
    
