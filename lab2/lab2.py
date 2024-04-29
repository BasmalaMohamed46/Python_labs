import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lab2"
)


cursor = db_connection.cursor()

cursor.execute(
    """create table employee(
            id INT UNIQUE NOT NULL PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL,
            age int NOT NULL,
            department char(55),
            salary int NOT NULL,
            managed_department char(55) DEFAULT NULL
            );"""
)
db_connection.commit()

class Employee:

    __all_employees=[]
    @classmethod
    def get_employees(cls):
        return cls.__all_employees

    @classmethod
    def get_employee_count(cls):
        return len(cls.__all_employees)
    @classmethod
    def get_last_employee_id(cls):
        if cls.get_employee_count() == 0:
            return 0
        return cls.get_employees()[-1].id
    @classmethod
    def get_employee_by_id(cls, emp_id):
        for emp in cls.__all_employees:
            if emp.id == emp_id:
                return emp
        return None
    def __init__(self,id,first_name,last_name,age,department,salary):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.department=department
        self.salary=salary
        Employee.get_employees().append(self)

        cursor.execute("""insert into employee(id,first_name,last_name,age,department,salary) values(%s,%s,%s,%s,%s,%s)""",(self.id,self.first_name,self.last_name,self.age,self.department,self.salary))
        db_connection.commit()
  

    def transfer(self, new_department):
        
        self.department = new_department

        cursor.execute("UPDATE employee SET department = %s WHERE id = %s", (self.department, self.id))

        db_connection.commit()

    def fire(self):
        
        Employee.get_employees().remove(self)

        cursor.execute("DELETE FROM employee WHERE id = %s", (self.id,))

        db_connection.commit()

    def show(self):
        print(f"ID: {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @classmethod
    def list_employee(cls):
        cursor.execute("SELECT * FROM employee")
        data_of_employees = cursor.fetchall()
        for data in data_of_employees:
           print(
                f"ID: {data[0]}\nFirst Name: {data[1]}\nLast Name: {data[2]}\nAge: {data[3]}\nDepartment: {data[4]}\nSalary: {data[5]}\n"
           )

class Manager(Employee):
    def __init__(self,id, first_name, last_name, age, department, salary, managed_department):
        super().__init__(id,first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        cursor.execute("UPDATE employee SET managed_department = %s WHERE id = %s", (self.managed_department, self.id))
        db_connection.commit()

    def show(self):
        print(f"ID: {self.id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Managed Department: {self.managed_department}")
        print("Salary: Confidential")

def add_employee():
    id = Employee.get_last_employee_id()+ 1
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    department = input("Department: ")
    salary = int(input("Salary: "))
    role = input("Are you a manager (m) or an employee (e): ").lower()
    if role == 'm':
        managed_department = input("Enter Managed Department: ")
        employee = Manager(id,first_name,last_name, age, department, salary, managed_department)
    else:
        employee = Employee(id, first_name,last_name, age, department, salary)
    print("Employee added successfully.")

def transfer_employee():
    id = int(input("Enter Employee ID: "))
    new_department = input("Enter New Department: ")
    employee = Employee.get_employee_by_id(id)
    employee.transfer(new_department)
    print("Employee transferred successfully.")

def fire_employee():
    id = int(input("Enter Employee ID: "))
    employee = Employee.get_employee_by_id(id)
    employee.fire()
    print("Employee fired successfully.")

def show_one_employee():
    id = int(input("Enter Employee ID: "))
    employee = Employee.get_employee_by_id(id)
    employee.show()


def menu_print():
    print("Employee Management System Menu:")
    print("1. Add New Employee")
    print("2. Transfer Employee")
    print("3. Fire Employee")
    print("4. List All Employees")
    print("5. Show Employee")
    print("6. Exit")

def main():
    while True:
        menu_print()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            transfer_employee()
            pass
        elif choice == '3':
            fire_employee()
            pass
        elif choice == '4':
            Employee.list_employee()
            pass
        elif choice == '5':
            show_one_employee()
            pass
        elif choice == '6':
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

db_connection.close()




                  