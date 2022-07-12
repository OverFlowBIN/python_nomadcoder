def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)

# javascript에서는 리턴값이 없는 함수의 결과값으로 undefined가 나오지만
# python에서는 None으로 나온다.