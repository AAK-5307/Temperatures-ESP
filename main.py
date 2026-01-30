import pandas as pd 
import matplotlib.pyplot as plt 

# Load the csv
df = pd.read_csv("temperatures.csv")

# Calculate average temperature
df["AvgTemp"] = (df["MinTemp"] + df["MaxTemp"]) / 2

# --- USER FUNCTION ---
def menu():
    print("\n===== Temperature Data Menu =====")
    print("1. View the full DataFrame")
    print("2. View the summary statistics")
    print("3. View Average Temperature")
    print("4. Plot Min, Avg and Max Temperatures")
    print("5. Input your own data and obtain a chart")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

def user_data():
    user_input = str(input("Enter a month within 2026: "))
    user_temp_month = []
    user_list_month = []
    while True:
        month = input("Enter the month of your choice: ")
        temperature_month = input("Enter the temperature of the month that you inputted: ")

        user_list_month.append(month)
        user_temp_month.append(temperature_month)
        
        option = Validator.validate("Would you like to continue your data input?: ")

class Validator:
    @staticmethod
    def validate(prompt: str, typ: type = str, allow_empty: bool = False):
        while True:
            user_input = input(prompt)

            if typ is str:
                if not allow_empty and user_input.strip() == "":
                    print("Please enter a valid option\n")
                    continue
                
                return user_input

            if not allow_empty and user_input.strip() == "":
                print("Please enter a valid integer\n")
            elif typ is float:
                print("Please enter a valid number\n")
            else:
                print("Please enter a valid value\n")
            continue
        try:
            if typ is int:
                return int(user_input)
            
            if typ is float:
                return float(user_input)

            return typ(user_input)

        except ValueError:
            if typ is int:
                print("Please enter a valid integer\n")
            elif typ is float:
                print("Please enter a valid number\n")
            else:
                print("Please enter a valid value\n")

# --- MAIN LOOP --- 
running = True 
while running:
    user_choice = menu()
    if user_choice == "1":
        print("\n--- Full DataFrame --- ")
        print(df)

    elif user_choice == "2":
        print("\n--- Summary Statistics ---")
        print(df.describe())

    elif user_choice == "3":
        print("\n--- Plotting Average Temperature ---")
        plt.figure(figsize = (10, 5))
        plt.plot(df["Month"], df["AvgTemp"], marker = 'o', label = "Average Temp")
        plt.title("Average Monthly Temperatures")
        plt.xlabel("Month")
        plt.ylabel("Temperature (*C)")
        plt.grid(True)
        plt.legend()
        plt.show()

    elif user_choice == "4":
        print("\n--- Plotting Temperature Range ---")
        plt.figure(figsize=(10, 5))
        plt.plot(df["Month"], df["MinTemp"], marker = 'o', label = "Min Temp")
        plt.plot(df["Month"], df["AvgTemp"], marker = 'o', label = "AvgTemp")
        plt.plot(df["Month"], df["MaxTemp"], marker = 'o', label = "MaxTemp")
        plt.title("Temperature Range Throughout The Year")
        plt.xlabel("Month")
        plt.ylabel("Temperature (*C)")
        plt.grid(True)
        plt.legend()
        plt.show()

    elif user_choice == "5":
        user_data()

    elif user_choice == "6":
        print("\n--- Exiting program... Bye!")
        running = False
        exit()

    else:
        print("\nInvalid Choice. Please enter a number between 1 and 5")


