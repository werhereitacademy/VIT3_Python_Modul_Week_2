import shelve


def check_movie(movie_data, movie_name):
    return movie_name in movie_data


def add_movie(movie_data, movie_name, movie_infos):
    if not check_movie(movie_data, movie_name):
        movie_data[movie_name] = movie_infos
        return True
    else:
        return False


def get_movie(movie_data, movie_name):
    #   print("I am looking up the movie info")
    if check_movie(movie_data, movie_name):
        data = movie_data.get(movie_name)
        answer = True
    else:
        data = "dummy data"
        answer = False
    return answer, data


def update_movie(movie_data, movie_name, movie_infos):
    if check_movie(movie_data, movie_name):
        movie_data[movie_name] = movie_infos
        return True
    else:
        return False


def remove_movie(movie_data, movie_name):
    if check_movie(movie_data, movie_name):
        movie_data.pop(movie_name)
        return True
    else:
        return False


def help_app():
    print("You can do lookup / add / update / remove; type quit to stop")


def quit_app():
    print("Thank you, goodbye!")

# main program
if __name__ == '__main__':
    with (shelve.open("movie_data.shelve") as the_movie_data):
        print("Welcome to the Movie List program")
        help_app()
        user_input = "dummy"
        while user_input != "quit":
            user_input = input("What would you like to do: ")

            if user_input == "add":
                the_movie_infos = input(
                    'Please add the movie\'s information by placing a comma between movie_name, movie_director, '
                    'release_date, movie_genre:\n')
                the_movie_infos = the_movie_infos.strip().split(',')
                for i in range(len(the_movie_infos)):  # make values perfect
                    the_movie_infos[i] = the_movie_infos[i].strip()
                the_movie_name = the_movie_infos[0]
                result = add_movie(the_movie_data, the_movie_name, the_movie_infos[1:4])
                if result:
                    print(
                        f'Added to Movie List = Movie Name: {the_movie_name}, Director: {the_movie_infos[1]}, Release Year: {the_movie_infos[2]}, Genre: {the_movie_infos[3]}')
                else:
                    print('Adding the film is UNSUCCESSFUL!\n'
                          'Reason: The movie, you want to add is already in the Movie List!')

            elif user_input == "lookup":
                the_movie_name = input("Which movie do you want to lookup? ")
                result, the_data = get_movie(the_movie_data, the_movie_name)
                if result:
                    print(
                        f"The infos for {the_movie_name} is:\nDirector: {the_data[0]}\nRelease Year: {the_data[1]}\nGenre: {the_data[2]}")
                else:
                    print(f'The movie you have look up \"{the_movie_name}\" hasn\'t added to the Movie List!')

            elif user_input == "update":
                the_movie_name = input("Which movie(name) do you want to edit/update? :")
                result, the_data = get_movie(the_movie_data, the_movie_name)
                if result:
                    print(f'{the_movie_name} Infos:\nDirector: {the_data[0]}\nRelease Year: {the_data[1]}\nGenre: {the_data[2]}')
                    the_data = input(f'Add new information for {the_movie_name}...\nTip: You can only update information '
                                     f'except movie name!\n')
                    the_data = the_data.strip().split(',')
                    for i in range(len(the_data)):  # make values perfect
                        the_data[i] = the_data[i].strip()
                    result2 = update_movie(the_movie_data, the_movie_name, the_data)
                    if result2:
                        print('Update process is SUCCESSFUL!')
                    else:
                        print('Update process is UNSUCCESSFUL!\nReason: The movie you want to update is ALREADY NOT in '
                              'the Movie List!')
                else:
                    print('Update is IMPOSSIBLE!!!\nReason: The movie you want to update is ALREADY NOT in '
                          'the Movie List!')

            elif user_input == "remove":
                the_movie_name = input("Which movie(name) do you want to delete? :")
                result = remove_movie(the_movie_data, the_movie_name)
                if result:
                    print(f'{the_movie_name} is successfully deleted from the list.')
                else:
                    print('Removing the film is UNSUCCESSFUL!\n'
                          'Reason: The movie you want to delete is ALREADY NOT in the Movie List!')

            elif user_input == "quit":
                quit_app()

            else:
                help_app()
the_movie_data.close()
