n = int(input("enter number of resources requests:"))
requests = [0]*n
for i in range(n):
    requests[i] = int(input("enter your request value:"))
low_demand =[]
moderate_demand =[]
high_demand=[]
invalid_requests=[]
valid_count = 0
for r in requests:

    if r<0:
        invalid_requests.append(r)
    elif r == 0:
        pass
    elif r >= 1 and r <= 20:
        low_demand.append(r)
        valid_count = valid_count+1
    elif r>=21 and r<= 49:
        moderate_demand.append(r)
        valid_count = valid_count+1
    else:
        high_demand.append(r)
        valid_count = valid_coun

BY = int(input("Enter your birth year:"))
PLI = BY%3
removed_count = 0
if PLI == 0:
    removed_count = len(low_demand)
    low_demand =[]
elif PLI == 1:
    removed_count = len(high_demand)
    high_demand = []
else:
    removed_count = len(low_demand)+len(high_demand)
    high_demand = []
    low_demand = []
print("Dispatch Report")
print("Birth Year:",BY)
print("PLI :",PLI)
print("Low Demand:",low_demand)
print("Moderate Demand:",moderate_demand)
print("High Demand:",high_demand)
print("Invalid Requests:",invalid_requests)
print("Valid Requests:",valid_count)
print("Removed Requests:",removed_count)
