def write_name_file():
    name = "Shayan Askarinejad-jahromi"
    file_path = "/home/saskarinejad-jahormi/Desktop/file.txt"

    with open(file_path, "w") as file:
        file.write(name)

write_name_file()

