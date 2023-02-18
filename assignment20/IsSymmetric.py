print("Step 1: Getting the array")

array=[]
l=0
j=0

while True:

    data=input("Please enter array data or type end to end:")
    if data=="end":
        break

    else:
        array.append(data)
        l=l+1

print("Step 2: Checking for symmetry")

for i in range(l//2):
    if array[i]==array[(i+1)*(-1)]:
        j+=1

if j==l//2:
    print("Result: The array is symmetric.")
else:
    print("Result: The array is not symmetric.")
    