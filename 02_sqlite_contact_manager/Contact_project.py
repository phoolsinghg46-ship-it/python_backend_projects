import sqlite3

DB_NAME = "contact_project.db"

def init_db():
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_no INTEGER,
            email TEXT 
        )
        ''')
        conn.commit()

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email: ").strip()
    
    if not name or not phone:
        print("❌ Name and Phone number cannot be empty.")
        return

    try:
        phone = int(phone)
        
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO contact(name, phone_no, email) VALUES (?, ?, ?)", 
                (name, phone, email)
            )
            conn.commit()
        print("✅ Contact details added successfully!")
    except ValueError:
        print("❌ Invalid phone number. Please enter digits only.")
    except sqlite3.Error as e:
        print(f"❌ Database error occurred: {e}")
        
def show_data():
    print("\n--- Contact Directory ---")
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contact")
            data = cursor.fetchall()
            
        if not data:
            print("The directory is currently empty.")
            return
            
        for contact in data:
            print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
    except sqlite3.Error as e:
        print(f"❌ Database error occurred: {e}")
        
def search_data():
    print("\n--- Search Contact ---")
    name = input("Enter the name to search: ").strip()
    
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contact WHERE name LIKE ?", (f"%{name}%",)) 
            data = cursor.fetchall()
            
        if data:
            print(f"\nFound {len(data)} record(s):")
            for contact in data:
                print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}")
        else:
            print("❌ No details found matching that name.")
    except sqlite3.Error as e:
        print(f"❌ Database error occurred: {e}")

def main():
  
    init_db()
    
    while True:
        print('''\n=========================
How would you proceed?
1. Add data
2. See all data in table
3. Search personal data
4. Exit
=========================''')
        
        user_choice = input("Enter your choice (1-4): ").strip()
        
        if user_choice == "1":
            add_contact()
        elif user_choice == "2":
            show_data()
        elif user_choice == "3":
            search_data()
        elif user_choice == "4":
            print("Goodbye!")
            break 
        else:
            print("❌ Invalid choice. Please pick a number between 1 and 4.")

if __name__ == "__main__":
    main()
    