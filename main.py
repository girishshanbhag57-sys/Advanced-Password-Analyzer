import re
import math
import string
import pandas as pd
import matplotlib.pyplot as plt

password = input("Enter password to analyze: ")

print("Password received for analysis.")

def check_length(password):
    length = len(password)

    if length >= 12:
        return 2
    elif length >= 8:
        return 1
    else:
        return 0


length_score = check_length(password)

print("Length:", len(password))
print("Length Score:", length_score)

def complexity_check(password):

    score = 0
    checks = {}

    checks["Uppercase"] = bool(re.search(r"[A-Z]", password))
    checks["Lowercase"] = bool(re.search(r"[a-z]", password))
    checks["Numbers"] = bool(re.search(r"[0-9]", password))
    checks["Special Characters"] = bool(re.search(r"[^A-Za-z0-9]", password))


    for key,value in checks.items():
        if value:
            score += 1

    return score, checks



complexity_score, result = complexity_check(password)

print(result)
print("Complexity Score:", complexity_score)

common_passwords = [
    "password",
    "123456",
    "admin",
    "qwerty",
    "password123"
]


def common_password_check(password):

    if password.lower() in common_passwords:
        return True
    
    return False



if common_password_check(password):
    print("Password exists in common password list")
else:
    print("Password is not commonly used")

def pattern_detection(password):

    warnings=[]

    if re.search(r"(.)\1\1", password):
        warnings.append("Repeated characters detected")


    if re.search(r"123|abc|qwe", password.lower()):
        warnings.append("Predictable sequence detected")


    return warnings



warnings = pattern_detection(password)


for warning in warnings:
    print("!!",warning)

def calculate_entropy(password):

    charset = 0


    if re.search("[a-z]",password):
        charset += 26

    if re.search("[A-Z]",password):
        charset += 26

    if re.search("[0-9]",password):
        charset += 10

    if re.search("[^A-Za-z0-9]",password):
        charset += 32


    entropy = len(password) * math.log2(charset)

    return round(entropy,2)



entropy = calculate_entropy(password)

print("Password Entropy:",entropy,"bits")

def brute_force_time(password):

    charset = 0


    if re.search("[a-z]",password):
        charset += 26

    if re.search("[A-Z]",password):
        charset += 26

    if re.search("[0-9]",password):
        charset += 10

    if re.search("[^A-Za-z0-9]",password):
        charset += 32


    possible_combinations = charset ** len(password)


    attack_speed = 10**9   # 1 billion guesses/sec


    seconds = possible_combinations / attack_speed


    years = seconds/(60*60*24*365)


    return years



years = brute_force_time(password)


print("Estimated brute force resistance:")
print(round(years,2),"years")

total_score = length_score + complexity_score


print("\n========== SECURITY REPORT ==========")

print("Password Length:",len(password))
print("Entropy:",entropy,"bits")
print("Score:",total_score,"/6")


if total_score <=2:
    print("Security Level: Weak")

elif total_score <=4:
    print("Security Level: Medium")

else:
    print("Security Level: Strong")

features = {
    "Length": length_score,
    "Complexity": complexity_score,
    "Entropy": entropy/20
}


plt.figure(figsize=(7,4))

plt.bar(features.keys(),features.values())

plt.title("Password Security Analysis")
plt.ylabel("Score")

plt.show()