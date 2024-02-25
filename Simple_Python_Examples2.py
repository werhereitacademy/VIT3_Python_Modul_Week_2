"""Question1: Student Grades Processing
You need to write a Python program to process a student's grades. The program needs to perform the following functions:

Store information and notes for 10 students using a dictionary. Let each student have their name, surname and grades (Midterm, Final and Oral grades). For example:
students = {
"Ahmet Yilmaz" : [85,90,78]
"Mehmet Demir" : [92,88,76]
"Ayse Kaya" : [78,89,95]
}
1-Calculate each student's GPA and add it to the dictionary.

2-Find the student with the highest GPA and print it on the screen.

3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.

4-Sort the names in alphabetical order and print the sorted list on the screen.

5-Keep students with a GPA below 70 in a cluster (set)."""


students = {}
student_averages = {}
number_of_students = 3
student_names = ()
counter = 0

while counter < number_of_students:
    name = input("Please enter your name:")
    surname = input("Please enter your surname:")
    midterm_grade = int(input("Enter your midterm grade:"))
    final_grade = int(input("Enter your final grade:"))
    oral_grade = int(input("Enter your oral grade:"))
    average = (midterm_grade + final_grade + oral_grade) / 3
    full_name = name + " " + surname
    students[full_name] = [midterm_grade, final_grade, oral_grade]
    student_averages[full_name] = [round(average, 2)]
    student_names += (name,)
    counter += 1

max_grade = 1

for i, j in student_averages.items():
    if j[0] > max_grade:
        max_grade = j[0]

for i, j in student_averages.items():
    if j[0] == max_grade:
        print("Student with the highest grade:", student)

student_name_list = []

for name in student_names:
    student_name_list.append(name)

student_name_list.sort()
print("Student names in alphabetical order:", student_name_list)

low_averages = {}

for i, j in student_averages.items():
    if j[0] < 70:
        low_averages[i] = j

print("Students with averages below 70:", low_averages)


"""Question 2: Film Library Management System Project
Project Description: This project aims to create an application that will help the user manage their movie collection. Users can add, edit, delete movies and view their collection.

Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

Basic Functions:

1-Create a movie data by taking information such as movie name, director, release year and genre from the user and store it in a dictionary.

2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for whatever data they want to change about the movie.)

3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

4-Save the movie data in a file and restore this data when you start the program."""

class FilmLibrary(object):
    def __init__(self, film_title, director, release_year, genre):
        self.film_title = film_title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.film_collection = []
        self.film_info = {}
        self.film_info_file_name = "film_info.txt"

        self.film_info[film_title] = [director, release_year, genre]
        self.film_collection.append(film_title)
        self.update_film_file()

    def update_film_file(self):
        with open(self.film_info_file_name, "w") as film_info_file:
            for film_title, info in self.film_info.items():
                film_info_file.write(f"{film_title},{info[0]},{info[1]},{info[2]}\n")
            print("Film file updated.")

    def delete_film(self, film_title):
        with open(self.film_info_file_name, "r") as film_info_file:
            lines = film_info_file.readlines()

        with open(self.film_info_file_name, "w") as film_info_file:
            for line in lines:
                values = line.strip().split(',')
                if len(values) == 4:
                    file_film_title, _, _, _ = values
                    if file_film_title != film_title:
                        film_info_file.write(line)

        print("Film file updated.")

    def add_film(self):
        film_title = input("Enter the title of the film you want to add:\nPress `2` to go back: ")
        if film_title == "2":
            return
        else:
            director = input("Enter the director of the film: ")
            release_year = input("Enter the release year of the film: ")
            genre = input("Enter the genre of the film: ")

        self.film_info[film_title] = [director, release_year, genre]
        self.film_collection.append(film_title)
        print("Films in your collection:", self.film_collection)

        self.update_film_file()

    def add_to_collection(self):
        film_title = input("Enter the title of the film you want to add to your collection:\nPress `2` to go back: ")
        if film_title == "2":
            return
        else:
            self.film_collection.append(film_title)
            print("Updated film collection:", self.film_collection)

    def edit_film(self):
        film_title = input("Enter the title of the film you want to edit (Press '2' to go back): ")
        if film_title in self.film_collection:
            choice1 = input(
                "Press '1' to change the director, '2' to change the release year, '3' to change the genre: ")
            if choice1 == "1":
                new_director = input("Enter the new director's name: ")
                self.film_info[film_title][0] = new_director
            elif choice1 == "2":
                new_release_year = input("Enter the new release year: ")
                self.film_info[film_title][1] = new_release_year
            elif choice1 == "3":
                new_genre = input("Enter the new genre: ")
                self.film_info[film_title][2] = new_genre
            print("Saved film information:", self.film_info)
            self.update_film_file()
        elif film_title == "2":
            return
        else:
            print("Film not found.")

    def delete_film_entry(self):
        film_title = input("Enter the title of the film you want to delete:\nPress `2` to go back: ")

        if film_title in self.film_collection:
            self.delete_film(film_title)
            if film_title in self.film_info.keys():
                del self.film_info[film_title]
            print(film_title, "is being removed from your collection.")
            self.film_collection.remove(film_title)
        elif film_title == "2":
            return
        else:
            print("Film not found.")

        print(self.film_info)

    def view_collection(self):
        print("Films in your collection:", self.film_collection)

    def all_film_info(self):
        print("Saved film information:", self.film_info)



