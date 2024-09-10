import pandas as pd

# Create a dictionary with the data
data = {
    "Apples": [35, 41],
    "Bananas": [21, 34]
}

# Create a DataFrame and set the index
df = pd.DataFrame(data, index=["2017 Sales", "2018 Sales"])

# Write the DataFrame to a CSV file
df.to_csv("fruit.csv")

# Output message indicating file was created
print("CSV file 'fruit.csv' has been created successfully.")