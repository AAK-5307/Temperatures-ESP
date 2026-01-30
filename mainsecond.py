import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("temperatures.csv")
mylabels = ["Ahmed", "Jayden", "Declan", "Ilona"]

def menu():
    print("1. Plot a pie chart")
    print("2. Plot a bar chart")
    print("3. View summary statistics")
    print("4. Find the average of the statistics")
    print("5. Exit the program")

    option = input("Please enter your choice: ")
    return option

running = True

while running:
    user_choice = menu()

    if user_choice == "1":
        print("Plotting pie chart now\n")
        y = np.array([23, 55, 76, 21])
        myexplode = [40, 0.5, 0.6, 0.9]
        plt.pie(y, labels = mylabels, explode = myexplode, startangle = 180)
        plt.show()

    elif user_choice == "2":
        print("Plotting bar chart now\n")
        x = np.array([17, 17, 16, 17])
        plt.show(20, 50)

    elif user_choice == "3":
        print("\n=== Printing Statistics Now ===")
        print(df.describe())
        break

    elif user_choice == "4":
        print("\nPlotting average now\n")
        print(df.mean())

    else:
        print("\nInvalid choice\n")
