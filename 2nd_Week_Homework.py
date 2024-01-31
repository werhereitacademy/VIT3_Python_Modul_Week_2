### Soru1: Öğrenci Notları İşleme
""""
Bir öğrenci notlarını işlemek için bir Python programı yazmanız gerekiyor. Programın aşağıdaki işlevleri yerine getirmesi gerekiyor:

Bir sözlük kullanarak 10 öğrencinin bilgilerini ve notlarını saklayın. Her öğrencinin adı, soyadı ve notları(Vize, Final ve Sozlu notu) olsun. Örneğin:

![resim](https://github.com/werhereitacademy/week_2/assets/141542413/dc91b4b6-a51c-4f5f-80a3-854d505ce48a)

1-Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin.

2-En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.

3-Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.

4-Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.

5-Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
"""

### Question 1: Student Grades Processing
"""You need to write a Python program to process student grades. The program should perform the following functions:

Store the information and grades of 10 students using a dictionary. Each student should have a name, surname, and grades (Midterm, Final, and Oral).

1-Calculate the average grade for each student and add it to the dictionary.

2-Find the student with the highest average grade and print it to the screen.

3-Separate the first name of each student from their surname and store them in a tuple, then add these tuples to a list.

4-Sort the list alphabetically by names and print the sorted list to the screen.

5-Store the students with an average grade below 70 in a set.
"""

students = {
    "Dragica Brodie": [75, 90, 78],
    "Neil Calvert": [92, 88, 75],
    "Raymond Evans": [90, 89, 95],
    "Philip Harrison": [80, 75, 78],
    "Jonathan Metcalfe": [60, 55, 65],
    "Sharron Norman": [84, 91, 55],
    "Laurence Pearson": [70, 65, 70],
    "James Pritchard": [78, 81, 75],
    "Simon Thacker": [87, 89, 55],
    "David Willis": [80, 90, 79]
}

# 1-Calculate the average grade for each student and add it to the dictionary.
for student, grades in students.items():
    average = sum(grades) / len(grades)
    students[student].append(average)

# 2-Find the student with the highest average grade and print it to the screen.
highestAverageStudent = max(students, key=lambda x: students[x][-1])
print(f"Student with the highest average grade: {highestAverageStudent}")

# 3-Separate the first name of each student from their surname and store them in a tuple, then add these tuples to a list.
nameSurnameList = [(name.split()[0], name.split()[1]) for name in students.keys()]
print(nameSurnameList)

# 4-Sort the list alphabetically by names and print the sorted list to the screen.
sortedNameSurnameList = sorted(nameSurnameList, key=lambda x: (x[0], x[1]))
print("Sorted list by names alphabetically:")
for firstName, lastName in sortedNameSurnameList:
    print(f"{firstName} {lastName}")

# 5-Store students with an average grade below 70 in a set.
below70Students = {student for student, grades in students.items() if grades[-1] < 70}
print("Students with an average grade below 70:", below70Students)

###

###

###  Soru 2 : Film Kütüphanesi Yönetim Sistemi Projesi

"""Proje Açıklaması: Bu proje, kullanıcının kendi film koleksiyonunu yönetmesine yardımcı olacak bir uygulama oluşturmayı amaçlar. Kullanıcılar filmleri ekleyebilir, düzenleyebilir, silebilir ve koleksiyonlarını görüntüleyebilir.

Kullanılan Veri Yapıları: Sözlükler (filmleri ve ilgili bilgileri saklamak için), listeler (film koleksiyonunu görüntülemek için)

Temel İşlevler:

1-Kullanıcıdan film adı, yönetmen, yayın yılı ve tür gibi bilgileri alarak bir film verisi oluşturun ve bunu bir sözlükte saklayın.

2-Kullanıcıya bir filmi düzenleme veya silme seçeneği sunun.(Bunun icin filme ait hangi veriyi degistirmek istiyorlarsa ona uygun bir fonksiyon yazilmasi gerekir.)

3-Kullanıcının koleksiyonunu görüntülemesine izin verin. Tüm filmleri listeleyin veya tür veya yayın yılı gibi kriterlere göre filtreleyin.

4-Film verilerini bir dosyada saklayın ve programı başlattığınızda bu veriyi geri yükleyin."""

