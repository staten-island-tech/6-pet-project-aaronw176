wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}

def find(dept):
    for ward, value in wards.items():
        for people in value:
            if people in staff:
                staff[ward] = {
                    ward
                }
            else:
                staff[people] = {
                    'Ward' : ward
                }
    print(staff)
        

find("bob")