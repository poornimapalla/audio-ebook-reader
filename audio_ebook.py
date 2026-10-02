import pyttsx3

# Create text-to-speech engine
engine = pyttsx3.init()

# E-book chapters
chapters = {
    1: {
        "title": "Introduction to Python",
        "content": """
Python is a high-level programming language.
It is simple, easy to learn, and widely used.
Python is used in web development, data science,
artificial intelligence, machine learning, and automation.
"""
    },

    2: {
        "title": "Features of Python",
        "content": """
Python has a simple and readable syntax.
It is an interpreted programming language.
Python supports object-oriented programming.
It has many built-in libraries and frameworks.
Python is also used for artificial intelligence and data analysis.
"""
    },

    3: {
        "title": "Applications of Python",
        "content": """
Python is used in many areas.
It is used for web development using Django and Flask.
It is used for data analysis using Pandas.
It is used for artificial intelligence and machine learning.
Python is also useful for automation and scripting.
"""
    }
}


# Display chapters
def view_chapters():
    print("\n========== AVAILABLE CHAPTERS ==========")

    for number, chapter in chapters.items():
        print(number, ".", chapter["title"])


# Read complete e-book
def read_complete_book():
    print("\nReading complete e-book...")

    for number, chapter in chapters.items():

        print("\nReading Chapter", number)
        print(chapter["title"])

        engine.say(chapter["title"])
        engine.say(chapter["content"])

        engine.runAndWait()


# Read selected chapter
def read_chapter():
    view_chapters()

    choice = input("\nEnter chapter number: ")

    if not choice.isdigit():
        print("Please enter a valid chapter number.")
        return

    chapter_number = int(choice)

    if chapter_number not in chapters:
        print("Chapter not found!")
        return

    chapter = chapters[chapter_number]

    print("\n========== CHAPTER ==========")
    print("Title:", chapter["title"])
    print(chapter["content"])

    print("\nReading chapter...")

    engine.say(chapter["title"])
    engine.say(chapter["content"])

    engine.runAndWait()


# View chapter content without reading
def view_chapter():
    view_chapters()

    choice = input("\nEnter chapter number: ")

    if not choice.isdigit():
        print("Please enter a valid chapter number.")
        return

    chapter_number = int(choice)

    if chapter_number not in chapters:
        print("Chapter not found!")
        return

    chapter = chapters[chapter_number]

    print("\n========== CHAPTER CONTENT ==========")
    print("Title:", chapter["title"])
    print(chapter["content"])


# Main menu
while True:

    print("\n==========================================")
    print("          AUDIO E-BOOK READER")
    print("==========================================")
    print("1. View Chapters")
    print("2. Read Complete E-book")
    print("3. Read Selected Chapter")
    print("4. View Chapter Content")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_chapters()

    elif choice == "2":
        read_complete_book()

    elif choice == "3":
        read_chapter()

    elif choice == "4":
        view_chapter()

    elif choice == "5":
        print("\nThank you for using Audio E-book Reader!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 5.")