### Question 2: Movie Library Management System Project
"""
Project Description: This project aims to create an application that assists users in managing their own film collection. Users can add, edit, delete films, and view their collections.

Used Data Structures: Dictionaries (to store films and related information), Lists (to display the film collection).

Core Functions:

Create film data by obtaining information such as the film title, director, release year, and genre from the user, and store this data in a dictionary.

Provide the user with the option to edit or delete a film. (For this, functions need to be written to modify the relevant data of the film.)

Allow the user to view their collection. List all films or filter based on criteria such as genre or release year.

Store film data in a file and reload this data when the program is started.
"""

filmLibrary = []

def addMovie():
    title = input("Enter the movie title: ")
    director = input("Enter the director's name: ")
    releaseYear = input("Enter the release year: ")
    genre = input("Enter the movie genre: ")

    movie = {
        'title': title,
        'director': director,
        'releaseYear': releaseYear,
        'genre': genre
    }

    filmLibrary.append(movie)
    print(f"{title} movie added to the collection.")

def viewCollection():
    for movie in filmLibrary:
        print(f"Movie Title: {movie['title']}, Director: {movie['director']}, Release Year: {movie['releaseYear']}, Genre: {movie['genre']}")

def editMovie():
    title = input("Enter the title of the movie you want to edit: ")
    
    for movie in filmLibrary:
        if movie['title'] == title:
            movie['director'] = input("Enter the new director's name: ")
            movie['releaseYear'] = input("Enter the new release year: ")
            movie['genre'] = input("Enter the new movie genre: ")
            print(f"{title} movie edited.")
            return

    print(f"{title} movie not found.")

def deleteMovie():
    title = input("Enter the title of the movie you want to delete: ")

    for movie in filmLibrary:
        if movie['title'] == title:
            filmLibrary.remove(movie)
            print(f"{title} movie deleted.")
            return

    print(f"{title} movie not found.")

# User interface
while True:
    print("\n1. Add Movie")
    print("2. View Collection")
    print("3. Edit Movie")
    print("4. Delete Movie")
    print("5. Exit")

    choice = input("Select the operation you want to perform (1-5): ")

    if choice == '1':
        addMovie()
    elif choice == '2':
        viewCollection()
    elif choice == '3':
        editMovie()
    elif choice == '4':
        deleteMovie()
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")

###

###
        
###  Soru 3 :Müşteri Yönetim Sistemi
"""
Proje Açıklaması: Bu proje, müşterilerinizi yönetmek ve temel işlemleri gerçekleştirmek için kullanabileceğiniz bir müşteri yönetim sistemi oluşturmanızı içerir. Bu sistem, müşteri bilgilerini saklama, yeni müşteri ekleyebilme, müşteri bilgilerini güncelleyebilme, müşteri silme ve müşteri listesini görüntüleme gibi temel işlevlere sahip olacaktır. İşte projenin temel adımları:

1-Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın. Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin. Her müşteri için ad, soyad, e-posta, telefon gibi bilgileri içeren bir sözlük kullanabilirsiniz.

2-Kullanıcıya aşağıdaki işlemleri seçebileceği bir menü sunun:

* Yeni müşteri eklemek
* Müşteri bilgilerini güncellemek
* Müşteri silmek
* Tüm müşterileri listelemek
* Çıkış yapmak

3-Kullanıcının seçimine göre ilgili işlemi gerçekleştirin. Örneğin, yeni müşteri eklerken kullanıcıdan gerekli bilgileri alın ve sözlüğe yeni bir müşteri ekleyin.

4-Müşteri bilgilerini güncellerken, müşteri kimliğini kullanarak mevcut bilgileri görüntüleyin ve güncellenmiş bilgileri kaydedin.

5-Müşteri silme işleminde kullanıcıdan müşteri kimliğini alın ve bu müşteriyi sözlükten silin.

6-Tüm müşterileri listeleme işleminde, mevcut müşterilerin listesini görüntüleyin.

7-Kullanıcı çıkış yapana kadar işlemleri tekrarlayın.
"""

