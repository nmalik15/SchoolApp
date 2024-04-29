main_database = {
    "students": [
        {"first_name": "John", "last_name": "Smith", "class": "3C"},
        {"first_name": "Anna", "last_name": "Purple", "class": "3C"},
        {"first_name": "Leo", "last_name": "Cap", "class": "4E"},
    ],
    "teachers": [
        {"first_name": "Milos", "last_name": "Forman", "subject": "math", "classes": ["3C", "4E"]},
    ],
    "homeroom_teachers": [
        {"first_name": "Jan", "last_name": "Kowalski", "class": "3C"},
    ]
}

def divider():
    print ("*" * 35)

def show_class(database, class_id):
    print("\nStudents: ")
    for student in database["students"]:
        if student["class"] == class_id:
            print(f"- {student["first_name"]} {student["last_name"]}")

    print("\nHomeroom Teachers: ")
    for homeroom_teacher in database["homeroom_teachers"]:
        if homeroom_teacher["class"] == class_id:
            print(f"- {homeroom_teacher["first_name"]} {homeroom_teacher["last_name"]}")


def show_student(database, first_name, last_name):
    for student in database["students"]:
        if student["first_name"] == first_name and student["last_name"] == last_name:
            print(f"Student {first_name} {last_name} attends class {student['class']}")
            print(f"\nTeachers teaching class {student['class']}:")
            # target_class = student['class']
            # print(target_class)
            for teacher in database["teachers"]:
                if student['class'] in teacher["classes"]:
                    print(f"- {teacher['first_name']} {teacher['last_name']}")
            return

    print(f"Student {first_name} {last_name} not found.")

def show_homeroom_teacher(database, first_name, last_name):
    for homeroom_teacher in database["homeroom_teachers"]:
        if homeroom_teacher["first_name"] == first_name and homeroom_teacher["last_name"] == last_name:
            print(f"Homeroom teacher {first_name} {last_name} leads class {homeroom_teacher['class']}")
            print("Student's list:")
            for student in database["students"]:
                if student["class"] == homeroom_teacher["class"]:
                    print(f"{student['first_name']} {student['last_name']}")


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
    divider()
    print("WELCOME TO SCHOOL MANAGEMENT SYSTEM")
    divider()
    print("\n1. Create Users\n2. Manage Users\n3. End")
    main_choice = input("\nChoose an action: ")

    if main_choice == "1":
        while True:
            divider()
            print("USER CREATION".center(35, " "))
            divider()
            print("\n1. Create Student\n2. Create Teacher\n3. Create Homeroom Teacher\n4. Back to Main Menu")
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
                print("Going back to main menu...")
                break

            else:
                print("Invalid Command!")

    elif main_choice == "2":
        while True:
            divider()
            print("USER MANAGEMENT".center(35, " "))
            divider()
            print("\n1. Manage Class\n2. Manage Student\n3. Manage Teacher\n4. Manage Homeroom Teacher\n5. Back to Main Menu")
            command = input("\nChoose an action: ")

            # list all students in class and the homeroom teacher
            if command == "1":
                class_id = input("Provide class id: ")
                show_class(main_database, class_id)

            # list all students in class and the homeroom teacher
            elif command == "2":
                print("Student search: ")
                first_name = input("Provide first name: ")
                last_name = input("Provide last name: ")
                show_student(main_database, first_name, last_name)

            # list all classes teacher teach
            elif command == "3":
                class_id = input("Provide class id: ")
                show_class(main_database, class_id)
                
            # list all students in the class of the homeroom teacher
            elif command == "4":
                print("Homeroom teacher search: ")
                first_name = input("Provide first name: ")
                last_name = input("Provide last name: ")
                show_homeroom_teacher(main_database, first_name, last_name)

            # back to main menu
            elif command == "5":
                print("Going back to main menu...")
                break

            else:
                print("Invalid Command!")

    # elif command == "debug":
    #     print(main_database)        

    elif main_choice == "3":
        print("Goodbye!")
        break

    else:
        print("OY!!! Invalid command!")