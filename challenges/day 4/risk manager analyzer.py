n = int(input("Enter number of activity scores:"))

score = [0] * n

for i in range(n):
    score[i] = int(input("enter your score:"))

D = int(input("enter the your registration number :"))

low_risk = [0] * n
medium_risk = [0] * n
high_risk = [0] * n
critical_risk = [0] * n

low_count = 0
medium_count = 0
high_count = 0
critical_count = 0

valid_entires = 0
igonred_entires = 0
removed_entires = 0


for i in range(n):

    scores = score[i]   # read value correctly

    if scores < 0:
        igonred_entires = igonred_entires + 1

    else:
        valid_entires = valid_entires + 1

        if scores <= 30:
            low_risk[low_count] = scores
            low_count = low_count + 1

        elif scores <= 60:
            medium_risk[medium_count] = scores
            medium_count = medium_count + 1

        elif scores <= 100:
            high_risk[high_count] = scores
            high_count = high_count + 1

        else:
            critical_risk[critical_count] = scores
            critical_count = critical_count + 1


print("before personalized filter:")

print("Low Risk:", end=" ")
for i in range(low_count):
    print(low_risk[i], end=" ")
print()

print("Medium Risk:", end=" ")
for i in range(medium_count):
    print(medium_risk[i], end=" ")
print()

print("High Risk:", end=" ")
for i in range(high_count):
    print(high_risk[i], end=" ")
print()

print("Critical Risk:", end=" ")
for i in range(critical_count):
    print(critical_risk[i], end=" ")
print()


if D % 2 == 0:
    removed_entires = removed_entires + low_count
    low_count = 0

else:
    removed_entires = removed_entires + high_count
    high_count = 0


print("After personalized filter:")

print("Low Risk:", end=" ")
for i in range(low_count):
    print(low_risk[i], end=" ")
print()

print("Medium Risk:", end=" ")
for i in range(medium_count):
    print(medium_risk[i], end=" ")
print()

print("High Risk:", end=" ")
for i in range(high_count):
    print(high_risk[i], end=" ")
print()

print("Critical Risk:", end=" ")
for i in range(critical_count):
    print(critical_risk[i], end=" ")
print()


print("Final Security Report:")
print("Total Valid Entries:", valid_entires)
print("Ignored entries:", igonred_entires)
print("Removed entires:", removed_entires)
