

def get_gryffindor():
    print_students(
        'gryffindor', 
        [
            "Harry Potter",
            "Ronald Weasley",
            "Neville Longbottom",
            "Dean Thomas",
            "Seamus Finnigan",
            "Hermione Granger",
            "Lavender Brown",
            "Parvati Patil",
        ]
    )

def get_hufflepuff():
    print_students(
        'hufflepuff',
        [
            "Ernie Macmillan",
            "Justin Finch-Fletchley",
            "Hannah Abbott",
            "Susan Bones",
            "Wayne Hopkins",
            "Megan Jones",
            "Roger Malone",
            "Kevin Entwhistle",
        ]
    )

def get_ravenclaw():
    print_students(
        'ravenclaw',
        [
            "Terry Boot",
            "Mandy Brocklehurst",
            "Michael Corner",
            "Anthony Goldstein",
            "Padma Patil",
            "Lisa Turpin",
            "Isobel MacDougal",
            "Stephen Cornfoot",
            "Oliver Rivers",
            "Sue Li",
        ]
    )

def get_slytherin():
    print_students(
        'slytherin',
        [
            "Draco Malfoy",
            "Vincent Crabbe",
            "Gregory Goyle",
            "Blaise Zabini",
            "Theodore Nott",
            "Pansy Parkinson",
            "Millicent Bulstrode",
            "Daphne Greengrass",
            "Tracey Davis",
        ]
    )

def print_students(team, students):
    print(f"The following students are from {team.upper()}:")

__all__ = [get_gryffindor, get_hufflepuff, get_ravenclaw, get_slytherin]
