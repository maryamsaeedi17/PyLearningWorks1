import qrcode

name=input("Please enter your name:")
num=input("Please enter your phone number:")

q=qrcode.make(name + "-" + num)
q.save("name and number to qrcode.png")
