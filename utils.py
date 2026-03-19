
def process_data(data, mode):
    if mode == "square":
        return [x**2 for x in data]
    elif mode == "filter":
        return [x for x in data if x % 2 == 0]
    elif mode == "sum":
        return sum(data)
    return data
