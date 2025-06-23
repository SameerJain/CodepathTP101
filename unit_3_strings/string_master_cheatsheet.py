#!/usr/bin/env python3
"""
Complete Python Strings Reference
==================================

This file contains everything you need to know about strings in Python.
All examples are executable - run this file or copy sections to experiment.

Table of Contents:
1. String Basics
2. String Creation
3. String Indexing & Slicing
4. String Methods
5. String Formatting
6. String Operations
7. Escape Sequences
8. Raw Strings
9. String Comparison
10. String Constants
11. Regular Expressions
12. Performance Tips
13. Common Patterns
"""

import string
import re
import sys
from datetime import datetime

def section_separator(title):
    """Helper function to print section separators"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print('='*60)

# ============================================================================
# 1. STRING BASICS
# ============================================================================

section_separator("1. STRING BASICS")

# What are Strings?
# - Strings are sequences of characters in Python
# - Immutable (cannot be changed after creation)
# - Ordered collection with indexing starting at 0
# - Can contain letters, numbers, symbols, and whitespace

s = "Hello World"
print(f"String: {s}")
print(f"Length: {len(s)}")           # 11 - length
print(f"Type: {type(s)}")            # <class 'str'>
print(f"First character: {s[0]}")    # 'H' - first character
print(f"Last character: {s[-1]}")    # 'd' - last character

# ============================================================================
# 2. STRING CREATION
# ============================================================================

section_separator("2. STRING CREATION")

# Single and Double Quotes
single = 'Hello World'
double = "Hello World"
mixed1 = "It's a beautiful day"
mixed2 = 'She said "Hello"'

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Mixed 1: {mixed1}")
print(f"Mixed 2: {mixed2}")

# Triple Quotes (Multiline)
multiline = """This is a
multiline string
spanning multiple lines"""

multiline2 = '''Another way
to create multiline
strings'''

print(f"Multiline 1:\n{multiline}")
print(f"Multiline 2:\n{multiline2}")

# Useful for docstrings
def my_function():
    """
    This is a docstring
    explaining the function
    """
    pass

print(f"Function docstring: {my_function.__doc__}")

# Empty Strings
empty1 = ""
empty2 = str()
print(f"Empty string 1: '{empty1}' (length: {len(empty1)})")
print(f"Empty string 2: '{empty2}' (length: {len(empty2)})")

# ============================================================================
# 3. STRING INDEXING & SLICING
# ============================================================================

section_separator("3. STRING INDEXING & SLICING")

s = "Python"
print(f"String: {s}")
print("Indexing:")
print("    012345  (positive indexing)")
print("   -654321  (negative indexing)")

# Indexing
print(f"s[0]: {s[0]}")    # 'P'
print(f"s[1]: {s[1]}")    # 'y'
print(f"s[-1]: {s[-1]}")  # 'n'
print(f"s[-2]: {s[-2]}")  # 'o'

# Slicing
s = "Hello World"
print(f"\nSlicing examples with '{s}':")

# Basic slicing: s[start:end:step]
print(f"s[0:5]: '{s[0:5]}'")      # 'Hello'
print(f"s[6:]: '{s[6:]}'")        # 'World'
print(f"s[:5]: '{s[:5]}'")        # 'Hello'
print(f"s[:]: '{s[:]}'")          # 'Hello World' (copy)

# With step
print(f"s[::2]: '{s[::2]}'")      # 'HloWrd' (every 2nd character)
print(f"s[::-1]: '{s[::-1]}'")    # 'dlroW olleH' (reverse)

# Negative indices
print(f"s[-5:]: '{s[-5:]}'")      # 'World'
print(f"s[:-6]: '{s[:-6]}'")      # 'Hello'

# ============================================================================
# 4. STRING METHODS
# ============================================================================

section_separator("4. STRING METHODS")

# Case Methods
s = "Hello World"
print(f"Original: {s}")
print(f"upper(): {s.upper()}")           # 'HELLO WORLD'
print(f"lower(): {s.lower()}")           # 'hello world'
print(f"capitalize(): {s.capitalize()}")  # 'Hello world'
print(f"title(): {s.title()}")           # 'Hello World'
print(f"swapcase(): {s.swapcase()}")     # 'hELLO wORLD'
print(f"casefold(): {s.casefold()}")     # 'hello world' (aggressive lowercase)

# Checking Methods
print(f"\nChecking methods for '{s}':")
s_test = "Hello123"

# Case checking
print(f"isupper(): {s_test.isupper()}")         # False
print(f"islower(): {s_test.islower()}")         # False
print(f"istitle(): {s_test.istitle()}")         # False

# Content checking
print(f"isalpha(): {s_test.isalpha()}")         # False (contains numbers)
print(f"isdigit(): {s_test.isdigit()}")         # False (contains letters)
print(f"isalnum(): {s_test.isalnum()}")         # True (letters and numbers)
print(f"isascii(): {s_test.isascii()}")         # True
print(f"isprintable(): {s_test.isprintable()}")  # True
print(f"isspace(): {s_test.isspace()}")         # False

# Specific checks
print(f"'123'.isdecimal(): {'123'.isdecimal()}")   # True
print(f"'123'.isnumeric(): {'123'.isnumeric()}")   # True
print(f"'hello'.isidentifier(): {'hello'.isidentifier()}")  # True (valid Python identifier)

# Search Methods
s = "Hello World Hello"
print(f"\nSearch methods for '{s}':")

# Finding
print(f"find('World'): {s.find('World')}")     # 6 (first occurrence)
print(f"rfind('Hello'): {s.rfind('Hello')}")   # 12 (last occurrence)
print(f"index('World'): {s.index('World')}")   # 6 (like find, but raises ValueError if not found)
print(f"rindex('Hello'): {s.rindex('Hello')}")  # 12

# Counting
print(f"count('Hello'): {s.count('Hello')}")    # 2
print(f"count('l'): {s.count('l')}")           # 3

# Checking existence
print(f"'World' in s: {'World' in s}")        # True
print(f"'world' in s: {'world' in s}")        # False (case-sensitive)
print(f"startswith('Hello'): {s.startswith('Hello')}")   # True
print(f"endswith('Hello'): {s.endswith('Hello')}")       # True

# Splitting and Joining
s = "apple,banana,cherry"
print(f"\nSplitting and joining with '{s}':")

# Splitting
print(f"split(','): {s.split(',')}")            # ['apple', 'banana', 'cherry']
print(f"split(',', 1): {s.split(',', 1)}")      # ['apple', 'banana,cherry'] (max splits)
print(f"'a b c'.split(): {'a b c'.split()}")    # ['a', 'b', 'c'] (default: whitespace)

# Advanced splitting
multiline_text = "hello\nworld\ntest"
print(f"'{multiline_text}'.splitlines(): {multiline_text.splitlines()}")  # ['hello', 'world', 'test']
print(f"'apple|banana'.partition('|'): {'apple|banana'.partition('|')}")       # ('apple', '|', 'banana')
print(f"'apple|banana|cherry'.rpartition('|'): {'apple|banana|cherry'.rpartition('|')}")  # ('apple|banana', '|', 'cherry')

# Joining
print(f"'-'.join(['a', 'b', 'c']): {'-'.join(['a', 'b', 'c'])}")      # 'a-b-c'
print(f"''.join(['h', 'e', 'l', 'l', 'o']): {''.join(['h', 'e', 'l', 'l', 'o'])}")  # 'hello'

# Cleaning Methods
s = "  Hello World  "
print(f"\nCleaning methods for '{s}' (with spaces):")

print(f"strip(): '{s.strip()}'")           # 'Hello World' (remove leading/trailing whitespace)
print(f"lstrip(): '{s.lstrip()}'")         # 'Hello World  ' (left strip)
print(f"rstrip(): '{s.rstrip()}'")         # '  Hello World' (right strip)
print(f"strip(' He'): '{s.strip(' He')}'") # 'llo World' (remove specific characters)

# Removing prefixes/suffixes (Python 3.9+)
try:
    print(f"'HelloWorld'.removeprefix('Hello'): {'HelloWorld'.removeprefix('Hello')}")  # 'World'
    print(f"'HelloWorld'.removesuffix('World'): {'HelloWorld'.removesuffix('World')}")  # 'Hello'
except AttributeError:
    print("removeprefix/removesuffix methods require Python 3.9+")

# Replacement Methods
s = "Hello World"
print(f"\nReplacement methods for '{s}':")

print(f"replace('World', 'Python'): {s.replace('World', 'Python')}")        # 'Hello Python'
print(f"replace('l', 'L', 1): {s.replace('l', 'L', 1)}")                    # 'HeLlo World' (replace 1 occurrence)

# Translation
table = str.maketrans("aeiou", "12345")
print(f"'hello'.translate(table): {'hello'.translate(table)}")            # 'h2ll4'

# Alignment and Padding
s = "Hello"
print(f"\nAlignment and padding for '{s}':")

print(f"center(10): '{s.center(10)}'")        # '  Hello   '
print(f"center(10, '*'): '{s.center(10, '*')}'")   # '**Hello***'
print(f"ljust(10): '{s.ljust(10)}'")         # 'Hello     '
print(f"rjust(10): '{s.rjust(10)}'")         # '     Hello'
print(f"zfill(10): '{s.zfill(10)}'")         # '00000Hello' (zero padding)

# Encoding/Decoding
s = "Hello"
print(f"\nEncoding/Decoding for '{s}':")

# Encoding to bytes
encoded_utf8 = s.encode('utf-8')
encoded_ascii = s.encode('ascii')
print(f"encode('utf-8'): {encoded_utf8}")       # b'Hello'
print(f"encode('ascii'): {encoded_ascii}")      # b'Hello'

# From bytes back to string
print(f"b'Hello'.decode('utf-8'): {b'Hello'.decode('utf-8')}")    # 'Hello'

# ============================================================================
# 5. STRING FORMATTING
# ============================================================================

section_separator("5. STRING FORMATTING")

name = "Alice"
age = 30
pi = 3.14159

# Old Style (% formatting)
print("Old Style (% formatting):")
old_style = "Hello %s, you are %d years old" % (name, age)
print(f"Basic: {old_style}")
print(f"Float: {'Value: %.2f' % pi}")     # 'Value: 3.14'
print(f"Hex: {'Hex: %x' % 255}")          # 'Hex: ff'

# str.format() Method
print(f"\nstr.format() Method:")

# Positional arguments
format_pos = "Hello {}, you are {} years old".format(name, age)
print(f"Positional: {format_pos}")

# Named arguments
format_named = "Hello {name}, you are {age} years old".format(name=name, age=age)
print(f"Named: {format_named}")

# Index-based
format_index = "Hello {0}, you are {1} years old".format(name, age)
print(f"Index-based: {format_index}")

# Formatting options
print(f"Float format: {'{:.2f}'.format(pi)}")        # '3.14'
print(f"Width: '{'{:10}'.format('hello')}'")         # 'hello     '
print(f"Right align: '{'{:>10}'.format('hello')}'")  # '     hello'
print(f"Center: '{'{:^10}'.format('hello')}'")       # '  hello   '
print(f"Fill char: '{'{:*^10}'.format('hello')}'")   # '**hello***'

# F-strings (Python 3.6+) - RECOMMENDED
print(f"\nF-strings (RECOMMENDED):")

# Basic usage
print(f"Basic: Hello {name}, you are {age} years old")

# Expressions
print(f"Expression: Next year you'll be {age + 1}")
print(f"Function call: Your name has {len(name)} letters")

# Formatting
print(f"Float format: Pi to 2 decimals: {pi:.2f}")       # 'Pi to 2 decimals: 3.14'
print(f"Alignment: Right aligned: '{name:>10}'")         # 'Right aligned:    Alice'
print(f"Hex: Hex value: {255:x}")                        # 'Hex value: ff'

# Debug feature (Python 3.8+)
x = 42
try:
    debug_output = f"{x=}"
    print(f"Debug feature: {debug_output}")             # 'x=42'
except:
    print("Debug feature (f'{x=}') requires Python 3.8+")

# Multiline f-strings
message = (
    f"Hello {name}! "
    f"You are {age} years old."
)
print(f"Multiline: {message}")

# Advanced Formatting
print(f"\nAdvanced Formatting:")

# Numbers
num = 1234567.89
print(f"Comma separator: {num:,}")              # '1,234,567.89' (comma separator)
print(f"Scientific: {num:.2e}")                 # '1.23e+06' (scientific notation)
print(f"Binary: {42:08b}")                      # '00101010' (binary with padding)

# Dates
now = datetime.now()
print(f"Date format: {now:%Y-%m-%d %H:%M:%S}")  # '2024-01-15 14:30:45'

# Percentage
ratio = 0.875
print(f"Percentage: {ratio:.1%}")               # '87.5%'

# ============================================================================
# 6. STRING OPERATIONS
# ============================================================================

section_separator("6. STRING OPERATIONS")

# Concatenation
print("Concatenation:")
print(f"Using +: {'Hello' + ' ' + 'World'}")     # 'Hello World'

# Using +=
s = "Hello"
s += " World"
print(f"Using +=: {s}")               # s is now 'Hello World'

# Using join (more efficient for many strings)
joined = " ".join(["Hello", "World"])
print(f"Using join: {joined}")    # 'Hello World'

# Repetition
print(f"\nRepetition:")
print(f"'Hi' * 3: {'Hi' * 3}")                    # 'HiHiHi'
print(f"'=' * 20: {'=' * 20}")                    # '===================='

# Membership
s = "Hello World"
print(f"\nMembership testing with '{s}':")
print(f"'World' in s: {'World' in s}")                # True
print(f"'world' in s: {'world' in s}")                # False
print(f"'xyz' not in s: {'xyz' not in s}")            # True

# ============================================================================
# 7. ESCAPE SEQUENCES
# ============================================================================

section_separator("7. ESCAPE SEQUENCES")

print("Common Escape Sequences:")
print("Newline: Hello\\nWorld ->", end=" ")
print("Hello\nWorld")
print("Tab: Hello\\tWorld ->", end=" ")
print("Hello\tWorld")
print("Backslash: Hello\\\\World ->", end=" ")
print("Hello\\World")
print("Double quote: He said \\\"Hello\\\" ->", end=" ")
print("He said \"Hello\"")
print("Single quote: It\\'s working ->", end=" ")
print('It\'s working')
print("Carriage return: Hello\\rWorld ->", end=" ")
print("Hello\rWorld")

# Unicode Escapes
print(f"\nUnicode Escapes:")
print(f"\\u0041: {chr(65)} (Unicode code point)")            # 'A' (Unicode code point)
print(f"\\U00000041: {chr(65)} (32-bit Unicode)")            # 'A' (32-bit Unicode)

# ============================================================================
# 8. RAW STRINGS
# ============================================================================

section_separator("8. RAW STRINGS")

# Regular string (escapes processed)
try:
    path_wrong = "C:\new\folder"      # Problem: \n is newline
    print(f"Regular string: {repr(path_wrong)}")
except:
    pass

# Raw string (escapes ignored)
path_correct = r"C:\new\folder"     # Correct
print(f"Raw string: {path_correct}")

# Useful for regex
pattern = r"\d+\.\d+"       # Matches decimal numbers
print(f"Regex pattern: {pattern}")

# ============================================================================
# 9. STRING COMPARISON
# ============================================================================

section_separator("9. STRING COMPARISON")

# Basic Comparison
print("Basic Comparison:")
print(f"'apple' == 'apple': {'apple' == 'apple'}")          # True
print(f"'apple' == 'Apple': {'apple' == 'Apple'}")          # False
print(f"'apple' < 'banana': {'apple' < 'banana'}")          # True (lexicographic)
print(f"'10' < '2': {'10' < '2'}")                          # True (string comparison, not numeric)

# Case-Insensitive Comparison
s1 = "Hello"
s2 = "HELLO"
print(f"\nCase-insensitive comparison:")
print(f"s1.lower() == s2.lower(): {s1.lower() == s2.lower()}")    # True
print(f"s1.casefold() == s2.casefold(): {s1.casefold() == s2.casefold()}")  # True (better for international)

# ============================================================================
# 10. STRING CONSTANTS
# ============================================================================

section_separator("10. STRING CONSTANTS")

print("String constants from string module:")
print(f"ascii_letters: {string.ascii_letters}")        # 'abcdefghijklmnopqrstuvwxyzABC...'
print(f"ascii_lowercase: {string.ascii_lowercase}")     # 'abcdefghijklmnopqrstuvwxyz'
print(f"ascii_uppercase: {string.ascii_uppercase}")     # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(f"digits: {string.digits}")                      # '0123456789'
print(f"punctuation: {string.punctuation}")            # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(f"whitespace: {repr(string.whitespace)}")        # ' \t\n\r\x0b\x0c'
print(f"printable length: {len(string.printable)}")    # All printable characters

# ============================================================================
# 11. REGULAR EXPRESSIONS
# ============================================================================

section_separator("11. REGULAR EXPRESSIONS")

text = "The phone number is 123-456-7890"
print(f"Text: {text}")

# Finding patterns
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if match:
    print(f"Found phone number: {match.group()}")

numbers = re.findall(r'\d+', text)               # ['123', '456', '7890']
print(f"All numbers: {numbers}")

# Replacing with regex
replaced = re.sub(r'\d', 'X', text)               # 'The phone number is XXX-XXX-XXXX'
print(f"Digits replaced: {replaced}")

# Splitting with regex
parts = re.split(r'[-\s]', text)               # Split on hyphens and spaces
print(f"Split on hyphens and spaces: {parts}")

# ============================================================================
# 12. PERFORMANCE TIPS
# ============================================================================

section_separator("12. PERFORMANCE TIPS")

import time

# Demonstrate efficient string building
print("String Building Performance:")

# Inefficient method (commented out as it's slow)
# start = time.time()
# result = ""
# for i in range(1000):
#     result += str(i)
# inefficient_time = time.time() - start
# print(f"Inefficient (+=): {inefficient_time:.4f} seconds")

# Efficient method
start = time.time()
result = "".join(str(i) for i in range(1000))
efficient_time = time.time() - start
print(f"Efficient (join): {efficient_time:.4f} seconds")

# Using list and join
start = time.time()
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)
list_join_time = time.time() - start
print(f"List and join: {list_join_time:.4f} seconds")

# String Interning
print(f"\nString Interning:")
a = "hello"
b = "hello"
print(f"a is b: {a is b}")                      # True (same object in memory)

# Manual interning for optimization
a_interned = sys.intern("some long string")
b_interned = sys.intern("some long string")
print(f"Manually interned strings are same object: {a_interned is b_interned}")  # True

# ============================================================================
# 13. COMMON PATTERNS
# ============================================================================

section_separator("13. COMMON PATTERNS")

# Validation Functions
def is_valid_email(email):
    """Simple email validation"""
    return "@" in email and "." in email.split("@")[1]

def is_phone_number(phone):
    """Check if string contains exactly 10 digits"""
    digits = "".join(filter(str.isdigit, phone))
    return len(digits) == 10

def is_strong_password(password):
    """Check for strong password criteria"""
    return (len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password))

print("Validation Examples:")
print(f"Valid email 'user@example.com': {is_valid_email('user@example.com')}")
print(f"Valid phone '123-456-7890': {is_phone_number('123-456-7890')}")
print(f"Strong password 'MyPass123': {is_strong_password('MyPass123')}")

# Text Processing Functions
def clean_text(text):
    """Clean and normalize text"""
    return " ".join(text.strip().split())

def title_case(text):
    """Convert to title case, handling special cases"""
    return " ".join(word.capitalize() for word in text.split())

def extract_numbers(text):
    """Extract all numbers from text"""
    return [int(s) for s in text.split() if s.isdigit()]

print(f"\nText Processing Examples:")
messy_text = "  hello    world   extra   spaces  "
print(f"Clean text: '{clean_text(messy_text)}'")
print(f"Title case: '{title_case('hello world python')}'")
print(f"Extract numbers: {extract_numbers('I have 5 apples and 10 oranges')}")

# File Extension Functions
def get_file_extension(filename):
    """Get file extension"""
    return filename.split(".")[-1] if "." in filename else ""

def change_extension(filename, new_ext):
    """Change file extension"""
    base = filename.rsplit(".", 1)[0] if "." in filename else filename
    return f"{base}.{new_ext}"

print(f"\nFile Extension Examples:")
print(f"Extension of 'document.pdf': '{get_file_extension('document.pdf')}'")
print(f"Change to .txt: '{change_extension('document.pdf', 'txt')}'")

# URL Processing Functions
def extract_domain(url):
    """Extract domain from URL"""
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    return url.split("/")[0]

def build_query_string(params):
    """Build URL query string from dictionary"""
    return "&".join(f"{k}={v}" for k, v in params.items())

print(f"\nURL Processing Examples:")
print(f"Domain: '{extract_domain('https://www.example.com/page')}'")
query_params = {"name": "John", "age": "30", "city": "NYC"}
print(f"Query string: '{build_query_string(query_params)}'")

# Data Formatting Functions
def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def format_percentage(decimal):
    """Format decimal as percentage"""
    return f"{decimal:.1%}"

def truncate_string(text, max_length, suffix="..."):
    """Truncate string with suffix"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

