# LAB - Class 01

## Author: Matthew Rangel

## Links and Resources

- [include help](https://www.includehelp.com/python/FileNotFoundError.aspx)
- Morning Lecture Video
- Bishal Khanal
- Dwight Lindquist
- Roger Wells
- [regex101](https://regex101.com/)
<!-- PORT - Port Number
DATABASE_URL - URL to the running Postgres instance/db
How to initialize/run your application (where applicable)
e.g. python main.py
How to use your library (where applicable)
Tests -->

## How do you run tests?

1. Created test and ran `pytest`
2. Imported formula from series module to test_series module
3. Run `pytest`
4. Fleshed out formula in series module
5. Run `pytest`
   - If failed, tweak check for error and refactor accordingly
      - GOOGLE, PEER, TA
   - If Pass, proceed to next formula.

### Class notes

1. Define functions to 'skip test'
2. Find first error, which is a typeError: read_template() takes 0 position  arguments but 1 was given
3. Now, AssertionError: assert None == 'It was {Adjective} and {Adjective} {Noun}.'
4. Look at test and see what it is looking for.
5. return that to pass.
6. provide .txt file  # for first test
7. read()
   - there is still white space, use strip to git rid.
8. Repeat steps 1 -5 for next test
9. return tuple, but there was an error of an extra parenthesis, so delete outer parenthesis
10. iterate through the string

#### iterate character by character

```json
for char in template:
   if not capturing:
      stripped += char
      if char == "{":
         capturing = True
   else: 
      if char == "}":
         stripped += char
         # more to do
      else:
         capture += char
         parts.append(capture)
         capture = ""
         capturing = False
      else:
         capture += char

```

when in the mode of iterating, create capturing var and assign it to false.

capture = ""

some_tuple = ("a",1, True) # as soon as you use that comma, it becomes a tuple.

## Any tests of note?

def parse_template required to use regex. Regex made it INSANELY harder. I needed a lot of hand holding on this on.

def test_read_template_raises_exception_with_bad_path threw me for a quick loop.

<!-- Describe any tests that you did not complete, skipped, etc -->