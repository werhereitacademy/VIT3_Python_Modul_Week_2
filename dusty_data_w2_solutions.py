# Student Grades Projects
# Store information and notes of 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Viva grades).

students = {
    'Simon Hoeve': [85, 90, 78],
    'Joshua Winkel': [79, 65, 72],
    'Aylin Yazici': [75, 90, 82],
    'Karen Yilmaz': [84, 72, 83],
    'Ahu Baysal': [96, 67, 88],
    'Jip Holte': [65, 80, 72],
    'Janneke Groot': [88, 68, 92],
    'John Karizma': [45, 67, 75],
    'Elif Winkie': [86, 79, 74],
    'Kerem Salman': [68, 42, 78] 
}

# Calculate each student's GPA and add it to the dictionary.

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    students[student].append(avg_grade)



# Finding the student with the highest average grade and print screen

highest_avg_grade_student = max(students, key=lambda x: students[x][-1])

print("En yüksek not ortalamasına sahip öğrenci:", highest_avg_grade_student)
print("Not ortalaması:", students[highest_avg_grade_student][-1])

# Separate each student's name from their surname and store them in a separate tuple and add them to a list.

student_names = [(student.split()[0], student.split()[1]) for student in students]


# Sort the names alphabetically and print the sorted list to the screen.

sorted_student_names = sorted(student_names)

print("Sıralanmış öğrenci adları:")
for name in sorted_student_names:
    print(name[0], name[1])


# Keep students with GPA below 70 in a cluster (set).

below_70_set = {student for student, grades in students.items() if grades[-1] < 70}

print("Not ortalaması 70'in altında olan öğrencilerin kümesi:", below_70_set)

# Film Collection Management

# Create a dictionary to store the film collection
film_collection = {}

# Add a new film
def add_film():
    film_name = input("Enter the film name: ")
    director = input("Enter the director: ")
    release_year = input("Enter the release year: ")
    genre = input("Enter the genre: ")

    film = {
        'Film Name': film_name,
        'Director': director,
        'Release Year': release_year,
        'Genre': genre
    }

    film_collection[film_name] = film
    print(f"{film_name} added to the collection.")

# Edit a film
def edit_film(film_name):
    if film_name in film_collection:
        print(f"Editing {film_name}...")
        new_data = {}
        new_data['Film Name'] = input(f"New film name ({film_collection[film_name]['Film Name']}): ")
        new_data['Director'] = input(f"New director ({film_collection[film_name]['Director']}): ")
        new_data['Release Year'] = input(f"New release year ({film_collection[film_name]['Release Year']}): ")
        new_data['Genre'] = input(f"New genre ({film_collection[film_name]['Genre']}): ")

        film_collection[film_name] = new_data
        print(f"{film_name} updated.")
    else:
        print(f"{film_name} not found in the collection.")

# Delete a film
def delete_film(film_name):
    if film_name in film_collection:
        del film_collection[film_name]
        print(f"{film_name} deleted from the collection.")
    else:
        print(f"{film_name} not found in the collection.")

# View the collection
def view_collection():
    print("\nFilm Collection:")
    for film_name, data in film_collection.items():
        print(f"Film Name: {data['Film Name']}")
        print(f"Director: {data['Director']}")
        print(f"Release Year: {data['Release Year']}")
        print(f"Genre: {data['Genre']}")
        print("-" * 30)

while True:
    print("\nFilm Collection Management")
    print("1. Add Film")
    print("2. Edit Film")
    print("3. Delete Film")
    print("4. View Collection")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_film()
        
    elif choice == '2':
        film_name = input("Enter the film name to edit: ")
        edit_film(film_name)
       
    elif choice == '3':
        film_name = input("Enter the film name to delete: ")
        delete_film(film_name)
        
    elif choice == '4':
        view_collection()
        
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid option! Please try again.")


# Customer Management System

# Using a dictionary structure to store customer information. Assigning a unique customer identification (ID) for 
# each customer and associate customer information with this ID. Using a dictionary containing information 
# such as name, surname, e-mail, phone number for each customer

customers = {}

def add_customer(customer_id, name, surname, email, phone_number):
    customers[customer_id] = {
        'name' : name,
        'surname' : surname,
        'email' : email,
        'phone_number' : phone_number
    }

    print("Customer added successfully!")

def get_customer_info(customer_id):
    return customers.get(customer_id, None)

def update_customer(customer_id, name=None, surname=None, email=None, phone_number=None):
    if customer_id in customers:
        if name:
            customers[customer_id]['name'] = name
        if surname:
            customers[customer_id]['surname'] = surname
        if email:
            customers[customer_id]['email'] = email
        if phone_number:
            customers[customer_id]['phone_number'] = phone_number
        print("Customer information updated successfully.")
    else:
        print("Customer ID not found.")

def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        print("Customer deleted successfully.")
    else:
        print("Customer ID not found")

def list_all_customers():
    if customers:
        print("List of all customers: ")
        for customer_id, customer_info in customers.items():
            print(f"Customer ID: {customer_id}, Name: {customer_info['name']}, Surname: {customer_info['surname']}, Email: {customer_info['email']}, Phone Number : {customer_info['phone_number']}")
    else:        
        print("No customers found.")

# 2-Providing a menu where the user can choose the following actions:
#Add new customer
#Update customer information
#delete customer
#List all customers
#check out


def menu():
    while True:
        print("\nCustomer Management System")
        print("1.Add new customer")
        print("2.Update customer information")
        print("3.Delete customer")
        print("4.List all customers")
        print("5.Check out")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            surname = input("Enter customer surname: ")
            email = input("Enter customer email: ")
            phone_number = input("Enter customer phone number: ")
            add_customer(customer_id, name, surname, email, phone_number)
        elif choice == '2':
            customer_id = int(input("Enter customer ID to update: "))
            name = input("Enter updated name (press Enter to skip): ")
            surname = input("Enter updated surname (press Enter to skip): ")
            email = input("Enter updated email (press Enter to skip): ")
            phone_number = input("Enter updated phone number (press Enter to skip): ")
            update_customer(customer_id, name, surname, email, phone_number)
        elif choice == '3':
            customer_id = int(input("Enter customer ID to delete: "))
            delete_customer(customer_id)
        elif choice == '4':
            list_all_customers()
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()




