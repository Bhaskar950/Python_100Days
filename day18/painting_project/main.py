import colorgram

colors = colorgram.extract("heist.jpg",45)

rgb_colors = []

for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)