from faker import Faker

# Aby działało musi być zainstalowana biblioteka faker
if __name__ == "__main__":
    faker = Faker()
    print(faker.name())
