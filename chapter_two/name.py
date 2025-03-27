name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}")

message=f"Hello, {full_name.title()}"
print(message)

message=f"{full_name.title()} loves:\n\tSports\n\tProgramming\n\tGoing out with friends"
print(message)

programming_language="Python "
print(programming_language.rstrip())

gmail_url="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox/FMfcgzQZTqBMGKnmnGkJnvJcsJGGdZld"
gmail_url_no_prefix=gmail_url.removeprefix("https://")
print(gmail_url_no_prefix)

