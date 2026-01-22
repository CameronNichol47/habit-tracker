import json
from pathlib import Path
from datetime import date, timedelta

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

def remove_habit():
    list_habits()
    remove_num = input("Enter the number corresponding to the habit you want to remove: ")

    if not remove_num.isdigit():
        print("Invalid selection.")
        return
    
    idx = int(remove_num) - 1
    if idx < 0 or idx >= len(habits):
        print("Invalid selection.")
        return
    
    habit=habits[idx]

    confirm = input(f"Are you sure you want to delete '{habit['name']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return
    
    habits.pop(idx)

def list_habits():
    count = 1

    today = date.today().isoformat()

    if len(habits)==0:
        print("No habits currently, you can add habits by pressing 1")
    else:
        print("\n")
        for count, habit in enumerate(habits, start=1):
            if today in habit["completions"]:
                status = "✅ Done today"
            else:
                status = "❌ Not done"

            print(f"{count}. {habit['name']}")
            

def load_data():
    if not DATA_FILE.exists():
        return {"habits": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("data.json is empty/corrupted — starting fresh.")
        return {"habits": []}
      
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
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


def compute_streak(completions):
    if not completions:
        return 0
    
    completed_dates = set(
        date.fromisoformat(d) for d in completions
    )

    today=date.today()

    if today not in completed_dates:
        return 0
    
    streak=0
    current_day=today

    while current_day in completed_dates:
        streak+=1
        current_day-=timedelta(days=1)

    return streak


def show_streaks():
    for habit in habits:
        streak = compute_streak(habit["completions"])
        print(f"{habit['name']}: {streak}-day streak")


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
        print("5) Remove habit")
        print("6) Quit")

        choice = input("Enter (1–6): ").strip()

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
            remove_habit()
            data["habits"] = habits
            save_data(data)
        elif choice == "6":
            running = False
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 1–6.")


if __name__ == "__main__":
    main()