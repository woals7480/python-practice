from faker import Faker

faker = Faker('ko-KR')
print(faker.name())
print(faker.address())
print(faker.text())