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
    
def remove(id):
    data=read_json()
    name=""
    for stud in data["students"]:
        if stud["sno"]==int(id):
            name=stud["username"]
            data["students"].remove(stud)
    
    i=1
    for stud in data["students"]:
        stud["sno"]=i
        i+=1
    write_json(data)
    return name
            
            