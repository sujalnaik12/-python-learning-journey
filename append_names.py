while True:
  name = input("Enter name(or type 'exit' to stop): ")
  if name.lower() == 'exit':
    break
  with open("userdata.text", "a") as file:
    file.write(f"Name: {name}\n")
print("All data saved.")
