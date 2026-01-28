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
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice
    print("Hello")


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
        print("\n--- Exiting program... Bye!")
        running = False
        exit()

    else:
        print("\nInvalid Choice. Please enter a number between 1 and 5")

menu()