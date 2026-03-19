
import json
from utils import process_data

with open("config.json") as f:
    config = json.load(f)

data = [i for i in range(1, 50)]

result = process_data(data, config["mode"])

print("Processed:", result)
