"""
BURNSIDE HIGH SCHOOl Canteen Menu Database

"""

import time
import subprocess
import sys
import sqlite3
import os

# Try importing tabulate, if not installed, install it using pip
try:
    from tabulate import tabulate
except ImportError:
    print("Installing 'tabulate'...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    print("'tabulate' installed successfully. Please restart the program.")
    sys.exit()


# Define table header for displaying canteen data
header = ['ID', 'ITEM', 'CATEGORY', 'PRICE']

# Establish a database connection
connection = sqlite3.connect("canteen.db")
cursor = connection.cursor()

# Password for staff only functions
password = 'burnsidehighschool'

# Function to clear terminal
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display menu in the database using tabulate
def displaymenu():
    viewall = cursor.execute('SELECT * FROM "food"')
    rows = viewall.fetchall()
    formatted_rows = [(food_id, food_name, food_price, avaliability) for food_id, food_name, food_price, avaliability in rows]
    print(' \033[1mMENU:\033[0m')
    print(tabulate(formatted_rows, headers=header, tablefmt="simple_grid"))

# Function to check if a food ID exists in the database
def findID(id):
    data = [id]
    cursor.execute('SELECT food_id FROM food WHERE food_id =?', data)
    viewid = cursor.fetchall()
    if viewid:
        return True
    
# Function for login system
def stafflogin(max_attempts=3):
    
    for attempt in range(max_attempts):
        login = input('Enter password')
        if login == password:
            print('Access granted')
            return True
        
        else:
            remaining_attempts = max_attempts - attempt - 1
            if remaining_attempts:
                print(f'Incorrect password. {remaining_attempts} attempts remaining.')
            else:
                print('Too many incorrect attempts.')
    return False
        





#Welcom users
print('Welcome to the Burnside High School online canteen menu!')
time.sleep(1.5)
#Main program loop
while True:
    
    
    print('MAIN MENU:')
    
    #Prompt user for main menu input
    main_menu = input('Enter \033[1m"A"\033[0m to order\nEnter \033[1m"B"\033[0m to view order history\nEnter \033[1m"C"\033[0m to view menu\nEnter \033[1m"D"\033[0m to edit menu (staff only)\n').strip().upper()

    #order items
    if main_menu == 'A':
        print('You chose order items from menu')
        
    
    #if main_menu == 'B':
    
    
    if main_menu == 'C':
        print('You chose view menu...')
        time.sleep(1)
        clearscreen()
        displaymenu()
        

    if main_menu == 'D':
        
        # Call login function
        if stafflogin():
            print('loading...')
            time.sleep(1)
        else:
            continue


