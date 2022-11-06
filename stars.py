'''This task aims to draw a patern of stars countinouslly 
'''
#1st triangle
import time
import os
os.system("CLS")
rows =int(input("enter your numer of rows to draw a patern "))  #number of rows
for i in range(0, rows):             # nested loop for each column
    for j in range(0, i + 1):        # nested loop for each column
        print("*", end=' ')          # print star
    print(" ")  	                 # new line after each row
print("\n")
time.sleep(1)

#2nd triangle

k = 2 * rows -2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
print("\n")
time.sleep(1)

#3rd triangle

k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print(" ")	
print("\n")
time.sleep(1)

#4th triangle

for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
print("\n")
time.sleep(1)

#5th triangle
m = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")
print("\n")
time.sleep(1)

#6th triangle
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
time.sleep(1)
print("\n")
