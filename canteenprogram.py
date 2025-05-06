"""
BURNSIDE HIGH SCHOOl Canteen Menu Database

"""


import subprocess
import sys
import sqlite3

# Try importing tabulate, if not installed, install it using pip
try:
    from tabulate import tabulate
except ImportError:
    print("Installing 'tabulate'...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
    print("'tabulate' installed successfully. Please restart the program.")
    sys.exit()


# Define table header for displaying canteen data
header = ['ID', 'NAME', 'CATEGORY', 'PRICE']

# Establish a database connection
connection = sqlite3.connect("")
cursor = connection.cursor()
