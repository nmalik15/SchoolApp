main_database = {
    "students": [
        {"first_name": "John", "last_name": "Smith", "class": "3C"},
        {"first_name": "Anna", "last_name": "Purple", "class": "3C"},
        {"first_name": "Jan", "last_name": "Kowalski", "class": "4E"},
    ],
    "teachers": [
        {"first_name": "Milos", "last_name": "Forman", "subject": "math", "classes": ["3C", "4E"]},
    ],
    "homeroom_teachers": [
        {"first_name": "Jan", "last_name": "Kowalski", "class": "3C"},
    ]
}

def show_class(database, class_id):
    print("Students: ")
    for student in database["students"]:
        if student["class"] == class_id:
            print(f"- {student["first_name"]} {student["last_name"]}")

    print("Homeroom Teachers: ")
    for homeroom_teacher in database["homeroom_teachers"]:
        if homeroom_teacher["class"] == class_id:
            print(f"- {homeroom_teacher["first_name"]} {homeroom_teacher["last_name"]}")


def create_student(database, first_name, last_name, class_id):
    student_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "class": class_id
        }
    database["students"].append(student_dict)
    return database

def create_teacher(database, first_name, last_name, subject, class_id):
    teacher_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "subject": subject,
            "class": class_id
        }
    database["teachers"].append(teacher_dict)
    return database

def create_homeroom_teacher(database, first_name, last_name, class_id):
    homeroom_teacher_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "class": class_id
        }
    database["homeroom_teachers"].append(homeroom_teacher_dict)
    return database

while True:
    print("\n1. Create Users\n2. Manage Users\n3. End")
    main_choice = input("Choose an action: ")

    if main_choice == "1":
        while True:
            print("\n1. Create Student\n2. Create Teacher\n3. Create Homeroom Teacher\n4. End")
            command = input("\nChoose an action: ")
            
            # create a new student in class
            if command == "1":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                class_id = input("Class: ")
                main_database = create_student(main_database, first_name, last_name, class_id)

            # create a new teacher
            elif command == "2":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                subject = input("Subject taught: ")
                class_id = input("Class: ")
                main_database = create_teacher(main_database, first_name, last_name, subject, class_id)
            
            # create a new homeroom teacher
            elif command == "3":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                class_id = input("Class: ")
                main_database = create_homeroom_teacher(main_database, first_name, last_name, class_id)
            
            elif command == "4":
                print("Going back to main menu.")
                break

            else:
                print("Invalid Command!")

    if main_choice == "2":
        command = input("Data to print: ")

    # list all students in class and the homeroom teacher
    if command == "class":
        class_id = input("Provide class id: ")
        show_class(main_database, class_id)



    elif command == "debug":
        print(main_database)        

    elif command == "exit":
        break
    else:
        print("Invalid command!")