#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import uuid
def create_directory():
    directory = {}

    while True:
        first_name = input("Enter first name (or 'q' to quit): ")
        if first_name.lower() == "q":
            break

        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        print("Data Entered successfully!")
        print("""Wether you continue to enter the entry?
        If not! Please enter q to exit""")
       
        user_id = uuid.uuid4()
       
        directory[user_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }

    with open("directory.txt", "w") as file:
        for user_id, user_info in directory.items():
            file.write(f"{user_id},{user_info['first_name']},{user_info['last_name']},{user_info['phone_number']}\n")




def access_directory():
    directory = read_directory_file()

    user_id = input("Enter user ID to access the details: ")

    if user_id in directory:
        user_info = directory[user_id]
        print("User Information:")
        print(f"First Name: {user_info['first_name']}")
        print(f"Last Name: {user_info['last_name']}")
        print(f"Phone Number: {user_info['phone_number']}")
    else:
        print("User ID not found in the directory.")


def delete_directory():
    directory = read_directory_file()

    user_id = input("Enter user ID to delete the details: ")

    if user_id in directory:
        del directory[user_id]

      
        with open("directory.txt", "w") as file:
            for user_id, user_info in directory.items():
                file.write(f"{user_id},{user_info['first_name']},{user_info['last_name']},{user_info['phone_number']}\n")

        print("User details deleted successfully!")
    else:
        print("User ID not found in the directory.")


def read_directory_file():
    directory = {}

    if os.path.exists("directory.txt"):
        with open("directory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                user_id, first_name, last_name, phone_number = line.strip().split(",")
                directory[user_id] = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number
                }

    return directory



while True:
    print("\n--- Directory Management System ---")
    print("1. Create Directory")
    print("2. Access User Details")
    print("3. Delete User Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_directory()
    elif choice == "2":
        access_directory()
    elif choice == "3":
        delete_directory()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Directory Management System!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




