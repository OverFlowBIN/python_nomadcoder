def say_hello(name, age):
  return f"Hello {name} you are {age} years old"
  # 또는 return "Hello" + name + "you are" + age + "years old"

hello = say_hello(name='alex', age='23')
print(hello)

# keyworded arguments를 사용하게 되면 인자의 위치와 상관없이 작동이 된다.