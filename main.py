from database import create_tables
from logic import (addCard, searchCard, deleteCard, showAll)

create_tables()

print("MENU")
print("1. Add a card")
print("2. Search for a card")
print("3. Delete a card")
print("4. Show all cards")
print("6. Exit")

choice = input("Enter an option: ")

if choice == "1":
    addCard()

if choice== "2":
    searchCard()

if choice == "3":
    deleteCard()

if choice == "4":
    showAll()