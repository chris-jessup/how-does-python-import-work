"""
A module recording the books and dates of publication
of the various harry potter books
"""

def philosophers_stone():
    print(_when_written("Philosopher's Stone", "1997"))

def chamber_of_secrets():
    print(_when_written("Chamber of Secrets", "1998"))

def prisoner_of_azkaban():
    print(_when_written("Prisoner of Azkaban", "1999"))

def goblet_of_file():
    print(_when_written("Goblet of Fire", "2000"))

def order_of_the_phoenix():
    print(_when_written("Order of the Phoenix", "2003"))

def half_blood_prince():
    print(_when_written("Half-Blood Prince", "2005"))

def deathly_hallows():
    print(_when_written("Deathly Hallows", "2007"))

def _when_written(book, year):
    return f"The book '{book}' was written in {year}"
