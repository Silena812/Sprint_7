from faker import Faker
fake = Faker("ru_RU")

def generate_login():
    login = fake.user_name()
    return login

def generate_password():
    password = fake.password(7)
    return password

def generate_name():
    name = fake.name()
    return name