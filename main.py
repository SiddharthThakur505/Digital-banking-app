# 1. Create Class  Bank 
# 2. CRUD operations
# create -> Create User
# Read -> Reading user details
# Update ->Updating user details
# Delete -> Deleting user details


from pathlib import Path
import json
import random
import string

class Bank:
    database = "data.json"
    data = []     #yeh data json mai save hoga

    try:
        if Path(database).exists():
            print("File Exists..")
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists...")
    except Exception as err:
        print("Error Occured")

    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @staticmethod
    def __generateAcc():  # to find the random account number 
        digits = random.choices(string.digits,k=4)
        alpha = random.choices(string.ascii_letters,k=4)
        id = digits + alpha
        random.shuffle(id)
        return "".join(id)

    # Create user
    def CreateAccount(self):
        info ={
            'name' : input('Enter your name:'),
            'age' : int(input("Enter your age:")),
            'phoneno.' : int(input("Enter your phone number:" )),
            'email' : input("Enter your email:"),
            'pin' :int(input("Enter your pin:")),
            'accountno.' : Bank.__generateAcc(),
            'balance' : 0  
        }
        if info['age'] > 18 and len(str(info['pin'])) == 4:
            Bank.data.append(info)
            Bank.__update()
            print('Data added in list')
            print(Bank.data)
        else:
            print("Credintials are not valid!")

    def depositmoney(self):
        accountno = input("Enter your accountno:")
        pin = int(input("Enter your 4 digit pin:"))

        user_data = [i for i in Bank.data if i ['accountno.'] ==accountno and i['pin']==pin]
        if user_data == False:
            print("User not found")
        else:
            amount = int(input("paise :"))
            if amount <= 0:
                print("Invalid Amount")
            elif amount > 10000:
                print("Grater than 10000")
            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print('Amount Credited')


    def Withdrawmoney(self):
        accountno = input("Enter your accountno:")
        pin = int(input("Enter your 4 digit pin:"))

        user_data = [i for i in Bank.data if i ['accountno.'] ==accountno and i['pin']==pin]
        if user_data == False:
            print("User not found")
        else:
            amount = int(input("paise :"))
            if amount <= 0:
                print("Invalid Amount")
            elif amount > 10000:
                print("Grater than 10000")
            else:
                if user_data[0]['balance'] < amount:
                    print("Insufficient Balance")
                else:
                    user_data[0]['balance'] -= amount    
                    Bank.__update()
                    print('Amount debited')
    
    def Details(self):
        accountno = input("Enter your accountno:")
        pin = int(input("Enter your 4 digit pin:"))

        user_data = [i for i in Bank.data if i ['accountno.'] ==accountno and i['pin']==pin]
        if user_data == False:
            print("User not found")
        else:
            for i in user_data[0]:
                print(i,user_data[0][i])

            

    def update_details(self):
        accountno = input("Enter your accountno:")
        pin = int(input("Enter your 4 digit pin:"))

        user_data = [i for i in Bank.data if i ['accountno.'] ==accountno and i['pin']==pin]
        if user_data == False:
            print("User not found")

        else:
            print("what do you want to update?")
            print("1. name")
            print("2. age")
            print("3. phone number")
            print("4. email")
            print("5. pin")
            print("6. update all details")

            choice = int(input("Enter your choice:"))

            if choice == 1:
                user_data[0]['name'] = input("Enter your name:")
                Bank.__update()
                print("name updated successfully")

            elif choice == 2:
                user_data[0]['age'] = int(input("Enter your age:"))
                Bank.__update()
                print("age updated successfully")

            elif choice == 3:
                user_data[0]['phoneno.'] = int(input("Enter your phone number:"))
                Bank.__update()
                print("phone number updated successfully")

            elif choice == 4:
                user_data[0]['email'] = input("Enter your email:")
                Bank.__update()
                print("email updated successfully")

            elif choice == 5:
                user_data[0]['pin'] = int(input("Enter your pin:"))
                Bank.__update()
                print("pin updated successfully")

            elif choice == 6:
                print("Leave blank to skip any field")

                name = input("Enter your name:")
                age = input("Enter your age:")
                phone = input("Enter your phone number:")
                email = input("Enter your email:")
                new_pin = input("Enter your pin:")

                if name:
                    user_data[0]['name'] = name

                if age.isdigit():
                    user_data[0]['age'] = int(age)

                if phone.isdigit():
                    user_data[0]['phoneno.'] = int(phone)

                if email:
                    user_data[0]['email'] = email

                if new_pin.isdigit() and len(new_pin) == 4:
                    user_data[0]['pin'] = int(new_pin)

                print("All details updated successfully")

            else:
                print("Invalid choice")

            Bank._Bank__update()
            # print()  yaha par ham phir se show karna chahe to kya karenge 


                
    def delete(self):
        accountno = input("Enter your accountno:")
        pin = int(input("Enter your 4 digit pin:"))

        user_data = [i for i in Bank.data if i ['accountno.'] ==accountno and i['pin']==pin]
        if user_data == False:
            print("User not found")
        else:
            print("are you sure you want to delete your account? yes/no")
            choice = input("Enter your choice:")
            if choice == "yes":
                ind=Bank.data.index(user_data[0])
                Bank.data.pop(ind)
                Bank.__update()
                print("account deleted successfully")
            else:
                print("operation terminated")


while True:
        obj=Bank()
        print("press 1 for Create Account")
        print("press 2 for Deposite Money")
        print("press 3 for Withdraw Money")
        print("press 4 for Account Details")
        print("press 5 for update details")
        print("press 6 for delete account")


        choice = int(input("Enter your choice:"))

        if choice == 1:
            obj.CreateAccount()

        elif choice == 2:
            obj.depositmoney()

        elif choice == 3:
            obj.Withdrawmoney()

        elif choice == 4:
            obj.Details()

        elif choice == 5:
            obj.update_details()

        elif choice == 6:
            obj.delete()
        
        else:
            print("Invalid choice")


obj = Bank()
obj.CreateAccount()
obj.depositmoney()
obj.Withdrawmoney()
obj.Details()
obj.update_details()
obj.delete()