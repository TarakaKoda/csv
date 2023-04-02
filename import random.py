import random
# import os

# value = random.random()
# print(round(value, 2))

# value = random.uniform(1,10)
# print(value)

# value = random.randint(1,6)
# print(value)

# coin = random.randint(0,1)
# print(coin)

# greetings = ["hello","hi", "hola", "dattebayo", "konichiwa"]
# result = random.choice(greetings)
# print(f"{result}!, srinu")

# colors = ["Red", "Black", "Green"]
# result = random.choices(colors, weights=[18, 18, 2], k=10)
# print(result)

deck = list(range(1,53))
# random.shuffle(deck)
# print(deck)

hand = random.sample(deck, k=5)
# print(hand)

first_names = ['Venkatesh', 'Srinivas', 'Rama Rao', 'Krishna', 'Narayana', 'Siva', 'Ravi', 'Kumar', 'Raju', 'Prasad', 'Suresh', 'Satyanarayana', 'Mohan', 'Vishnu', 'Ramana', 'Subba Rao', 'Madhu', 'Mahesh', 'Vijay', 'Jagannath']

last_names = ['Reddy', 'Rao', 'Naidu', 'Kumar', 'Sharma', 'Pillai', 'Patel', 'Mishra', 'Gupta', 'Singh', 'Khan', 'Mohan', 'Raj', 'Nair', 'Menon', 'Panicker', 'Kurup', 'Menon', 'Menon', 'George']

street_names = ['Dwaraka Nagar Main Road', 'Waltair Main Road', 'MVP Double Road', 'Siripuram Main Road', 'Beach Road', 'Lawsons Bay Colony Road', 'Gajuwaka Main Road', 'Sampath Vinayaka Temple Road', 'Sriharipuram Main Road', 'Rama Talkies Road', 'Diamond Park Road', 'Gurudwara Junction Road', 'Jagadamba Junction Road', 'Asilmetta Junction Road', 'Pandurangapuram Main Road', 'Madhurawada-Vizag Expressway', 'Resapuvanipalem Main Road', 'Kancharapalem Main Road', 'NAD X Road', 'Akkayyapalem Main Road']

fake_cities = ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Rajahmundry', 'Tirupati', 'Kakinada', 'Nellore', 'Kurnool', 'Kadapa', 'Anantapur', 'Eluru', 'Ongole', 'Machilipatnam', 'Tenali', 'Adoni', 'Hindupur', 'Proddatur', 'Chittoor', 'Srikakulam', 'Bhimavaram']

state = 'Andhra Pradesh'

for num in range(20):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone_no = f"91-{random.randint(9000000000,9999999999)}"

    street_num = random.randint(100,999)
    street = random.choice(street_names)
    cites = random.choice(fake_cities)
    zip_code = random.randint(530000,530098)
    address = f"{street_num} {street} {cites} {state} {zip_code}"

    email = first.lower() + last.lower() + '@fakegmail.com'

    # print(f"{first} {last}\n{phone_no}\n{address}\n{email.strip()}\n")
    with open("sample data.csv", "a") as wf:
        wf.seek(1)
        wf.write(f"{first},{last},{email}\n")
#
# os.rename("csv.csv","sample data.csv")