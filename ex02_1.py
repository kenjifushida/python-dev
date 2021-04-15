import random
from collections import deque, defaultdict

ctime = 0
customer = (0, 0) #customer no 0 coming at time 0

queue = deque()

servers = [ None, None, None, None ]

serviced = defaultdict(list)

while ctime < 100:

    # if the current time is at a customer coming time,
    # add the customer to the queue
    # generate a future customer event
    if ctime == customer[1]:
        queue.append(customer)
        customer = (customer[0]+1, ctime + random.randint(1, 25))

    for n in range(4):
        if servers[n]:
            if ctime == servers[n][2]: # the current time is the service finish time
                serviced[n].append(servers[n])

    for n in range(4):
        if queue and not servers[n]:
            service_customer = queue.pop()
            servers[n] = (service_customer, ctime, ctime + random.randint(1, 100))

    ctime += 1

print(queue)
print(servers)
print(serviced)