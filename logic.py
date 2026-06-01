from database import get_connection

def addCard():
    cardName = input("Enter card name: ")
    cardNumber = input("Enter card number: ")
    cardQ = input("Enter quantity of card(s): ")
    loc = input("Enter location of card(s): ")
    
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        INSERT INTO cards (cardN, cardID, quantity, location)
        VALUES (?, ?, ?, ?)
                   """, (cardName, cardNumber, cardQ, loc))
    
    connect.commit()
    connect.close()
    print("Card added successfully.")
    

def searchCard():
    choice = input("Enter name of card: ")
    
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        SELECT * FROM cards WHERE cardN LIKE ?
                   """, ("%" + choice + "%",))
    
    results = cursor.fetchall()
    
    if results:
        for card in results:
            print(card)
    else:
        print("No card with that name found.")
        
    connect.close()

def deleteCard():
    showAll()
    name = input("Enter name of card: ")
    number = input("Enter the number of the card: ")
    
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        DELETE FROM cards WHERE cardN = ? AND cardID = ?
                   """, (name, number))

    connect.commit()
    
    if cursor.rowcount > 0:
        print("Card deleted successfuly")
    else:
        print("No matching card found.")
        
    connect.close()
    
def showAll():
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        SELECT * FROM cards
                   """)
    
    results = cursor.fetchall()
    
    if results:
        for card in results:
            print(card)
    else:
        print("No cards found.")
        
    connect.close()