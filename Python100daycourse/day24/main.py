from pathlib import Path
script_dir = Path(__file__).parent
file_path = script_dir / "myfile.txt"

# file = open(file_path, "r")
# contents = file.read()
# print(contents)
# file.close()

# with open(file_path, "w") as file:
#     file.write("\nHello, World!")

with open(file_path, "r") as file:
    contents = file.read()
    print(contents) 