# 4

def delete_keys(delete_list,dictionary):
    for a in delete_list:
        dictionary.pop(a)
    return dictionary
dict = {"firstName":"Mohanmed","lastName":"Farag","birthYear":1990,"nationality":"Egyptian"}
print(delete_keys(["lastName","birthYear"],dict))