# Import necessary packages.
import random
import csv
import os

# Import necessary modules.
from faker import Faker

# Create Faker instance with Romanian data.
fake = Faker("ro_RO")


def generate_batch() -> list:

    batch_data = []

    person_name = fake.name()
    user_name = "".join(person_name.split(" ")).lower()
    email = user_name + "@" + fake.free_email_domain()
    personal_number = fake.ssn()
    birth_date = fake.date_of_birth()
    address = fake.address().replace("\n", ", ")
    phone_number = fake.phone_number()
    mac_address = fake.mac_address()
    ip_address = fake.ipv4()
    iban = fake.iban()
    accessed_at = fake.date_time_between("-1y")
    download_speed = random.randint(0, 1000)
    upload_speed = random.randint(0, 800)

    batch_data.append(person_name)
    batch_data.append(user_name)
    batch_data.append(email)
    batch_data.append(personal_number)
    batch_data.append(birth_date)
    batch_data.append(address)
    batch_data.append(phone_number)
    batch_data.append(mac_address)
    batch_data.append(ip_address)
    batch_data.append(iban)
    batch_data.append(accessed_at)
    batch_data.append(download_speed)
    batch_data.append(upload_speed)

    return batch_data


with open("batch.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    header_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    writer.writerow(header_data)

    # Write generated data
    for row in range(10):
        writer.writerow(generate_batch())
