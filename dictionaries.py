student_Id = {
    1: "Reeves",
    2: "LeToya",
    3: "Tyrion",
    4: "Diana",
    6: "Idiong"
}
print(student_Id)
student_Id[9] = "Bassey"
print(student_Id)
student_Id[6] = "Skippy"
print(student_Id)
print(student_Id[1])

# Nested dictionary.
bio_data = {
    "Skip": {'name': 'Skippy', 'age': '10', 'sex': 'Male'},
    "Rey": {'name': 'Reeves', 'age': '27', 'sex': 'Male'},
    "Ty": {'name': 'Tyrion', 'age': '1', 'sex': 'Male'},
}

print(bio_data)
for k, v in bio_data.items():
    print(k, ":", v)


print(student_Id.keys())
del student_Id[6]
print(student_Id)