film_title = input("Enter the title of the film you want to save: ")
director = input("Enter the director of the film you want to save: ")
release_year = input("Enter the release year of the film you want to save: ")
genre = input("Enter the genre of the film you want to save: ")


f1 = FilmLibrary(film_title=film_title, director=director, release_year=release_year, genre=genre)


while True:
    choice = input(
        "To add a film, press '1'\n"
        "To edit film details, press '2'\n"
        "To delete a film, press '3'\n"
        "To view your collection, press '4'\n"
        "To only add to your collection, press '5'\n"
        "To view existing film information, press '6'\n"
        "To exit, press '7': ")
    if choice == "1":
        f1.add_film()
    elif choice == "2":
        f1.edit_film()
    elif choice == "3":
        f1.delete_film_entry()
    elif choice == "4":
        f1.view_collection()
    elif choice == "5":
        f1.add_to_collection()
    elif choice == "6":
        f1.all_film_info()
    elif choice == "7":
        print("Exiting the system.")
        break


"""Question 3: Customer Management System
Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.

2-Provide a menu where the user can choose the following actions:

Add new customer
Update customer information
delete customer
List all customers
check out
3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.

4-When updating customer information, view the current information using the customer ID and save the updated information.

5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.

6-In the process of listing all customers, view the list of existing customers.

7-Repeat the process until the user logs out."""

class CustomerManagementSystem:
    def __init__(self, id, name, surname, email, phone):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.customer_info = {}
        self.customer_names = {}
        choice = input("To save the entered information, press 1\nTo go back to the screen, press 2.")
        if choice == "1":
            self.customer_info[id] = [name, surname, email, phone]
            self.customer_names[id] = name
        elif choice == "2":
            return
        print(self.customer_info)
        print(self.customer_names)

    def add_new_customer(self):
        new_id = input("Enter the id for the new customer:\nTo go back to the previous page, press `2`:")
        if new_id == "2":
            return
        while new_id in self.customer_info.keys():
            print("The system already has the same id. Enter a new id:")
            new_id = input("Enter another id")

        new_name = input("Enter the name of the new customer:")
        new_surname = input("Enter the surname of the new customer:")
        new_email = input("Enter the email address of the new customer:")
        new_phone = input("Enter the phone number of the new customer:")
        self.customer_info[new_id] = [new_name, new_surname, new_email, new_phone]
        self.customer_names[new_id] = new_name

    def update_customer(self):
        choice1 = input(
            "Enter the id of the customer whose information you want to change:\nTo go back to the previous page, press `2`:")
        if choice1 == "2":
            return
        while choice1 not in self.customer_info.keys():
            choice1 = input("The entered id is not in the system. Please enter a new id")

        choice2 = input(
            "Which information of the customer do you want to change:\n For Name press `1`\nFor Surname press `2`\nFor Email press `3`\nFor Phone Number press `4`:")
        if choice2 == "1":
            new_name = input("Enter the new name you want to save in the system.")
            self.customer_info[choice1][0] = new_name
            self.customer_names[choice1] = new_name

        elif choice2 == "2":
            new_surname = input("Enter the new surname you want to save in the system.")
            self.customer_info[choice1][1] = new_surname

        elif choice2 == "3":
            new_email = input("Enter the new email you want to save in the system.")
            self.customer_info[choice1][2] = new_email

        elif choice2 == "4":
            new_phone = input("Enter the new phone number you want to save in the system.")
            self.customer_info[choice1][3] = new_phone

    def delete_customer(self):
        choice3 = input("Enter the id of the customer you want to delete.")
        while choice3 not in self.customer_info.keys():
            print("Id not found, enter again.")
            choice3 = input("Enter the id of the customer you want to delete again.")
        del self.customer_info[choice3]
        del self.customer_names[choice3]
        print("Updated customer names:", ",".join(i for i in self.customer_names.values()))

    def view_customers(self):
        return print(",".join(i for i in self.customer_names.values()))


id = "faltay"
name = "Furkan"
surname = "Altay"
email = "furkan@gmail.com"
phone = 683051515

c1 = CustomerManagementSystem(id=id, name=name, surname=surname, email=email, phone=phone)

while True:
    choice = input(
        "If you want to add a new customer to the system, press `1`\nIf you want to make changes to existing customer information, press `2`\nTo delete a customer, press `3`\nTo access customer names, press `4`\nTo exit, press `5`.")
    if choice == "1":
        c1.add_new_customer()
    elif choice == "2":
        c1.update_customer()
    elif choice == "3":
        c1.delete_customer()
    elif choice == "4":
        c1.view_customers()
    elif choice == "5":
        break
