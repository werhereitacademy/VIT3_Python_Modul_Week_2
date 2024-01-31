#**********Q1**********

student = {
"Daan Emma" : [50,60,70],  
"Lucas Julia" : [45,35,55],
"Finn Sophie" : [70,40,80],
"Sem Mila" : [55,25,65],
"Jesse Tess" : [70,66,65],
"Milan Zoë" : [90,70,80],
"Levi Sara" : [45,35,40],
"Liam Eva" : [65,70,85],
"Noah Anna" : [90,50,60],
"Luuk Noor" : [25,35,45], 
}
voor_naam = []  
achter_naam = []  
gemiddeld_max =[]
low_70 =[]
print("1-Calculating each student's grade point average and adding it to the dictionary")    
for key, value in student.items():
    gemiddeld=round(sum(value)/3)
    gemiddeld_max.append(gemiddeld)
    student[key].append(gemiddeld)
    print(key,value) #1-Calculating each student's grade point average and adding it to the dictionary

for key, value in student.items():
    if student[key][-1] == max(gemiddeld_max) :
        print(f"2-{key} is the student with the highest GPA with {max(gemiddeld_max)}")
    if  student[key][-1] <= 70 :
        low_70.append(key)

for key in student:
    x = (key.split(" ")) 
    for i in x:
        voor_naam.append(x[0])
        achter_naam.append(x[1])
        break 

print(f"3-Name tuble ={tuple(voor_naam)}\n  Lastname tuble={tuple(achter_naam)}")
print(f"4-Alphabetical order of names = {sorted(voor_naam)}")
print(f"5-Set of students with GPA below 70 ={set(low_70)}")

#**********Q2**********
from colorama import Fore, init
init(autoreset=True) 
import json
my_archive = []
def add_movie():
    name_film = input("The name of the movie:")
    name_director = input("Film director:")
    film_category = input("Category of the movie:")
    film_year = input("Release year of the movie:")
    my_film = {
        "Film name" : name_film,
        "Film director" : name_director,
        "Film category" : film_category,
        "Film year" : film_year,
    }

    my_archive.append(my_film) 
    print(type(my_archive)) 
    
def edit_movie(name_film):
    for edit in my_archive:
       if edit["Film name"] == name_film:
           edit["Film director"] = input("New director:")
           edit["Film category"] = input("New category:")
           edit["Film year"] = input("New year:")
           return
    print(Fore.RED + "Movie not found")   

def list_movie():
    i = 1
    for film in my_archive:
        print(f'{i}.{film["Film name"]},{film["Film director"]},{film["Film category"]},{film["Film year"]}')
        i+=1
    
def filter_movie():
    print("""    Press 1 to filter by year
    Press 2 to filter by category""")   
    filter_select = input("Please enter filter number:")
    if filter_select == "1" :
        filter_year = input("Please enter year:")
        i=1
        for film in my_archive:
            if film["Film year"] == filter_year:
                 print(f'{i}.{film["Film name"]},{film["Film director"]},{film["Film category"]},{film["Film year"]}')
                 i+=1
            else:
                print(Fore.RED + "There were no results.")
    elif filter_select == "2" :
        filter_category = input("Please enter category:")
        i=1
        for film in my_archive:
            if film["Film category"] == filter_category:
                 print(f'{i}.{film["Film name"]},{film["Film director"]},{film["Film category"]},{film["Film year"]}')
                 i+=1
            else:
                print(Fore.RED + "There were no results.")        
    else:
        print(Fore.RED + "Please enter a number between 1 and 2")
        
def delete_movie():
    film_delete = input("Enter the name of the movie to be deleted:")
    for film in my_archive:
        if film["Film name"] == film_delete:
            my_archive.remove(film)
            print(Fore.GREEN + "Movie deleted successfully")
        else:
            print(Fore.RED + "Movie not found")

def exit_movie():
    with open('my_archive.json', 'w') as json_archive:
        json.dump(my_archive, json_archive,indent=6, sort_keys=True)
    print(Fore.GREEN + "All information was recorded.")  

