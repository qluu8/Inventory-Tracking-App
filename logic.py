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
    

def searchCard(cardName, cardNumber):
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        SELECT * FROM cards WHERE cardN LIKE ? AND cardID LIKE ?
                   """, ("%" + cardName + "%", "%" + cardNumber + "%"))
    
    results = cursor.fetchall()
    connect.close()
    
    return results

def deleteCard(cardName, cardNumber):
    connect = get_connection()
    cursor = connect.cursor()
    
    cursor.execute("""
        DELETE FROM cards WHERE cardN = ? AND cardID = ?
                   """, (cardName, cardNumber))

    connect.commit()
    connect.close()
    