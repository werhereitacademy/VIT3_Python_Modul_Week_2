'''Question1: Student Grades Processing
You need to write a Python program to process student grades. The program should perform the following functions:

Use a dictionary to store the information and grades of 10 students. Each student should have a name, surname, and grades (Midterm, Final, and Oral grades).
'''

students = {
    'Aysima Coskun':  [90, 85, 75],
    'Suheyb Coskun':  [35, 60, 50],
    'Guluzar Coskun': [68, 88, 78],
    'Derya Seker': [65, 87,86],
    'Gamze Yilmaz': [78, 88, 78],
    'Ahmet Furkan': [88, 66, 56],
    'Elif SEN': [78, 58, 88],
    'Ender Yilmaz': [77, 88, 67],
    'Dilan Demir': [99, 88, 77],
    'Duygu Seker': [69, 88, 78]
}

#1-Calculate the average grade for each student and add it to the dictionary.

def calculate_average(grades):
    return sum(grades) / len(grades)

names = students.keys()

for name in names:
    #I assigned both the grades and the average to variables for later use.
    
    student_grades = students[name]
    average = int(calculate_average(student_grades))
    students[name] = {'average': average, 'grades': student_grades}
print(students)

#2-Find and print the student with the highest average grade.

highest_average_grade = 0
student_with_highest_average_grade = ""

for name in students:
    average = students[name]['average']
    if average > highest_average_grade:
        highest_average_grade = average
        student_with_highest_average_grade = name
print("Student with the highest average grade: {}".format(student_with_highest_average_grade))



#3-Separate each student's name and surname and store them in a separate tuple, then add them to a list.


list_of_tuple_names = []
for name in students:
    name_list = tuple(name.split())
    list_of_tuple_names.append(name_list)
print(list_of_tuple_names)
    

#4-Sort the names in alphabetical order and print the sorted list.

print(sorted(names))
    
#5-Store the students with an average grade below 70 in a set.

set_of_students = set([])
for name in students:
    if students[name]['average'] < 70 :
        set_of_students.add(name)
    
print(set_of_students)




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





# Customer Management System

# Project Description: This project involves creating a customer management system that you can use to manage your customers and perform basic operations. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers, and listing customers. Here are the basic steps of the project:

customer_info = {}
customer_id = 1

while True:
    print("\n1. Add a new customer\n2. Update customer information\n3. Delete a customer\n4. List all customers\n5. Exit")
    
    choice = input("Please select an operation (1-5): ")
    if choice == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_info[customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
        customer_id += 1
        print(customer_info)
        
    elif choice == "2":
        print(customer_info)
        updated_customer_id = int(input("Customer ID to update: "))
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_info[updated_customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
    
        print ("Customer information updated!")
        print (customer_info)
        
    elif choice =="3":
        print(customer_info)
        deleted_customer_id = int(input("Customer ID to delete: "))
        del customer_info[deleted_customer_id]
        print("Your operation has been successfully completed.")
        print(customer_info)
        
    elif choice == "4":
        print(customer_info)
        
    elif choice == "5":
        print("Exiting . . .")
        print("GOODBYE")
        break
        
    else:
        print("Invalid choice! Please make a selection between 1-5.")
