import random

random_array=[]

n=int(input("Please enter a number less than 20: "))

while n>20:
    n=int(input("Please enter a true number (less than 20): "))


for i in range(n):
    random_num=random.randint(-100,100)

    while random_num in random_array:
        random_num=random.randint(-100,100)

    random_array.append(random_num)

print("\n")
print("Your random array is: ", random_array)        
        