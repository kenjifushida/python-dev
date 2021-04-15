from collections import defaultdict
 
service = [ ('circle', 1), ('square', 2), ('circle', 1), ('circle', 3), ('square', 3)]
service_dict = defaultdict(list)
 
for k, v in service:
    service_dict[k].append(v)

print(service_dict)