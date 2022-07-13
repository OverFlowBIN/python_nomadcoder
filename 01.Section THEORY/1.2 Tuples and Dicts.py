# Tuple => immutable
days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))  # tuple


# dictionary
alex = {
  "name" : "Alex",
  "age" : 29,
  "Korean" : True,
  "fav_food" : ["kimchi", "Ssashimi"]  
}

print(alex['fav_food'])
alex["hansome"] = True
print(type(alex))
