import validators

def main():
    email = input("What is you email adsress? ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")



main()

