#!/usr/bin/env python3
def fun2(n): 
    if(n == 0): 
        return
      
    fun2(n // 2) 
    print(n % 2, end="") 
	
n=int(input("Enter the number : "))
print("Binary equivalent of {} is : ".format(n),end="")
fun2(n)
print()