### Question 3: Customer Management System
"""
Project Description: This project involves creating a customer management system that allows you to manage your customers and perform basic operations. The system will have fundamental functionalities such as storing customer information, adding new customers, updating customer information, deleting customers, and displaying the list of customers. Here are the basic steps for the project:

Use a dictionary structure to store customer information. Assign a unique customer identifier (ID) to each customer and associate customer information with this ID. You can use a dictionary for each customer, including information such as first name, last name, email, and phone.

Provide the user with a menu where they can choose the following operations:

* Add a new customer
* Update customer information
* Delete a customer
* Display all customers
* Exit the system
Based on the user's selection, perform the corresponding operation. For example, when adding a new customer, prompt the user for the required information and add a new customer to the dictionary.

When updating customer information, display the current information using the customer ID and save the updated information.

For the customer deletion process, take the customer ID from the user and remove that customer from the dictionary.

In the operation to display all customers, show the list of existing customers.

Repeat the operations until the user chooses to exit.
"""

# Create an empty customer list
customerList = []

# Function to add a new customer
def addNewCustomer():
    firstName = input("Enter the customer's first name: ")
    lastName = input("Enter the customer's last name: ")
    email = input("Enter the customer's email address: ")
    phone = input("Enter the customer's phone number: ")

    # Generate a unique ID for each customer (e.g., a sequential number)
    customerId = len(customerList) + 1

    # Store customer information in a dictionary
    customer = {
        'id': customerId,
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'phone': phone
    }

    # Add the customer to the list
    customerList.append(customer)
    print(f"Customer {firstName} {lastName} added. Customer ID: {customerId}")

# Function to list all customers
def listCustomers():
    if not customerList:
        print("No customers added yet.")
    else:
        print("\nCUSTOMER LIST:")
        for customer in customerList:
            print(f"ID: {customer['id']}, First Name: {customer['firstName']}, Last Name: {customer['lastName']}, Email: {customer['email']}, Phone: {customer['phone']}")

# Function to update a customer
def updateCustomer():
    if not customerList:
        print("No customers to update. Add a customer first.")
        return

    listCustomers()
    customerId = int(input("Enter the ID of the customer to update: "))

    for customer in customerList:
        if customer['id'] == customerId:
            print(f"\nCurrent Customer Information:")
            print(f"ID: {customer['id']}, First Name: {customer['first_name']}, Last Name: {customer['last_name']}, Email: {customer['email']}, Phone: {customer['phone']}")

            # Get new information
            customer['firstName'] = input("Enter the new first name: ")
            customer['lastName'] = input("Enter the new last name: ")
            customer['email'] = input("Enter the new email address: ")
            customer['phone'] = input("Enter the new phone number: ")

            print("Customer information updated.")
            return

    print(f"Customer with ID {customerId} not found.")

# Function to delete a customer
def deleteCustomer():
    if not customerList:
        print("No customers to delete. Add a customer first.")
        return

    listCustomers()
    customerId = int(input("Enter the ID of the customer to delete: "))

    for customer in customerList:
        if customer['id'] == customerId:
            customerList.remove(customer)
            print(f"Customer with ID {customerId} deleted.")
            return

    print(f"Customer with ID {customerId} not found.")

# User interface
while True:
    print("\nCUSTOMER MANAGEMENT SYSTEM")
    print("1. Add New Customer")
    print("2. List Customers")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Exit")

    choice = input("Select the operation you want to perform (1-5): ")

    if choice == '1':
        addNewCustomer()
    elif choice == '2':
        listCustomers()
    elif choice == '3':
        updateCustomer()
    elif choice == '4':
        deleteCustomer()
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")
