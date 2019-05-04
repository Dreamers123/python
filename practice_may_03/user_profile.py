def build_profile(first_name,last_name,**info):
    profile={}
    profile['first_name']=first_name
    profile['last_name']=last_name
    for key,value in info.items():
        profile[key]=value
    return profile
profile1=build_profile("Abeer","Azad",location="Dhaka",Sex="Male")
print(profile1)