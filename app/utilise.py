import json
def is_json(data):
    try:
        p_data = json.loads(data)
        valied = True
    except ValueError:
        valied = False
    return valied
