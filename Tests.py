import pyfiglet

banner = pyfiglet.figlet_format("Heart")
print(banner)

Flag = True

while(Flag):
    try:
        x = int(input("Enter number of centimetres : "))

        if x <= 0:
            print("You should enter number large 0. Try one more time")
        else:
            Flag = False
    except ValueError:
        print("You should enter number. Try one more time")

print(x)
