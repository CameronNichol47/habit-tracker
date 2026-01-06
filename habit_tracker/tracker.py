def add_habit():
    print("TODO: add_habit()")


def list_habits():
    print("TODO: mark_done()")


def mark_done():
    print("TODO: mark_done()")


def show_streaks():
    print("TODO: show_streaks()")


def main():
    running = True

    while running:
        print("\n=== Habit Tracker ===")
        print("1) Add habit")
        print("2) List habits")
        print("3) Mark habit done today")
        print("4) Show streaks")
        print("5) Quit")

        choice = input("Enter (1–5): ").strip()

        if choice == "1":
            add_habit()
        elif choice == "2":
            list_habits()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            show_streaks()
        elif choice == "5":
            running = False
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()