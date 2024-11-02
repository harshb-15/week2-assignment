
def validate(data, template, path=[]):
    for key in template.keys():
        if key not in data.keys():
            return (False, f"mismatched keys: {".".join(path+[key])}")
        if checkType(data[key], template[key]):
            if (type(data[key]) == dict):
                nested_validation = validate(data[key], template[key], path+[key])
                if (nested_validation[0] == False): return nested_validation
        else:
            return (False, f"bad type: {".".join(path+[key])}")
    for key in data.keys():
        if key not in template.keys():
            return (False, f"mismatched keys: {".".join(path+[key])}")
    return (True, "")
        
        

def checkType(data, template):
    if (template == int) or (template == str):
        return template == type(data)
    return type(data) == dict