
# Python String Methods Demonstration
# Each method includes a brief explanation and a print output

s = "  Hello World 123  "

# lower(): Converts all characters to lowercase
print("lower():", s.lower())

# upper(): Converts all characters to uppercase
print("upper():", s.upper())

# title(): Capitalizes first letter of each word
print("title():", s.title())

# capitalize(): Capitalizes first character of the string
print("capitalize():", s.capitalize())

# strip(): Removes leading and trailing whitespace
print("strip():", s.strip())

# lstrip(): Removes leading whitespace
print("lstrip():", s.lstrip())

# rstrip(): Removes trailing whitespace
print("rstrip():", s.rstrip())

# replace(): Replaces occurrences of a substring
print("replace():", s.replace("World", "Python"))

# split(): Splits string into a list using delimiter
print("split():", s.split())

# join(): Joins elements of a list into a string
words = ["Python", "is", "powerful"]
print("join():", " ".join(words))

# find(): Returns lowest index of substring or -1 if not found
print("find():", s.find("World"))

# rfind(): Returns highest index of substring
print("rfind():", s.rfind("l"))

# index(): Returns index of substring or raises error if not found
print("index():", s.index("Hello"))

# count(): Counts occurrences of substring
print("count():", s.count("l"))

# startswith(): Checks if string starts with substring
print("startswith():", s.startswith("  Hello"))

# endswith(): Checks if string ends with substring
print("endswith():", s.endswith("123  "))

# isalpha(): True if all characters are alphabets
print("isalpha():", "Hello".isalpha())

# isdigit(): True if all characters are digits
print("isdigit():", "123".isdigit())

# isalnum(): True if all characters are alphanumeric
print("isalnum():", "Hello123".isalnum())

# isspace(): True if all characters are whitespace
print("isspace():", "   ".isspace())

# istitle(): True if string is title-cased
print("istitle():", "Hello World".istitle())

# islower(): True if all characters are lowercase
print("islower():", "hello".islower())

# isupper(): True if all characters are uppercase
print("isupper():", "HELLO".isupper())

# swapcase(): Swaps case of all characters
print("swapcase():", s.swapcase())

# center(): Centers the string with padding
print("center():", "Hello".center(20, "*"))

# ljust(): Left-justifies string with padding
print("ljust():", "Hello".ljust(20, "-"))

# rjust(): Right-justifies string with padding
print("rjust():", "Hello".rjust(20, "-"))

# zfill(): Pads numeric string on the left with zeros
print("zfill():", "42".zfill(6))

# format(): Formats string using placeholders
print("format():", "My name is {} and age is {}".format("Aditya", 20))

# partition(): Splits string into 3 parts using separator
print("partition():", s.partition("World"))

# rpartition(): Splits string into 3 parts from right
print("rpartition():", s.rpartition("l"))

# splitlines(): Splits string at line breaks
multi = "Line1\nLine2\nLine3"
print("splitlines():", multi.splitlines())

# encode(): Encodes string into bytes
print("encode():", "Hello".encode("utf-8"))
