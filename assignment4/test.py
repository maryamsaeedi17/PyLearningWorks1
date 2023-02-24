import qrcode

data=[]

name=input("Please enter your name:")
num=input("Please enter your phone number:")

data.append(name)
data.append(num)

q=qrcode.make(data)
q.save("datann.png")

