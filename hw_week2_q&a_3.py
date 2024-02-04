import shelve


def check_customer(customer_data, customer_id):
    return customer_id in customer_data


def add_customer(customer_data, customer_name, customer_surname, customer_email, customer_phone):
    if not customer_data:
        customer_data['1001'] = [customer_name, customer_surname, customer_email, customer_phone]
        print('This is first customer adding!!!')
        return True
    else:
        if not (customer_name in customer_data and customer_surname in customer_data and customer_email in customer_data and customer_phone in customer_data):
            customer_id = str(int([x for x in customer_data][-1]) + 1)
            customer_data[customer_id] = [customer_name, customer_surname, customer_email, customer_phone]
            return True
        else:
            return False


def get_list(customer_data):
    result = []
    print(f'ID\tName\tSurname\tEmail\tPhone\n')
    for i in customer_data:
        result += [f'{i}\t{customer_data[i][0]}\t{customer_data[i][1]}\t{customer_data[i][2]}\t{customer_data[i][3]}']
    return result

def update_customer(customer_data, customer_id, customer_name, customer_surname, customer_email, customer_phone):
    if check_customer(customer_data, customer_id):
        customer_data[customer_id] = customer_name, customer_surname, customer_email, customer_phone
        return True
    else:
        return False


def remove_customer(customer_data, customer_id):
    if check_customer(customer_data, customer_id):
        customer_data.pop(customer_id)
        return True
    else:
        return False


def get_customer(customer_data, customer_id):
    if customer_id in customer_data:
        data = customer_data.get(customer_id)
        answer = True
    else:
        data = 'dummy data'
        answer = False
    return answer, data


def help_app():
    print("You can do getlist / add / update / remove; type quit to stop")


def quit_app():
    print("Thank you, goodbye!")


# main program
if __name__ == '__main__':
    with (shelve.open("customer_data.shelve") as the_customer_data):
        print("Welcome to the CMS(Customer Management System) program")
        help_app()
        user_input = "dummy"
        while user_input != "quit":
            user_input = input("What would you like to do: ").strip()

            if user_input == "getlist":
                data = get_list(the_customer_data)
                for i in data:
                    print(i)

            elif user_input == "add":
                the_customer_infos = input(
                    'Please add your customer\'s information by placing a comma between Name, Surname, Email and Phone Number:\n')
                the_customer_infos = the_customer_infos.strip().split(',')
                for i in range(len(the_customer_infos)):  # make values perfect
                    the_customer_infos[i] = the_customer_infos[i].strip()
                the_customer_name = the_customer_infos[0]
                the_customer_surname = the_customer_infos[1]
                the_customer_email = the_customer_infos[2]
                the_customer_phone = the_customer_infos[3]
                result = add_customer(the_customer_data, the_customer_name, the_customer_surname, the_customer_email,
                                      the_customer_phone)
                if result:
                    print(
                        f'Added to CMS = Customer Name: {the_customer_name}, Surname: {the_customer_surname}, Email: {the_customer_email}, Phone Number: {the_customer_phone}')
                else:
                    print('Adding the customer is UNSUCCESSFUL!\n'
                          'Reason: The customer, you want to add is already in the CMS!')

            elif user_input == "update":
                data = get_list(the_customer_data)
                for i in data:
                    print(i)
                the_customer_id = input('Input the Customer ID that you want to update/edit: Tip: Only permitted to change customer information "EXCEPT Customer ID": ')
                result, the_data = get_customer(the_customer_data, the_customer_id)
                if result:
                    print(f"The customer info for ID= {the_customer_id} is:\nName: {the_data[0]}\nSurname: {the_data[1]}\nEmail: {the_data[2]}\nPhone Number: {the_data[3]}")
                    the_data = input(
                    'Please add your customer\'s new information by placing a comma between Name, Surname, Email and Phone Number:\n')
                    the_data = the_data.strip().split(',')
                    for i in range(len(the_data)):  # make values perfect
                        the_data[i] = the_data[i].strip()
                    result = update_customer(the_customer_data, the_customer_id, the_data[0], the_data[1], the_data[2], the_data[3])
                    if result:
                        print('Update process is SUCCESSFUL!')
                    else:
                        print('Update process is UNSUCCESSFUL!\nReason: The customer you want to update is ALREADY NOT in '
                            'the CMS!')
                else:
                    print('Update is IMPOSSIBLE!!!\nReason: The customer you want to update is ALREADY NOT in '
                          'the CMS!')


            elif user_input == "remove":
                the_data = get_list(the_customer_data)
                for i in the_data:
                    print(i)
                the_customer_id = input("Which customer(ID) do you want to remove from CMS? :")
                result = remove_customer(the_customer_data, the_customer_id)
                if result:
                    print(f'The customer whose ID = {the_customer_id} is successfully deleted from the CMS.')
                else:
                    print('Removing the customer is UNSUCCESSFUL!\n'
                          'Reason: The customer you want to delete is ALREADY NOT in the CMS!')

            elif user_input == "lookup":
                the_customer_id = input("Which customer id do you want to lookup? ")
                result, the_data = get_customer(the_customer_data, the_customer_id)
                if result:
                    print(
                        f"The customer info for ID= {the_customer_id} is:\nName: {the_data[0]}\nSurname: {the_data[1]}\nEmail: {the_data[2]}\nPhone Number: {the_data[3]}")
                else:
                    print(f'The customer you have look up \"{the_customer_id}\" hasn\'t added to the CMS yet!')
            elif user_input == "quit":
                quit_app()

            else:
                help_app()
    the_customer_data.close()
