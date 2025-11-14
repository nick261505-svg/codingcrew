def process_data(data_list):
    result = {}
    for item in data_list:
        key = len(item)
        if key not in result:
            result[key] =item
    return result

hufs_courses = ["python", "java", "c++", "os", "network"]
output = process_data(hufs_courses)
print(output[2])