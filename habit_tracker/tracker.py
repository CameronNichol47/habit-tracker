import json
from pathlib import Path
from datetime import date

DATA_FILE = Path("data.json")
habits=[]

def add_habit():
    not_dupe=True
    new_habbit = input("\nAdd habbit name: ").strip()
    if not new_habbit:
        print("No empty habits")
        return
    
    for i in habits:
        if (i['name'].lower() == new_habbit.lower()):
            print("No duplicate habbits")
            new_habbit=""
            not_dupe=False
            break

    if not_dupe:
        habits.append({
            "name": new_habbit,
            "completions": []
        })
        print(f"Added: {new_habbit}")

def list_habits():
    count = 1
    if len(habits)==0:
        print("No habits currently, you can add habits by pressing 1")
    else:
        print("\n")
        for count, habit in enumerate(habits, start=1):
            print(f"{count}. {habit['name']}")


def load_data():
    if not DATA_FILE.exists():
        return {"habits": []}
    
    with open(DATA_FILE, "r") as f:
        return json.load(f)
      

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
        
def mark_done():
    if not habits:
        print("No habits currently")
        return
    
    list_habits()
    choice = input("Select habit number: ").strip()

    try:
        idx = int(choice) - 1
        habit = habits[idx]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    today = date.today().isoformat()

    if today in habit["completions"]:
        print("Already marked done today.")
        return
    
    habit["completions"].append(today)
    print(f"Marked '{habit['name']}' done for {today}.")

def show_streaks():
    print("TODO: show_streaks()")


def main():
    running = True

    data=load_data()
    global habits
    habits=data["habits"]

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
            data["habits"]=habits
            save_data(data)
        elif choice == "2":
            list_habits()
        elif choice == "3":
            mark_done()
            data["habits"] = habits
            save_data(data)
        elif choice == "4":
            show_streaks()
        elif choice == "5":
            running = False
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()