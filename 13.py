scores = [68, 74, 83]
avg = sum(scores) / len(scores)
if avg >= 75:
     print(f"Average: {avg:g} - Passed")
else:
     print(f"Average: {avg:g} - Failed")