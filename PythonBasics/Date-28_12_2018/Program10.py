keys=['S','T','G','F','R']
values=['Sony','TestYantra','Google','Facebook','RollsRoyce']
# keys_values=zip(keys,values)
# print(list(keys_values))
Dict = { k:v for (k,v) in zip(keys, values)}
print(Dict)