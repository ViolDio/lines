#1
immutable_var =["good", True, 2]
print(immutable_var)

#2
#immutable_var = "good", True, 2
#print(immutable_var)
#immutable_var[2] = 3
#print(immutable_var)
#Значения можно поменять только если они находятся в списке. Внизу правильная операция

immutable_var = ["good", True, 2]
print(immutable_var)
immutable_var[2] = 3
print(immutable_var)

#3
mutable_list =["good", "bad", "nice"]
mutable_list.append (False)
print(mutable_list)

