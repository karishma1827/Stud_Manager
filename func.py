from util import*

def registeration(username,age,address,course,duration):
    data=read_json()

    temp_data={
        "sno":len(data["students"])+1,
        "username":username,
        "age":age,
        "address":address,
        "course":course,
        "duration":duration

    }

    data["students"].append(temp_data)
    write_json(data)
    print()