print(f"\nData Formatting Examples:")
print(f"Currency: {format_currency(1234567.89)}")
print(f"Percentage: {format_percentage(0.875)}")
long_text = "This is a very long string that needs to be truncated"
print(f"Truncated: '{truncate_string(long_text, 20)}'")

# ============================================================================
# QUICK REFERENCE
# ============================================================================

section_separator("QUICK REFERENCE")

print("Most Used String Methods:")
reference_methods = [
    "s.strip()           # Remove whitespace",
    "s.split()           # Split into list", 
    "s.replace(old, new) # Replace substring",
    "s.find(sub)         # Find substring position",
    "s.startswith(pre)   # Check prefix",
    "s.endswith(suf)     # Check suffix",
    "s.upper()           # Convert to uppercase",
    "s.lower()           # Convert to lowercase",
    "len(s)              # Get length",
    "s in text           # Check membership"
]

for method in reference_methods:
    print(method)

print(f"\nF-string Formatting Quick Reference:")
formatting_examples = [
    'f"{value}"          # Basic',
    'f"{value:10}"       # Width 10',
    'f"{value:<10}"      # Left align',
    'f"{value:>10}"      # Right align', 
    'f"{value:^10}"      # Center align',
    'f"{value:.2f}"      # 2 decimal places',
    'f"{value:,}"        # Comma separator',
    'f"{value:%}"        # Percentage',
    'f"{value:x}"        # Hexadecimal'
]

for example in formatting_examples:
    print(example)

print(f"\n{'='*60}")
print(" END OF PYTHON STRINGS REFERENCE")
print('='*60)

if __name__ == "__main__":
    print("\nThis file contains a complete reference for Python strings.")
    print("You can run it to see all examples, or copy specific sections.")
    print("All code examples are functional and ready to use!")