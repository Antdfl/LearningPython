import colorgram

# Example: Extract colors from an image
colors = colorgram.extract("image.jpg", 6)

# Print the colors
for color in colors:
    print(color)