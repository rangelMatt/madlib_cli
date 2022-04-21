import re

welcome = """**************************************
**    Welcome to the Mad Libs!   **
**    Please see our Libs below.    **
**
** To quit at any time, type "quit" **
**************************************"""

print(welcome)

def read_template(file_path):
  with open(file_path,'r') as file:
    try:
      # print(file.read().strip())
      return file.read().strip() #.strip gets rid of any leading/trailing white strip.
    except FileNotFoundError:
      print("File does not")

def parse_template(string):
    mad_input = r'{\w*}'
    sentence = r'\w{2,}'
    
    parts = str(re.findall(mad_input, string))
    return_parts = tuple(re.findall(sentence,parts))
    stripped_string = re.sub(mad_input, '{}',string)

    return stripped_string, return_parts

def merge(string, user_input):
  merged = string.format(*user_input)

  return merged
