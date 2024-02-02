########Soltion_1

# Information of 10 students is added under their name key in the created dictionary.
student_information = {
    "Ali": {
        "Last Name": "Demir",
        'Grades': [56, 78, 90],
    },
    "Ayse": {
        "Last Name": "Yilmaz",
        "Grades": [89, 76, 95],
    },
    "Ahmet": {
        "Last Name": "Coban",
        "Grades": [45, 38, 70],
    },
    "Mehmet": {
        "Last Name": "Kaya",
        "Grades": [70, 65, 80],
    },
    "Beyza": {
        "Last Name": "Dag",
        "Grades": [80, 90, 95],
    },
    "Firat": {
        "Last Name": "Celik",
        "Grades": [75, 89, 70],
    },
    "Guluzar": {
        "Last Name": "Coskun",
        "Grades": [85, 90, 100],
    },
    "Sevgi": {
        "Last Name": "Kara",
        "Grades": [45, 50, 75],
    },
    "Fatma": {
        "Last Name": "Kisa",
        "Grades": [65, 70, 90],
    },
    "Orhan": {
        "Last Name": "Seckin",
        "Grades": [30, 38, 50]
    }
}

# List created to add students with below-average grades.
low_grades = []

# Dictionary to store calculated averages.
averages = {
    "Ali": "",
    "Ayse": "",
    "Ahmet": "",
    "Mehmet": "",
    "Beyza": "",
    "Firat": "",
    "Guluzar": "",
    "Sevgi": "",
    "Fatma": "",
    "Orhan": ""
}

# This function calculates the average of given grades, adds it to the dictionaries,
# and adds the students with averages below 70 to the list.
def calculate_average(name, midterm, final, oral):
    average = int((midterm + final + oral) / 3)
    student_information[name]["Average"] = average
    averages[name] = average
    if average < 70:
        low_grades.append("{} : {}".format(name, average))
    return average

calculate_average("Ali", 56, 78, 90)
calculate_average("Ayse", 12, 43, 40)
calculate_average("Ahmet", 45, 38, 70)
calculate_average("Mehmet", 70, 65, 80)
calculate_average("Beyza", 80, 90, 95)
calculate_average("Firat", 75, 89, 70)
calculate_average("Guluzar", 85, 90, 100)
calculate_average("Sevgi", 45, 50, 28)
calculate_average("Fatma", 65, 70, 90)
calculate_average("Orhan", 30, 38, 30)

# To find the student with the highest average, first get the highest grade from values,
# then find the key of that value.
average_list = tuple(averages.values())
highest_grade = sorted(average_list)[-1]

grade_values = list(averages.values())
highest_grade_index = grade_values.index(highest_grade)

grade_keys = list(averages.keys())
highest_grade_owner = grade_keys[highest_grade_index]

print("The highest average grade is {} and it belongs to {}.".format(highest_grade, highest_grade_owner))

# After storing each student's name as the main key in the first dictionary in a tuple,
# the tuple is converted to a list and displayed on the screen after being sorted alphabetically.
student_names = tuple(student_information.keys())
student_names_list = []
student_names_list.append(student_names)
print(sorted(student_names_list))

# To print the list created for students with below-average grades as a set;
low_grades_set = set(low_grades)
print(low_grades_set)

########Solution_2
class MovieLibrary(object):
    def __init__(self, movie_title, director, release_year, genre):
        self.movie_title = movie_title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.movie_collection = []
        self.movie_info = {}
        self.movie_info_file_name = "movie_info.txt"

        self.movie_info[movie_title] = [director, release_year, genre]
        self.movie_collection.append(movie_title)
        self.update_movie_file()

    def update_movie_file(self):
        with open(self.movie_info_file_name, "w") as movie_info_file:
            for movie_title, info in self.movie_info.items():
                movie_info_file.write(f"{movie_title},{info[0]},{info[1]},{info[2]}\n")
            print("Movie file updated.")

    def delete_movie(self, movie_title):
        with open(self.movie_info_file_name, "r") as movie_info_file:
            lines = movie_info_file.readlines()

        with open(self.movie_info_file_name, "w") as movie_info_file:
            for line in lines:
                values = line.strip().split(',')
                if len(values) == 4:
                    file_movie_title, _, _, _ = values
                    if file_movie_title != movie_title:
                        movie_info_file.write(line)

        print("Movie file updated.")

    def add_movie(self):
        movie_title = input("Enter the name of the movie you want to add:\nEnter `2` to go back: ")
        if movie_title == "2":
            return
        else:
            director = input("Enter the director of the movie: ")
            release_year = input("Enter the release year of the movie: ")
            genre = input("Enter the genre of the movie: ")

        self.movie_info[movie_title] = [director, release_year, genre]
        self.movie_collection.append(movie_title)
        print("Movies in your collection:", self.movie_collection)

        self.update_movie_file()

    def add_to_collection(self):
        movie_title = input("Enter the name of the movie you want to add to your collection:\nEnter `2` to go back: ")
        if movie_title == "2":
            return
        else:
            self.movie_collection.append(movie_title)
            print("Updated movie collection:", self.movie_collection)

    def edit_movie(self):
        movie_title = input("Enter the name of the movie you want to edit (Press '2' to go back): ")
        if movie_title in self.movie_collection:
            choice1 = input(
                "Press '1' to change the director, '2' to change the release year, '3' to change the genre: ")
            if choice1 == "1":
                new_director = input("Enter the name of the new director: ")
                self.movie_info[movie_title][0] = new_director
            elif choice1 == "2":
                new_release_year = input("Enter the new release year: ")
                self.movie_info[movie_title][1] = new_release_year
            elif choice1 == "3":
                new_genre = input("Enter the new genre: ")
                self.movie_info[movie_title][2] = new_genre
            print("Saved movie information:", self.movie_info)
            self.update_movie_file()
        elif movie_title == "2":
            return
        else:
            print("Movie not found.")

    def delete_movie(self):
        movie_title = input("Enter the name of the movie you want to delete:\nEnter `2` to go back: ")

        if movie_title in self.movie_collection:
            self.delete_movie(movie_title)
            if movie_title in self.movie_info.keys():
                del self.movie_info[movie_title]
            print(movie_title, "is being removed from your collection.")
            self.movie_collection.remove(movie_title)
        elif movie_title == "2":
            return
        else:
            print("Movie not found.")

        print(self.movie_info)

    def view_collection(self):
        print("Movies in your collection:", self.movie_collection)

    def all_movie_info(self):
        print("Saved movie information:", self.movie_info)


# User input
movie_title = input("Enter the name of the movie you want to save: ")
director = input("Enter the director of the movie you want to save: ")
release_year = input("Enter the release year of the movie you want to save: ")
genre = input("Enter the genre of the movie you want to save: ")

# Creating an instance of the MovieLibrary class
m1 = MovieLibrary(movie_title=movie_title, director=director, release_year=release_year, genre=genre)

# Providing options to the user
while True:
    choice = input(
        "Press '1' to add a movie\n"
        "Press '2' to edit movie details\n"
        "Press '3' to delete a movie\n"
        "Press '4' to view your collection\n"
        "Press '5' to add to your collection only\n"
        "Press '6' to view current movie information\n"
        "Press '7' to exit: ")
    if choice == "1":
        m1.add_movie()
    elif choice == "2":
        m1.edit_movie()
    elif choice == "3":
        m1.delete_movie()
    elif choice == "4":
        m1.view_collection()
    elif choice == "5":
        m1.add_to_collection()
    elif choice == "6":
        m1.all_movie_info()
    elif choice == "7":
        print("Exiting the system.")
        break


########Solution_3

customer_information = {}
customer_id = 1

while True:
    print("\n1. Add a new customer\n2. Update customer information\n3. Delete a customer\n4. List all customers\n5. Exit")
    
    choice = input("Please choose an operation (1-5): ")
    if choice == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_information[customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
        customer_id += 1
        print(customer_information)
        
    elif choice == "2":
        print(customer_information)
        updated_customer_id = int(input("Customer ID to update: "))
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_information[updated_customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
    
        print("Customer information updated!")
        print(customer_information)
        
    elif choice =="3":
        print(customer_information)
        deleted_customer_id = int(input("Customer ID to delete: "))
        del customer_information[deleted_customer_id]
        print("Your operation has been successfully completed.")
        print(customer_information)
        
    elif choice == "4":
        print(customer_information)
        
    elif choice == "5":
        print("Exiting. . .")
        print("GOODBYE")
        break
        
    else:
        print("Invalid choice! Please choose between 1-5.")
