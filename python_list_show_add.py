mylist = []

print("""

█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀
█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀
░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀
""")


print("""
- type show for showing the list names -
- type exit to exit or q the program -
""")

while True:

    friends_inp = input("- Enter The Name Of Your Friends: ")


    if friends_inp == "":

        continue

    friends = friends_inp.capitalize().split()

    if friends[-1] == "Show":

        for i in mylist:

            print(f"- {i} -")

    elif friends[-1] == "Exit" or friends[-1] == "Q":

        print("- Close The Program -")

        break

    else:

        mylist.append(friends)

