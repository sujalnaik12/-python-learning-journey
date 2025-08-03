name = input("Enter your name: ")
with open("userdata.txt", "w") as file:
    file.write(f"Name: {name}\n")
print("Data saved to userdata.txt")
