# Original dictionary
people = {
    "Alice": 20,
    "Bob": 15,
    "Charlie": 25,
    "David": 17
}

# Dictionary with only people aged 18 or older
adults = {name: age for name, age in people.items() if age >= 18}

# Dictionary with ages written as strings
age_text = {name: str(age) + " years old" for name, age in people.items()}

# Print the dictionaries
print("Original Dictionary:", people)
print("Adults:", adults)
print("Age Text:", age_text)