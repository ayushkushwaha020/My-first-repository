def normalize_email(value):
    return value.strip().lower()

def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def discount(total, rate):
    return total - (total * rate)