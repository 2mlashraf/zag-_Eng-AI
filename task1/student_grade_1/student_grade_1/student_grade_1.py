'''
def grade(marks):
    if marks>= 90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"
    #fun to display details
    def display(student_data,index):
        print (f"{index}.Name:{student_data['name']} | Subject:{student_data['subject']} | marks:{student_data['marks']} | Grade:{student_data['grade']}")
    #fun to validate if the name contains only letters
    def is_valid_name(name):
        return name.isalpha()
    #main to input and store student data 
    def main():
        student=[] #list to store student records
        while True:
            student_name = input("Enter Student Name :)")
            while not is_valid_name(student_name):
                print ("Invalid name :( / Enter a name containing only letters.")
                student_name = input("Enter student name: ")
    #get subject name 
    subject = input ("Enter subject: ")
    #get marks and validate input
    while True:
        try:
            marks =int (input("Enter marks: "))
            if marks <0 or marks >100:
                print ("Marks should be between 0 and 100. :) Enter again")
            else:
                break
        except ValueError:
            print("Invalid input :( Enter a valid number for marks .")
             #calc the grade
    grade = calculate_grade(marks)

    #store student data 
    student_data={
        'name': student_name,
        'subject':subject,
        'marks':marks,
        'grade':grade
        }
    #add the student`s data to the students list
    students.append(student_data)

    # ask if wants to add another student
    another = input("Do you want to add another student ?(yes/no): ").lower()
    if another != 'yes':
        break
        
   

    
    #Display all studends` records
    print("\n---student records---")
    for i,student in enumerate(student,1):
        display_student(student,i)

        main()
'''
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# fun to display details 
def display(student_data, index):
    print(f"{index}. Name: {student_data['name']} | Subject: {student_data['subject']} | Marks: {student_data['marks']} | Grade: {student_data['grade']}")

#fun to validate if the name contains only letters
def is_valid_name(name):
    return name.isalpha()

#main to input and store student data  
def main():
    students = []  # list to store students_data
    while True:
      
        student_name = input("Enter student name: ")
        while not is_valid_name(student_name):
            print("Invalid name! Please enter a name containing only letters.")
            student_name = input("Enter student name: ")

        # get subject name
        subject = input("Enter subject: ")

        #get marks and validate input 
        while True:
            try:
                marks = int(input("Enter marks: "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100. Please enter again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number for marks.")

        #calc the grade 
        grade = calculate_grade(marks)

        # store student data
        student_data = {
            'name': student_name,
            'subject': subject,
            'marks': marks,
            'grade': grade
        }

        # add the student`s data to the students list
        students.append(student_data)

        # ask if wants to add another student
        another = input("Do you want to add another student? (yes/no): ").lower()
        if another != 'yes':
            break

    # Display all studends` records
    print("\n--- Student Records ---")
    for i, student in enumerate(students, 1):
        display(student, i)


main()
