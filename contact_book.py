contacts = []

def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone number:")
  contacts.append({"name": name, "phone": phone})
  print("Contact added!")

def view_contacts():
  if not contacts:
    print("No contacts available.")
  else:
    for c in contacts:
      print(f" Name: {c['name']}, Phone: {c['phone']}")

def search_contact():
  search_name = input("Enter name to search: ")
  found = False
  for c in contacts:
    if c['name'].lower() == search_name.lower():
      print(f"Name: {c['name']}, Phone: {c['phone']}")
      found = True
  if not found:
    print("Contact not found!")

while True:
  print("\n Options: add / view / search / exit.")
  action = input("Choose an action: ").lower()
  if action == 'add':
    add_contact()
  elif action == 'view':
    view_contacts()
  elif action == 'search':
    search_contact()
  elif action == 'exit':
    print("Goodbye!")
    break
  else:
    print("Invalid option. Please try again!")

