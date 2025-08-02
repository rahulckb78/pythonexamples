#!/usr/bin/env python3
days_in_a_week = { 
            1: "Sunday", 
            2: "Monday", 
            3: "Tuesday", 
            4: "Wednesday", 
            5: "Thursday", 
            6: "Friday", 
            7: "Saturday" 
} 

def get_day_name(day_num): 
    """Function will return the day's in week

    Args:
        day_num (int): Day number 1 to 7

    Returns:
        String: Date name
    """
    return days_in_a_week.get(day_num, "Invalid number") 

def main():
    try: 
        day_num = int(input("Enter a number between 1 and 7: ")) 
        print("The corresponding day is:", get_day_name(day_num)) 
    except ValueError: 
        print("Please enter a valid integer between 1 and 7.")

# Main program 
if __name__ == "__main__":
    main()

    
