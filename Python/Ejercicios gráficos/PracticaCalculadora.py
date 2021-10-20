year_of_birth=int(input("Date of birth: "))
current_year=int(input("Actual Date: "))

if year_of_birth==current_year:
    print("You were born this very year!")

elif year_of_birth==current_year-1:
    print("You are "+ str((year_of_birth-current_year)*-1) + " year old!")

elif year_of_birth<=current_year:
    print("You are "+ str((year_of_birth-current_year)*-1) + " years old!")

elif year_of_birth>=current_year:
    print("You will be born in " + str(year_of_birth-current_year) + " Years. ")
