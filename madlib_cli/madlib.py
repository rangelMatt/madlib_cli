# print("""


# """)

def read_template(file_path):
  with open("./assets/dark_and_storm_night_template.txt",'r') as file:
    try:
      return file.read().strip()
      print(file.read().strip())
    except FileNotFoundError:
      print("File does not")

# def parse_template(file):
#   # with open("./assets/dark_and_storm_night_template.txt", "r") as file: