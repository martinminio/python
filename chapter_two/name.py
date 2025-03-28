name="ada lovelace"
print(name.title()) # prints the value in title case
print(name.upper()) # prints the value in upper case
print(name.lower()) # prints the value in lower case

first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}" #f-strings are formatted strings. They are used to insert variables into strings
print(full_name.title())
print(f"Hello, {full_name.title()}") # you can perform operations within f-strings inside the curly braces

message=f"Hello, {full_name.title()}" # you can also store the formatted string in a variable
print(message)

message=f"{full_name.title()} loves:\n\tSports\n\tProgramming\n\tGoing out with friends" # \n is used to insert a new line and \t is used to insert a tab
print(message)

programming_language="Python "
print(programming_language.rstrip()) # rstrip() removes the whitespace from the right side of the string
programming_language=" Python"
print(programming_language.lstrip()) # lstrip() removes the whitespace from the left side of the string
programming_language=" Python "
print(programming_language.strip()) # strip() removes the whitespace from both sides of the string

gmail_url="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox/FMfcgzQZTqBMGKnmnGkJnvJcsJGGdZld"
gmail_url_no_prefix=gmail_url.removeprefix("https://") # removeprefix() removes the specified prefix from the string
print(gmail_url_no_prefix)

