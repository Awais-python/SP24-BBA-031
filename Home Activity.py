#Home Activity 1
marks = int(input("Enter marks (1-100): "))

if marks < 50:
    grade = 'F'
elif marks <= 60:
    grade = 'E'
elif marks <= 70:
    grade = 'D'
elif marks <= 80:
    grade = 'C'
elif marks <= 90:
    grade = 'B'
elif marks <= 100:
    grade = 'A'
else:
    grade = 'Invalid Marks'

print("Grade:", grade)

#Home Activity 2

temperature = float(input("Enter temperature in centigrade: "))

if temperature < 0:
    message = 'FREEZING'
elif temperature <= 15:
    message = 'COLD'
elif temperature <= 30:
    message = 'WARM'
elif temperature <= 40:
    message = 'HOT'
else:
    message = 'VERY HOT'

print("Temperature Condition:", message)