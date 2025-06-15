#Main.py 

def star_marker():
    print("*"*100)

def main():
    choice = 0
    while True:
        star_marker()
        print("Hi John What you want to do with your shedule , These are your options : ")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Show all Tasks")
        print("4. Exit")
        choice = int(input("Enter your Choice Agent John : "))
        if choice == 1:
            star_marker()
            pass
            print("Task added to Schedule")
        elif choice == 2:
            star_marker()
            pass
            print("Task removed")
        elif choice == 3:
            star_marker()
            print("These are your Task which you have decided to perform today")
            pass
        elif choice == 4:
            print("Exited from Task Menu")
            break
        else:
            print("Enter Valid Choice! Try Again....")

if __name__ == "__main__":
    main()