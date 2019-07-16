class Employee:
    number_of_objects = 0


    def __init__(self, first_name, last_name, email, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.monthly_salary = salary
        Employee.number_of_objects += 1

    def get_annual_salary(self):
        return self.monthly_salary * 12


    def show_employee_information(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Pracownik: {full_name}, Adres email: " 
              f"{self.email}, Wynagrodzenie miesieczne: " 
              f"{self.monthly_salary}")


employee_1 = Employee("Jan", "Kowalski", "jankowalski@wp.pl", 3000)

employee_2 = Employee("Oliwia", "Nowak", "oliwianowak@gmail.com", 2800)


print(employee_1.get_annual_salary())
employee_1.show_employee_information()

print("-----------------")

print(employee_2.get_annual_salary())
employee_2.show_employee_information()

print(f"Liczba pracowników: {Employee.number_of_objects}")