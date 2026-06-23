import csv
import os
import statistics
import sys


def main():
    options = {
        "1.": "Add Student",
        "2.": "View All Students",
        "3": " Search Student",
        "4": "Class Average",
        "5.": "Exit",
    }
    print("=== Student Grade Tracker ===")
    for key, value in options.items():
        print(f"{key} : {value}")
    while True:
          userInput = input("\n Enter Option : ").strip()
          if userInput == "1":
              add_student()
          elif userInput == "2":
              view_students()
          elif userInput == "3":
              search_students()
          elif userInput == "4":
              get_avarage()
          elif userInput == "5":
              sys.exit("Thank You")
          else:
              print("please provide a valid option")




def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            students = list(reader)

            students = sorted(
                students,
                key=lambda student: int(student["Grade"]),
                reverse=True
            )

            for student in students:
                print(student["Name"], student["Grade"])

    except FileNotFoundError:
        print("File does not exist")

def search_students():
    name = get_name()
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            found = False
            for lines in reader:
                if name in lines.values():
                    print(f"{lines["Name"]} | {lines["Grade"]} ")
                    found = True 

            if not found:
                print(f"{name} does not exist")
    except FileNotFoundError:
        print("File does not exist")


def add_student():

    name = get_name()
    grade = get_grade()

    student_info = {"Name": name, "Grade": grade}

    if os.path.exists("students.csv"):
        with open("students.csv", "a", newline="") as file:
            writter = csv.DictWriter(file, fieldnames=["Name", "Grade"])
            writter.writerow(student_info)
            print("operation successfull")
    else:
        with open("students.csv", "w", newline="") as file:
            writter = csv.DictWriter(file, fieldnames=["Name", "Grade"])
            writter.writeheader()
            writter.writerow(student_info)
            print("operation successfull")


def get_avarage():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        items = []
        for line in reader:
            grade = line.get("Grade")
            grade = int(grade)
            items.append(grade)
        average = statistics.fmean(items)
        print(f"The avarage mark of all students is {average:.2f}")


def get_name():

    while True:
        userinput = input("enter name : ").strip().lower()
        if userinput.isalpha():
            userinput = userinput.capitalize()

            return userinput
        else:
            print("name should contain only letters")


def get_grade():
    while True:
        userinput = input("enter grade : ").strip().lower()
        if userinput.isdigit():
            userinput = int(userinput)
            if 0 <= userinput <= 100:
                return userinput
            else:
                print("grade should be between 0 and 100")
        else:
            print("grade should be a number ")


if __name__ == "__main__":
    main()
