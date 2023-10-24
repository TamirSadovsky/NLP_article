# Local Citation Recommendation - Towards The Perfect Prefetching : A Comparative Analysis of Encoding Techniques for Citation Retrieval

This is NLP project from TAU univercity, aiming to improve performance and results from existing techniques used in https://github.com/nianlonggu/Local-Citation-Recommendation. Full details in our PDF article.

All our new data and python code which generated them are located in **data/custom/new_data**.

All data was generated using Semantic Scholar API. To use the API efficiently, you should request an API key through their website first.

To use our new data or some of it, you can use the existing json with the titles already appended in **papers_with_additional_fields.json**.

If you would like to modify the existing data, you can use **papers_metadata.json** and choose the fields that you would like to use.

If you would like to try and generate new data and append it to the existing one on **papers.json**, you can use the papers IDs mapping that we generated and use the semantic scholar API.

All the steps are elaborated on our PDF.

To run the baseline code, follow the instructions on https://github.com/nianlonggu/Local-Citation-Recommendation.
