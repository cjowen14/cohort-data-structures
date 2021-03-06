"""Functions to parse a file containing student data."""


from dbm import dumb

from numpy import full


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1
    cohort_list = []
    for key in student_dict:
      cohort_list.append(student_dict[key][2])

    for cohort in cohort_list:
      houses.add(cohort)

    houses.remove('')
    # print(sorted(houses))

    return sorted(houses)


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1

    delete = set()
    for student in student_dict:
      if student_dict[student][4] == "I\n" or student_dict[student][4] == "G\n":
        delete.add(student)
      
    for i in delete:
      student_dict.pop(i)

    cohort_students = []
    for student in student_dict:
      if cohort == "All":
        cohort_students.append(student_dict[student][0] + " " + student_dict[student][1])
      elif cohort == student_dict[student][4].strip():
        cohort_students.append(student_dict[student][0] + " " + student_dict[student][1])

    return sorted(cohort_students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1
    house_list = []
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []


    for student in student_dict:
      if student_dict[student][2] == "Dumbledore's Army":
        dumbledores_army.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][2] == "Gryffindor":
        gryffindor.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][2] == "Hufflepuff":
        hufflepuff.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][2] == "Ravenclaw":
        ravenclaw.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][2] == "Slytherin":
        slytherin.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][4].strip() == "G":
        ghosts.append(student_dict[student][0] + " " + student_dict[student][1])
      elif student_dict[student][4].strip() == "I":
        instructors.append(student_dict[student][0] + " " + student_dict[student][1])

    house_list.append(sorted(dumbledores_army))
    house_list.append(sorted(gryffindor))
    house_list.append(sorted(hufflepuff))
    house_list.append(sorted(ravenclaw))
    house_list.append(sorted(slytherin))
    house_list.append(sorted(ghosts))
    house_list.append(sorted(instructors))


    # print (house_list)

    return house_list


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    # read data and add to dictionary
    all_data = []
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1

    # Strip whitespace
    for student in student_dict:
      student_dict[student][4] = student_dict[student][4].strip()

    # create tuples and append to list
    delete = set()
    tuple = ()
    for person in student_dict:
      fullname = (student_dict[person][0] + " " + student_dict[person][1])
      delete.add(student_dict[student][1])
      tuple = ()
      tuple = tuple + (fullname,)
      for i in student_dict[person]:
        if not i == student_dict[person][1] and not i == student_dict[person][0]:
          tuple = tuple + (i,)
      all_data.append(tuple)
    

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
  
    the_cohort = ''
    fullname_list = [];
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1

    # Strip whitespace
    for student in student_dict:
      student_dict[student][4] = student_dict[student][4].strip()

    # Make sure the name passed through exists in the data
    for student in student_dict:
      fullname = (student_dict[student][0] + " " + student_dict[student][1])
      fullname_list.append(fullname)
    if not name in fullname_list:
      return

    for student in student_dict:
      if (student_dict[student][0] + " " + student_dict[student][1]) == name:
        the_cohort = student_dict[student][4]

      if the_cohort == "I" or the_cohort == "G":
        the_cohort = "None"
    
    return the_cohort
      


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    dupes = set()
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1
    # Strip whitespace
    for student in student_dict:
      student_dict[student][4] = student_dict[student][4].strip()

     
    for student in student_dict:
      num = 1
      for i in student_dict:
        try:
          num += 1
          if(student_dict[student][1] == student_dict[student + num][1]):
            dupes.add(student_dict[student][1])
        except KeyError:
          pass
      
    # print(dupes)

    return dupes


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    mates = set()
    cohort_data = open(filename, 'r')
    student_dict = {}
    student = 1
    for line in cohort_data:
      student_dict[student] = line.split("|")
      student += 1
    # Strip whitespace
    for student in student_dict:
      student_dict[student][4] = student_dict[student][4].strip()

    for student in student_dict:
      if name == student_dict[student][0] + " " + student_dict[student][1]:
        person = student_dict[student]
    
    for student in student_dict:
      if (student_dict[student][2] == person[2]) and (student_dict[student][4] == person[4]):
        mates.add(student_dict[student][0] + " " + student_dict[student][1])

    mates.remove(person[0] + " " + person[1])
    
    # print(mates)

    return mates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    # filename = "cohort_data.txt"
    # get_housemates_for(filename, 'Harry Potter')
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
