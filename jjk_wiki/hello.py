name = input("name: ")
age = int (input("Age: "))
print(f"hello, {name}")

if age < 18:
    print("Pretty young age")
elif age >= 18:
    print("You are an adult sort off")
elif age > 20:
    print("get a job")
else:
    print("you are old")
