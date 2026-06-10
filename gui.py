import tkinter as tk
from tkinter import ttk
from database import get_connection

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

    for cards in results:
        inventoryView.insert("", tk.END, values=(cards[1], cards[2], cards[3], cards[4]))
    
    connect.close()


