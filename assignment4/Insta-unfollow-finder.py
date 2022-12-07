import instaloader
import getpass

f=open("followers.txt" , "r")
old_followers=[]

for line in f:
    old_followers.append(line.strip())

f.close()

L=instaloader.Instaloader()

username=input("Please enter usernam:")
password=getpass.getpass("Please enter password:")

L.login(username,password)

print("✨You are already logged in.✨")

profile=instaloader.Profile.from_username(L.context,"m.saeedi.kh")

new_followers=[]

for follower in profile.get_followers():
    new_followers.append(follower.username)

print("Your current followers:")
for new_follower in new_followers:
    print(new_follower)

if new_followers==[]:
    print("No followers!!!🤷‍♀️")

unfollowers=[]
print("These accounts have unfollowed you:")
for old_follower in old_followers:
    if old_follower not in new_followers:
        unfollowers.append(old_follower)
        print(old_follower)

if unfollowers==[]:
    print("No one has unfollowed you!👌✨")        

f=open("followers.txt" , "w") 
for follower in new_followers:
    f.write(follower +"\n")
f.close()              