def match_records(records, target_ids):
    matches = []
    for record in records:
        for target in target_ids:
            if record["id"] == target:
                matches.append(record)
    return matches

def build_report(items):
    output = ""
    for item in items:
        output += str(item) + "\n"
    return output