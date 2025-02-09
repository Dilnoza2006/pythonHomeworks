from datetime import datetime 
name = input ("  name:")
date_of_birth = int(input("enter your birth year:"))
current_year = datetime.now().year
age = current_year - date_of_birth
print("hello," ,name, ",you are ", age,"years old.")