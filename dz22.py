import re
test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
print(re.findall(r'\+?7\d{10}', test))
print("New")




