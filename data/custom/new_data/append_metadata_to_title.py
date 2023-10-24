import json

# Load papers.json
with open('papers.json', 'r') as file:
    papers_data = json.load(file)

# Load papers_metadata.json
with open('papers_metadata.json', 'r') as file:
    papers_metadata = json.load(file)

# Modify the papers_data with the metadata
for paper_id, metadata in papers_metadata.items():
    title = papers_data[paper_id]['title']
    # Append each metadata field to the title
    for field, value in metadata.items():
        if isinstance(value, list):
            value_str = ', '.join(value)
        else:
            value_str = str(value)
        title += f" @{field}: {value_str}"
    papers_data[paper_id]['title'] = title

# Save the updated papers_data to a new file
with open('all_data_no_n.json', 'w') as file:
    json.dump(papers_data, file, indent=4)
