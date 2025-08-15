import pandas as pd
df = pd.read_json("Project/students.json")

df.to_csv("Project\students.csv", index=False)
print("JSON file converted into CSV file.")