
"""
PROJECT EULER - PROBLEM 9 - Special Pythagorean Triplet

a < b < c
"""
import time

start_time = time.time()

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

print(time.time() - start_time)
    
    