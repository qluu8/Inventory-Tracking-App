import tkinter as tk
from tkinter import ttk
from database import get_connection
from logic import addCard, deleteCard, searchCard

def runGUI():
    root = tk.Tk()

    root.title("Inventory Tracking App")
    root.geometry("600x400")

    button_frame = tk.Frame(root)
    button_frame.pack(side="top", fill="x")

    addButton = tk.Button(button_frame, text="Add Card")
    addButton.pack(side="left", padx="5", pady="5")

    deleteButton = tk.Button(button_frame, text="Delete Card")
    deleteButton.pack(side="left", padx="5", pady="5")

    searchButton = tk.Button(button_frame, text="Search")
    searchButton.pack(side="left", padx="5", pady="5")

    viewFrame = tk.Frame(root)
    viewFrame.pack(side="top", fill="both", expand=True)

    inventoryView = ttk.Treeview(viewFrame, columns=("Card Name", "Card Number", "Quantity", "Location"), show="headings" )

    inventoryView.heading("Card Name", text="Card Name")
    inventoryView.heading("Card Number", text="Card Number")
    inventoryView.heading("Quantity", text="Quantity")
    inventoryView.heading("Location", text="Location")

    inventoryView.column("Card Name", width="200")
    inventoryView.column("Card Number", width="120")
    inventoryView.column("Quantity", width="20")
    inventoryView.column("Location", width="100")

    inventoryView.pack(fill="both", expand=True, padx=10, pady=10)
    
    loadInventory(inventoryView)
    
    addButton.config(command=lambda: handleAddButton(root, inventoryView))
    deleteButton.config(command=lambda: handleDeleteButton(root, inventoryView))
    searchButton.config(command=lambda: handleSearchButton(root, inventoryView))
    root.mainloop()

def loadInventory(inventoryView):
    connect = get_connection()
    cursor = connect.cursor()

    cursor.execute("""
    SELECT * FROM cards
                   """)
    results = cursor.fetchall()

    for row in inventoryView.get_children():
        inventoryView.delete(row)

    for card in results:
        inventoryView.insert("", tk.END, values=(card[1], card[2], card[3], card[4]))
    
    connect.close()

def handleAddButton(root, inventoryView):
    def saveCard():
        cardName = addName.get()
        cardNumber = addNumber.get()
        cardQ = addQuantity.get()
        cardL = addLocation.get()
        
        addCard(cardName, cardNumber, cardQ, cardL)
        loadInventory(inventoryView)
        addWindow.destroy()
    addWindow = tk.Toplevel(root)
    
    addWindow.geometry("300x200")
    addWindow.title("Adding a Card")
    
    addNameL = tk.Label(addWindow, text="Name of Card:", font=('Times', 10))
    addName = tk.Entry(addWindow)
    
    addNumberL = tk.Label(addWindow, text="Card Number:", font=('Times', 10))
    addNumber = tk.Entry(addWindow)
    
    addQuantityL = tk.Label(addWindow, text="Quantity of Card", font=('Times', 10))
    addQuantity = tk.Entry(addWindow)
    
    addLocationL = tk.Label(addWindow, text="Location of Card", font=('Times', 10))
    addLocation = tk.Entry(addWindow)
    
    saveButton = tk.Button(addWindow, text="Save", command=saveCard)
    saveButton.grid(row=4, column=0, columnspan=2, pady=10)
    
    addNameL.grid(row=0,column=0, padx=5, pady=5)
    addName.grid(row=0, column=1, padx=5, pady=5)
    addNumberL.grid(row=1, column=0, padx=5, pady=5)
    addNumber.grid(row=1, column=1, padx=5, pady=5)
    addQuantityL.grid(row=2, column=0, padx=5, pady=5)
    addQuantity.grid(row=2, column=1, padx=5, pady=5)
    addLocationL.grid(row=3, column=0, padx=5, pady=5)
    addLocation.grid(row=3, column=1, padx=5, pady=5)


def handleDeleteButton(root, inventoryView):
    def confirmDelete():
        cardName = delName.get()
        cardNumber = delNumber.get()
        
        deleteCard(cardName, cardNumber)
        loadInventory(inventoryView)
        deleteWindow.destroy()

    deleteWindow = tk.Toplevel(root)

    deleteWindow.geometry("300x175")
    deleteWindow.title("Deleting a Card")
    
    nameLabel = tk.Label(deleteWindow, text="Name of Card", font=('Times', 10))
    delName = tk.Entry(deleteWindow)
    
    numberLabel = tk.Label(deleteWindow, text="Number of Card", font=('Times', 10))
    delNumber = tk.Entry(deleteWindow)
    
    confirmButton = tk.Button(deleteWindow, text="Delete", command=confirmDelete)
    confirmButton.grid(row=2, column=0, columnspan=2, pady=10)
    
    nameLabel.grid(row=0, column=0, padx=5, pady=5)
    delName.grid(row=0, column=1, padx=5, pady=5)
    numberLabel.grid(row=1, column=0, padx=5, pady=5)
    delNumber.grid(row=1, column=1, padx=5, pady=5)
    

def handleSearchButton(root, inventoryView):
    searchWindow = tk.Toplevel(root)
    searchWindow.geometry("200x180")
    searchWindow.title("Searching for a Card")

    nameLabel = tk.Label(searchWindow, text="Name of Card", font=('Times', 10))
    searchName = tk.Entry(searchWindow)
    numberLabel = tk.Label(searchWindow, text="Number of Card", font=('Times', 10))
    searchNumber = tk.Entry(searchWindow)

    nameLabel.grid(row=0, column=0, padx=5, pady=5)
    searchName.grid(row=0, column=1, padx=5, pady=5)
    numberLabel.grid(row=1, column=0, padx=5, pady=5)
    searchNumber.grid(row=1, column=1, padx=5, pady=5)


