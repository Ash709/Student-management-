import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ASH@1234562003",  # Replace with your MySQL password
    database="school"
)
cursor = conn.cursor()


def add_student():
    id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO students (id, name, marks) VALUES (%s, %s, %s)", (id, name, marks))
    conn.commit()
    print("Student added successfully.")


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


def update_student():
    id = int(input("Enter Student ID to update: "))
    marks = int(input("Enter new marks: "))
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (marks, id))
    conn.commit()
    print("Student record updated.")

def delete_student():
    id = int(input("Enter Student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (id,))
    conn.commit()
    print("Student record deleted.")

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


cursor.close()
conn.close()
