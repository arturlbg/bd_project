import json

def convert_to_json(columns, values):
    data = []

    for row in values:
        r = {}
        for idx, row in enumerate(row):
            r[columns[idx]] = row
        data.append(r)

    json_data = json.dumps(data)
    return json_data
