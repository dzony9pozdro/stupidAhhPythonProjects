import json
import os
from typing import cast
FILE = 'contacts.json'

def load() -> dict[str, dict[str,str]]:
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return cast(dict[str, dict[str,str]], json.load(f))
    return {}

def save(contacts: dict[str,dict[str,str]]) -> None:
    with open(FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def add(name: str, phone: str, email: str):
    contacts = load()
    contacts[name] = {"phone": phone, "email": email}
    save(contacts)


def delete(name: str):
    contacts = load()
    del contacts[name]
    save(contacts)
    
def run(action: str):
    match action:
        case "add":
            name = input("name: ")
            phone = input("phone: ")
            email = input("email: ")
            add(name, phone, email)
        case "delete":
            name = input("name: ")
            delete(name)
        case "list":
            contacts = load()
            for name, items in contacts.items():
                print(name, items["phone"], items["email"])
        case "search":
            contacts = load()
            query = input("name: ")
            if query in contacts:
                info = contacts[query]
                print(query, info["phone"], info["email"])
            else:
                print("contact not found")
        case _:
            print('valid actions are: add, delete. list, search')
action ="" 
while True:
    action = input('add, delete, list, search: ')
    if action in ("add", "delete", "list", "search"):
        run(action)
        break

