
my_dict = {
    "name": range(1,10),
    "age": list(range(1,100)),
    "class_name":set(range(1,5)),
}


#* dict API

# add value

my_dict["major"] = "computer"


# remove  value

my_dict.pop("age")


# get all keys

all_keys = my_dict.keys()

print(f"all keys is {all_keys}")
# clear dict 

# len of dict

print(f"len of dict is {len(my_dict)}")


my_dict.clear()

print(my_dict)