try:
    with open('my_archive.json', 'r') as json_archive:
        my_archive = json.load(json_archive)
except FileNotFoundError:
    print(Fore.RED + "No data found.") 

while True:
    print('*'*36)
    print(Fore.BLUE + "Welcome to The Movie Archive System")
    print("""    1 press to add movie
    2 press to edit movie
    3 press to list movie
    4 press to filter movie
    5 press to delete movie      
    6 press to exit archive system""")
    process = input("Please enter process number=")
    if process == "1":
        add_movie() 
        print(Fore.GREEN + "The movie was saved successfully")

    elif process == "2":
        name_film = input("Name of the movie to be edited:")
        edit_movie(name_film) 
        print(Fore.GREEN + "The movie was edited successfully")
    elif process == "3":
        list_movie()
    elif process == "4":
        filter_movie()
    elif process == "5":
        delete_movie()     
    elif process == "6":
        exit_movie()
        break        
    else:
        print(Fore.RED + "Please enter a number between 1 and 6")
      
#**********Q3**********
from colorama import Fore, init
init(autoreset=True) 
import datetime
import json
customer = []
def costumer():
    name_customer = input("Costumer Name =")
    lname_customer = input("Costumer Last Name =")
    email_customer = input("Costumer email =")
    phone_customer = input("Costumer Phone Number=")
    customer_system = {
        "Customer Number":customer_number(),
        "Name" : name_customer,
        "Lname":lname_customer,
        "Email":email_customer,
        "Phone":phone_customer
    }
    customer.append(customer_system)
    print(Fore.GREEN + "The customer was saved successfully")
    list()
def update():
    list()
    update_id = input("Please enter the customer number to be updated=")
    for update_edit in customer:
        if update_edit["Customer Number"] == update_id:
            update_edit["Name"] = input("Enter the new name:")
            update_edit["Lname"] = input("Enter the new lastname:")
            update_edit["Email"] = input("Enter te new email:")
            update_edit["Phone"] = input("Enter the new phone:")
            print(Fore.GREEN + "The customer was edited successfully")
            return
    else:
        print(Fore.RED+ "Customer Not Found")    

def delete():
    list()
    delete_id = input("Please enter the customer number to be updated=")
    for delete_customer in customer:
        if delete_customer["Customer Number"] == delete_id:
            customer.remove(delete_customer)
            print(Fore.GREEN + "Customer Deleted Successfully")
        else:
             print(Fore.RED+ "Customer Not Found")    
               
def list():
    x = '*'*10
    print(Fore.GREEN + f'{x}"General Customer List"{x}')
    i = 1
    for my_list in customer:
        print(f'{i}.{my_list["Customer Number"]},{my_list["Name"]},{my_list["Lname"]},{my_list["Email"]},{my_list["Phone"]}')
        i+=1

def register():
     with open('customer.json', 'w') as json_customer:
        json.dump(customer, json_customer,indent=6,sort_keys= True)
        print(Fore.GREEN + "All information was recorded.")  
 
def customer_number():
    x = datetime.datetime.now()
    id = x.strftime("%d%m%y%H%M%S")
    return id 

try:
    with open('customer.json', 'r') as json_customer:
        customer = json.load(json_customer)
except FileNotFoundError:
    print(Fore.RED + "No data found.") 
 
while True:
    print(Fore.MAGENTA + '*'*36)
    print(Fore.BLUE + "    Welkom to Customer Registration System")
    print("""    1 press to add a new customer
    2 press to edit costemer
    3 press to delete costemer
    4 press to list costemer     
    5 press to exit registration system""")
    process = input("   Please enter process number=")
    if process == "1":
        costumer() 
    elif process == "2":
        update() 
    elif process == "3":
        delete()
    elif process == "4":
        list()
    elif process == "5":
        register()
        break             
    else:
        print(Fore.RED + "Please enter a number between 1 and 5")
