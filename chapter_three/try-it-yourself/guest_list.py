guests = ['John Lennon', 'Donald Trump', 'Dario Z' ]
invitation_one = f"Mr {guests[0]}, you are invited to my dinner"
invitation_two = f"Mr {guests[1]}, you are invited to my dinner"
invitation_three = f"Mr {guests[2]}, you are invited to my dinner"

print(invitation_one)
print(invitation_two)
print(invitation_three)

print(f"\n\n{guests[1]} will not be present at the dinner")

del guests[1]

guests.append('Lionel Messi')

invitation_one = f"Mr {guests[0]}, you are invited to my dinner"
invitation_two = f"Mr {guests[1]}, you are invited to my dinner"
invitation_three = f"Mr {guests[2]}, you are invited to my dinner"
print(invitation_one)
print(invitation_two)
print(invitation_three)

print("\n\nI found a bigger table so more guests are coming")

guests.insert(0, 'Shakira')
guests.insert(3, 'David Lynch')
guests.append('Tinelli')

invitation_one = f"Mr {guests[0]}, you are invited to my dinner"
invitation_two = f"Mr {guests[1]}, you are invited to my dinner"
invitation_three = f"Mr {guests[2]}, you are invited to my dinner"
invitation_four = f"Mr {guests[3]}, you are invited to my dinner"
invitation_five = f"Mr {guests[4]}, you are invited to my dinner"
invitation_six = f"Mr {guests[5]}, you are invited to my dinner"

print(invitation_one)
print(invitation_two)
print(invitation_three)
print(invitation_four)
print(invitation_five)
print(invitation_six)

print("\nMy new dinner table won't be arriving on time sadly")
print(f"\nSorry {guests.pop()}, I can't have you to my dinner")
print(f"\nSorry {guests.pop()}, I can't have you to my dinner")
print(f"\nSorry {guests.pop()}, I can't have you to my dinner")
print(f"\nSorry {guests.pop()}, I can't have you to my dinner")

print(f"\nFortunately, {guests[1]}, I can have you to my dinner")
print(f"\nFortunately {guests[0]}, I can have you to my dinner")

del guests[1]
del guests[0]

print(guests)

print(f"I'm inviting {len(guests)} to my dinner")


