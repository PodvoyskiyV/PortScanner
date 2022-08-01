import pyfiglet

banner = pyfiglet.figlet_format("Heart")
print(banner)

Flag = True

while(Flag):
    x = int(input("Enter number of centimetres : "))

    if x <= 0:
        print("Try one more time")
    else:
        Flag = False

print(x)