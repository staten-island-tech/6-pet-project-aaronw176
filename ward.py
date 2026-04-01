wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
staffward = []
for ward, value in wards.items():
    for people in value:
        if people not in staff:
            staff[people] = []
        staff[people].append(ward)
print(staff['Bob'])
        
