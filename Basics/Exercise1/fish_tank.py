length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = (length * width * height) * 0.001

water_needed = volume - (volume*(percentage*0.01))
print(water_needed)