# Pay Calculator Week 3 Lecture
hours_worked = int(input("How many hours did you work? "))
normal_rate = 51.45
overload_rate = 88.9

if hours_worked <= 35:
    pay = hours_worked * normal_rate
elif hours_worked > 35:
    pay = (35 * normal_rate) + ((hours_worked - 35) * overload_rate)
print(f"Your weekly payment is {pay}")

# Find largest number
numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
largest = max(numbers)
print(f"Largest number is {largest}")

s = {'a'}
if 'a' in s or 'b' not in s:
    print("hello2")
    #a("There")

prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = sorted([key if key != '3000-01-15' else '2020-01-15' for key in prc_dic])
#sorted_keys.sort()

print(sorted_keys)

APIKEY = 'abcdcf'


def meme(n, m):
    r = n
    for i in range(2, m+1):
        r = r*n
    return r

print(meme(10, 7))