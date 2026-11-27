import random
import time
from datetime import datetime

# ---------- DATA ----------

quotes = {
    "motivation": [
        "Small progress is still progress.",
        "Your future depends on what you do today.",
        "Consistency beats motivation.",
        "Every expert was once a beginner.",
        "Don't compare your journey with others.",
        "Believe in yourself and keep moving forward.",
        "Success begins with the decision to try."
    ],

    "success": [
        "Success starts with self-discipline.",
        "Dream big, work hard, stay focused.",
        "Great things take time.",
        "Believe in your ability to improve.",
        "Your efforts will create opportunities.",
        "Work hard in silence, let success make the noise.",
        "Every accomplishment begins with a decision."
    ],

    "confidence": [
        "Trust yourself. You are capable of more than you think.",
        "Be proud of how far you have come.",
        "Confidence grows when you keep trying.",
        "Your mistakes are proof that you are learning.",
        "Don't be afraid to start something new."
    ]
}

study_tips = {
    "Programming": [
        "Write code yourself instead of only reading it.",
        "Break complex problems into smaller steps.",
        "Practise debugging your own programs.",
        "Understand the logic before writing syntax.",
        "Practise one coding problem every day."
    ],

    "Theory": [
        "Make short notes in your own words.",
        "Use diagrams to understand concepts.",
        "Revise topics at regular intervals.",
        "Explain concepts without looking at notes.",
        "Connect new concepts with real-life examples."
    ],

    "Exams": [
        "Practise previous question papers.",
        "Understand important concepts first.",
        "Attempt questions within a time limit.",
        "Revise formulas and definitions regularly.",
        "Test yourself instead of only rereading."
    ]
}

challenges = [
    "Solve one coding problem today.",
    "Learn five new technical terms.",
    "Revise one difficult topic.",
    "Explain one concept to a friend.",
    "Learn a new keyboard shortcut.",
    "Read for 20 minutes without distractions.",
    "Write a short summary of today's learning.",
    "Complete one pending task.",
    "Learn something new outside your syllabus.",
    "Organize your study materials."
]

study_hours = 0.0
completed_challenges = []


# ---------- FUNCTIONS ----------

def show_quote():
    print("\nCHOOSE QUOTE CATEGORY")
    print("1. Motivation")
    print("2. Success")
    print("3. Confidence")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        category = "motivation"
    elif choice == "2":
        category = "success"
    elif choice == "3":
        category = "confidence"
    else:
        print("Invalid choice!")
        return

    print("\n🌟", random.choice(quotes[category]))


def show_study_tip():
    print("\n===== CHOOSE SUBJECT =====")
    print("1. Programming")
    print("2. Theory")
    print("3. Exams")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        subject = "Programming"
    elif choice == "2":
        subject = "Theory"
    elif choice == "3":
        subject = "Exams"
    else:
        print("Invalid choice!")
        return

    print("\n📚", random.choice(study_tips[subject]))


def give_challenge():
    challenge = random.choice(challenges)

    print("\n🎯 Today's challenge:")
    print(challenge)

    answer = input("\nDid you complete it? (yes/no): ").lower()

    if answer == "yes":
        completed_challenges.append(challenge)
        print("Excellent work! Keep going.")
    elif answer == "no":
        print("No problem. Try again when you're ready.")
    else:
        print("Please enter yes or no.")


def start_study_session():
    global study_hours

    try:
        minutes = int(input("Enter study duration in minutes: "))

        if minutes <= 0:
            print("Enter a positive number.")
            return

        print("\nStudy session started!")
        print("Focus on your work. Good luck!")

        time.sleep(minutes * 60)

        study_hours += minutes / 60

        print("\nSession completed! Great work.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    print("\n====== YOUR PROGRESS ======")

    print("Date:", datetime.now().strftime("%d-%m-%Y"))
    print("Total study hours:", round(study_hours, 2))
    print("Challenges completed:", len(completed_challenges))

    if completed_challenges:
        print("\nCompleted challenges:")

        for challenge in completed_challenges:
            print("-", challenge)
    else:
        print("\nNo challenges completed yet. Start today!")


# ---------- MAIN MENU ----------

while True:

    print("\nCAMPUS SURVIVAL KIT")


    print("1. Get a motivational quote")
    print("2. Get a study tip")
    print("3. Daily productivity challenge")
    print("4. Start study session")
    print("5. View my progress")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        show_quote()

    elif choice == "2":
        show_study_tip()

    elif choice == "3":
        give_challenge()

    elif choice == "4":
        start_study_session()

    elif choice == "5":
        show_progress()

    elif choice == "6":
        print("\nThanks for using Campus Survival Kit!")
        print("Keep learning and keep growing!")
        break

    else:
        print("\nInvalid choice! Please select between 1 and 6.")