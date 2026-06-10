from database import get_connection

def addCard(cardName, cardNumber, cardQ, cardL):  
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        INSERT INTO cards (cardN, cardID, quantity, location)
        VALUES (?, ?, ?, ?)
                   """, (cardName, cardNumber, cardQ, cardL))
    
    connect.commit()
    connect.close()
    

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

def deleteCard(cardName, cardNumber):
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        DELETE FROM cards WHERE cardN = ? AND cardID = ?
                   """, (cardName, cardNumber))

    connect.commit()
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