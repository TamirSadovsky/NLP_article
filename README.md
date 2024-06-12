## Local Citation Recommendation - Advancing Prefetching: A Comparative Analysis of Encoding Techniques for Citation Retrieval 📚

Welcome to our NLP project at Tel Aviv University, where we explore innovative encoding techniques for the prefetching step and introduce substantial enhancements to the dataset originally utilized in the [referenced article](https://arxiv.org/pdf/2112.01206).
For detailed information, please refer to our [PDF article](https://github.com/TamirSadovsky/NLP_project/blob/master/NLP_PDF.pdf). 💡

## Project Data 📂

All of our newly generated data and the Python code responsible for their creation are located in the directory: **data/custom/new_data**.

We obtained all this data using the Semantic Scholar API. To utilize the API effectively, make sure to obtain an API key through their website. 🔑

To leverage our new data or a subset of it, you can access the pre-existing JSON file with titles already appended: **papers_with_additional_fields.json**.

If you wish to modify the existing data or select specific fields for your use, you can start with **papers_metadata.json**.

For those interested in generating new data and appending it to the existing corpus within **papers.json**, we've provided a helpful mapping of paper IDs. This mapping can be used with the Semantic Scholar API.

Detailed instructions for these processes can be found in our PDF document. 📄

## Running the Baseline Code 🚀

To execute the baseline code, kindly follow the instructions provided in the [original project repository](https://github.com/nianlonggu/Local-Citation-Recommendation).

## Key Contributions 🌟

1. **Encoding Techniques**: We introduce novel encoding methods for the prefetching step, utilizing various pre-trained language models, including Llama2, BERT, and SciBERT. These encoders generate text embeddings that capture contextual and semantic information, enabling efficient nearest neighbor search for candidate paper retrieval. 🧠

2. **Enriched Dataset**: We have created an expanded and enriched dataset by leveraging the Semantic Scholar API. This dataset provides a more comprehensive representation of each paper, including metadata such as publication year, authors, fields of study, and topics. The enriched dataset aims to improve the recall and accuracy of the citation recommendation system. 📈

3. **State-of-the-Art Results**: By training the baseline model on our improved dataset and integrating our advanced encoding techniques, we achieved state-of-the-art performance in local citation recommendation, surpassing the results reported in the baseline work. 🏆

Thank you for exploring our project! For any questions or additional information, please refer to our PDF or reach out to our team. 📩
