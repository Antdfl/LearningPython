countries = ["USA", "Canada", "Mexico"]

# Create a tuple
countries_tuple = ("USA", "Canada", "Mexico")
print(type(countries_tuple))  # Output: <class 'tuple'>

countries_tuple2 = "USA", "Canada", "Mexico"
print(type(countries_tuple2))  # Output: <class 'tuple'>

countries_tuple3 = ("onlyone")
print(type(countries_tuple3))  # Output: <class 'str'>

# If we add the trailing comma to a single value, it becomes a tuple
countries_tuple4 = ("onlyone",)
print(type(countries_tuple4))  # Output: <class 'tuple'>

# How to access elements. It's similar to lists
tuple1 = (1200,2500)
print(tuple1[0])  # Output: 1200

print(tuple1[1:])  # Output: 2500
print(tuple1[:1])  # Output: 1200
