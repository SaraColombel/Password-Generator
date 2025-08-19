import string, random

characterList = ""
allowedPunctuation = "%#!*$?"

length = int(input("Choose the length of your password please : "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

while(True):
    choice = int(input("Pick a number : "))
    if choice == 1 :
        characterList += string.digits
    elif choice == 2 :
        characterList += string.ascii_letters
    elif choice == 3 :
        characterList += allowedPunctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option !")

if not characterList:
    print("No character set selected, password cannot be generated.")
    exit()

password = "".join(random.choice(characterList) for _ in range(length))


print("Your new password is : " + password)