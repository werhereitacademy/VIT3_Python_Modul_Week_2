"""
Readme:

- Week 2 Homework Answers, VIT 3 Project, 2024

"""

students = {'Ahmet Yilmaz': [85, 90, 78],
            'Mehmet Demir': [92, 88, 76],
            'Ayse Kaya': [78, 89, 95],
            'Salih Ergun': [80, 96, 92],
            'Ibrahim Turhan': [70, 78, 90],
            'Samet Kilic': [48, 30, 50],
            'Mustafa Saritas': [69, 58, 72],
            'Guluzar Coskun': [88, 80, 100],
            'Furkan Altay': [70, 72, 74],
            'Murat Yildirim': [82, 86, 94]}


def show_list(list1):  # This function represents the members of a list as a string with a comma between each member.
    long_string = ''
    for _ in list1:
        long_string += _ + ', '
    return long_string[0:(len(long_string) - 2)]


if __name__ == '__main__':
    print('\nAnswer 1/1:')
    for i in students:
        avg = float(format(sum(students[i]) / len(students[i]), '.2f'))
        students[i] += [avg]
    print(students)

    print('\nAnswer 1/2:')

    list_avg = []
    excellent_students = []  # Maybe there are more students who have the same average.
    for i in students:
        list_avg += [students[i][3]]
    for i in students:
        if max(list_avg) == students[i][3]:
            excellent_students += [i]
    print('The most successful student(s): ', show_list(excellent_students))

    print('\nAnswer 1/3:')
    # Information Source: https://stackoverflow.com/questions/16449184/converting-string-to-tuple-without-splitting-characters

    name = []
    surname = []
    full_names = []
    for i in students:
        full_name = i.split(' ')
        name, surname = tuple([full_name[0]]), tuple([full_name[1]])
        full_names += [name, surname]  # If I had to place each person individually in the list item I would have to use this code: full_names += [[name, surname]]
    print(full_names)

    print('\nAnswer 1/4:')

    print('Only student names are sorted')
    print(sorted(students))

    print('Student names sorted with notes')
    students2 = []
    for i in sorted(students):
        students2 += [[i] + students[i]]
    print(students2)

    print('\nAnswer 1/5:')

    students_under70 = set()
    for i in students:
        if students[i][3] < 70:
            students_under70.add(i)
    print(students_under70)
