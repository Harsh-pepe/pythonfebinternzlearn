def greet():
    print("Hello, welcome to Python!")
greet()


def greet_user(name):
    print(f'Hello, {name}')


names=["Harsh","Alice","Rahul","Saranya","Rakshit", "Dharshini","Charitha"]
for i in names:
    greet_user(i)