# ch9_29.py
fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print(f"Value = {ret_value1}")
ret_value2 = fruits.get('Grape')
print(f"Value = {ret_value2}")
ret_value3 = fruits.get('Grape', 10)
print(f"Value = {ret_value3}")

