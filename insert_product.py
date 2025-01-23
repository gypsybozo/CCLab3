import sqlite3
import requests
import random
def get_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM products')
    
    
    products = []
    rows = cursor.fetchall()
    
    for i in range(len(rows)):
        temp = rows[i]
        products.append(temp)

    if len(products) > 0:
        products.sort(key=lambda x: 0)
    # print(products)
    connection.commit()
    connection.close()
    return products

def insert_cart_products(cookies,products):
    random.seed(42)
    for i in range(100):
        
        p=random.choice(products)
        print("http://127.0.0.1:5000/cart/{}".format(p[0]))
        r=requests.post("http://127.0.0.1:5000/cart/{}".format(p[0]),cookies=cookies)
        
        if r.status_code==200:
            print(r)
            print("inserted product")
        else:
            print("failed to insert")
        
        

def insert_user(username, password):
    connection = sqlite3.connect("auth.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    connection.commit()
    
def login(username, password):
    session = requests.Session()
    payload = {
        "username": username,
        "password": password
    }
    r = session.post("http://127.0.0.1:5000/login", data=payload)
    print(f"Login Response: {r.status_code}, {r.text}")
    
    if r.status_code == 200:
        print("Logged in successfully")
        return session.cookies
    else:
        print("Could not log in")
        return None

        
    
    
    
def main():
    username="123"
    password="123"
    insert_user(username, password)
    cookies=login(username,password)
    print(cookies)
    products=get_products()
    insert_cart_products(cookies,products)
    

if __name__ == "__main__":
    main()
