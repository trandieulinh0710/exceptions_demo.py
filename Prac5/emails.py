def main():
    names_and_emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        names_and_emails[name] = email
        email = input("Email: ")

    for name, email in names_and_emails.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    prefix = email.split('@')[0]
    f_l_name = prefix.split('.')
    name = " ".join(f_l_name).title()
    return name


main()
