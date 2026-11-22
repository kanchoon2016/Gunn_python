angle3 = 180 - 35 - 55
if angle3 == 90:
    kind = "Right Triangle"
elif angle3 > 90:
     kind = "Obtuse Triangle"
else:
     kind = "Acute Triangle"
print(f"Third angle: {angle3} degrees; {kind}")