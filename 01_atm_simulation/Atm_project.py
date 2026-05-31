import json
import os

class ATM:
    
    def __init__(self):
        self.filename = "database.json"
        self.data = self.load_data()
        self.current_user = None  
        
        
        if self.auth_menu():
            while True:
                action = self.main_menu()
                if action == "exit":
                    break 

    def load_data(self):
        
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w") as f:
                json.dump([], f)
                return []
        with open(self.filename, "r") as f:
            return json.load(f)
            
    def save_data(self):
        
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4) 
            return True

    def auth_menu(self):
        
        print("\n--- Welcome to the ATM ---")
        print("1. Type 1 to Register")
        print("2. Type 2 to Login")
        user_input = input("Enter your choice: ").strip()
        
        if user_input == "1":
            self.registration()
            return False 
        elif user_input == "2":
            return self.login()
        else:
            print("Invalid choice.")
            return False
            
    def registration(self):
        print("\n--- Registration ---")
        name = input("Enter your name: ").strip()
        pin = input("Enter your pin (must be 4 digits): ").strip()
        account_no = input("Enter your account number (must be 12 digits): ").strip()
        
        
        if len(pin) != 4 or not pin.isdigit():
            print("❌ Invalid PIN. Must be exactly 4 digits.")
            return
        if len(account_no) != 12 or not account_no.isdigit():
            print("❌ Invalid account number. Must be exactly 12 digits.")
            return
        if not name.replace(" ", "").isalpha():
            print("❌ Name must contain alphabet letters only.")
            return

        
        for item in self.data:
            if account_no in item:
                print("❌ This account number is already registered.")
                return
        
        
        new_user = {
            account_no: {
                "name": name,
                "pin": pin,
                "account_no2": account_no,
                "Balance": 0
            }
        }
        
        self.data.append(new_user)
        if self.save_data():
            print("✅ Registration successful! Please log in now.")
	
    def login(self):
        print("\n--- Login ---")
        account_no = input("Enter your account number: ").strip()
        
        for item in self.data:
            if account_no in item:  
                user_details = item.get(account_no)
                pin = input("Enter your PIN: ").strip()
                
                if user_details["pin"] != pin:
                    print("❌ Wrong PIN. Try again.")
                    return False
                else:
                    print(f"\n✅ Login successful! Welcome, {user_details['name']}.")
                    self.current_user = user_details  
                    return True  
        else:
            print("❌ Account number not found.")
            return False
	        
    def main_menu(self):
        
        print(f"\n--- ATM Main Menu (User: {self.current_user['name']}) ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        user_input = input("Enter your choice: ").strip()
        if user_input == "1":
            self.check_balance()
        elif user_input == "2":
            self.deposit_money()
        elif user_input == "3":
            self.withdraw_money()
        elif user_input == "4":
            self.change_pin()
        elif user_input == "5":
            print("Thank you for using our ATM. Goodbye!")
            return "exit"
        else:
            print("Invalid choice.")
		      	
    def check_balance(self):
        print(f"💰 Your Current Balance: ${self.current_user['Balance']}")
			
    def deposit_money(self):
        try:
            amount = int(input("Enter deposit amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                return
            self.current_user["Balance"] += amount
            self.save_data()
            print(f"✅ ${amount} deposited successfully.")
        except ValueError:
            print("❌ Invalid amount. Please enter numbers only.")		
			
    def withdraw_money(self):
        try:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                return
                
            if amount <= self.current_user["Balance"]:
                self.current_user["Balance"] -= amount
                self.save_data()
                print(f"✅ ${amount} withdrawn successfully.")
            else:
                print("❌ Insufficient funds.")
        except ValueError:
            print("❌ Invalid amount. Please enter numbers only.")
			
    def change_pin(self):
        new_pin = input("Enter new 4-digit PIN: ").strip()
        if len(new_pin) == 4 and new_pin.isdigit():
            self.current_user["pin"] = new_pin
            self.save_data()
            print("✅ New PIN set successfully.")
        else:
            print("❌ Invalid PIN. It must be exactly 4 digits.")

# Run the Application
if __name__ == "__main__":
    a = ATM()
    