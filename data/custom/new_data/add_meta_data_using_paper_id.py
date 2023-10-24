import json
import requests
import time
from unidecode import unidecode
import concurrent.futures


def fetch_metadata_for_paper_id(paper_id, counter):
    print(f"Fetching metadata for paper number: {counter}")
    base_url = f"https://api.semanticscholar.org/v1/paper/{paper_id}"
    api_key = '<YOUR_API_KEY_HERE>'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    retries = 7
    delay = 2

    while retries > 0:
        response = requests.get(base_url, headers=headers)

        if response.status_code == 200:
            return response.json(), counter
        elif response.status_code == 429:  # TOO MANY REQUESTS
            print('TOO MANY REQUESTS')
            time.sleep(delay)
            delay *= 2
            retries -= 1
        else:
            print(f"Error {response.status_code} for paper number {counter}.")
            retries -= 1

    print(f'Could not fetch metadata for paper number {counter}')
    return None, counter


with open('papers_id_mapping.json', 'r') as file:
    mapping = json.load(file)

papers_metadata = {}

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(fetch_metadata_for_paper_id, paper_id, counter + 1)
               for counter, (paper_id, _) in enumerate(mapping.items())]

    for future in concurrent.futures.as_completed(futures):
        metadata, counter = future.result()
        orig_id = list(mapping.values())[counter - 1]

        if metadata:
            metadata['authors'] = [unidecode(author['name']) for author in metadata['authors']]
            metadata['topics'] = [unidecode(topic['topic']) for topic in metadata['topics']]
            metadata['s2FieldsOfStudy'] = [unidecode(field['category']) for field in metadata['s2FieldsOfStudy']]
            papers_metadata[orig_id] = metadata
            for field in ['abstract', 'arxivId', 'citations', 'corpusId', 'doi', 'is_open_access', 'paperId',
                          'references', 'title', 'url', 'year']:
                metadata.pop(field, None)
with open('papers_metadata.json', 'w') as file:
    json.dump(papers_metadata, file, indent=4)
