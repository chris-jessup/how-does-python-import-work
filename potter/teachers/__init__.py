

SCHOOL_NAME = 'hogwarts'

def get_teachers():
    for teacher in [
            "Argus Filch",
            "Filius Flitwick",
            "Gilderoy Lockhart",
            "Poppy Pomfrey",
            "Quirinus Quirrell",
            "Horace Slughorn",
            "Pomona Sprout",
            "Sybill Trelawney",
        ]:
        print(f"{teacher} is a teacher at {SCHOOL_NAME.upper()}")

__all__ = [get_teachers]
