def leetcode():
    print("TODO: Leetcode")

def gym():
    print("TODO: Gym")

def internships():
    print("TODO: Apply for internships")

def study():
    print("TODO: Study")


check = True
while check:
    choice = input(
        "\nLeetcode (1)\n"
        "Gym (2)\n"
        "Apply for Internships (3)\n"
        "Study (4)\n"
        "Quit (5)\n"
        "Enter: "
    ).strip()

    if choice == "1":
        leetcode()
    elif choice == "2":
        gym()
    elif choice == "3":
        internships()
    elif choice == "4":
        study()
    elif choice == "5":
        check = False
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1–5.")
