# Imports
import json
import pandas as pd

# Load SQuAD data
with open('data/raw/dev-v2.0.json', 'r') as file:
    squad_data = json.load(file)

# Extract data
data = []
for article in squad_data['data']:
    title = article['title']
    for paragraph in article['paragraphs']:
        context = paragraph['context']
        data.append([title, context])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['title', 'text'])

# Save as CSV
df.to_csv('data/transformed/squad_data.csv', sep='\t', index=False)
