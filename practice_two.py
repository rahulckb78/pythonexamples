#!/usr/bin/env python3
# Need to add datetime library of python
from datetime import datetime

num_of_persons = {}
# Function to calculate age
def find_age_of_person(birth_date):
    """Calculate the age of the person

    Args:
        birth_date (Object): Datetime

    Returns:
        Int: age of the person
    """
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    """Main function
    """
    # Input data for 20 persons
    for _ in range(20):
        name = input("Enter name: ")
        dob_str = input("Enter date of birth (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        num_of_persons[name] = dob

    # Print names of persons who are more than 21 years old
    print("Persons more than 21 years old:")
    for name, dob in num_of_persons.items():
        if find_age_of_person(dob) > 21:
            print(name)

# Run main function
if __name__ == "__main__":
    main()