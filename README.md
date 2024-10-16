# aws-blog-post-example

This repository contains a script to accompany the Unstructured.io blog post in collaboration with AWS.

_Link to the blog post is coming soon._ 

The blog post illustrates how Unstructured.io's Serverless API can transform unstructured data into a 
structured JSON format that can be used by RAG systems on AWS. It provides a step-by-step guide on how 
to use the Unstructured API, detailing each stage of the data transformation process including ingestion, 
partitioning, extraction, chunking, embedding with Bedrock, and syncing with OpenSearch. 

To use this example: 
1) Download and install Python version 3.9.0 or later.
2) Clone the repo, and create a virtual environment.
3) In the new virtual environment install the required dependencies:
   * Open your terminal in the root directory of the cloned repo.
   * Run either `pip install "unstructured-ingest[s3, opensearch, pdf, bedrock]"` to install the latest library versions, or `pip install -r requirements.txt` to use specific versions as defined in the `requirements.txt` file.
4) Open the `run_pipeline.py`, and add your values for the environment variables required to authenticate you with Unstructured Serverless API, Amazon OpenSearch, S3, and Bedrock. 

You can now run the script from your terminal by executing: 

```bash
python run_pipeline.py
```



