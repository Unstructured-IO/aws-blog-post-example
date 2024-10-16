import os
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
from unstructured_ingest.v2.processes.chunker import ChunkerConfig
from unstructured_ingest.v2.processes.embedder import EmbedderConfig
from unstructured_ingest.v2.processes.connectors.fsspec.s3 import (
   S3ConnectionConfig,
   S3DownloaderConfig,
   S3IndexerConfig,
   S3AccessConfig,
)
from unstructured_ingest.v2.processes.connectors.opensearch import (
   OpenSearchAccessConfig,
   OpenSearchConnectionConfig,
   OpenSearchUploaderConfig,
   OpenSearchUploadStagerConfig,
)

# TODO: add your credentials below:
os.environ["AWS_S3_URL"] = ""
os.environ["AWS_ACCESS_KEY_ID"] = ""
os.environ["AWS_SECRET_ACCESS_KEY"] = ""
os.environ["UNSTRUCTURED_API_KEY"] = ""
os.environ["UNSTRUCTURED_API_URL"] = ""

os.environ["OPENSEARCH_HOST"] = ""
os.environ["OPENSEARCH_INDEX_NAME"] = ""
os.environ["OPENSEARCH_USERNAME"] = ""
os.environ["OPENSEARCH_PASSWORD"] = ""

if __name__ == "__main__":
    Pipeline.from_configs(
        # General pipeline settings
        context=ProcessorConfig(verbose=True),

        # S3 bucket configuration
        indexer_config=S3IndexerConfig(
            remote_url=os.getenv("AWS_S3_URL")
        ),
        downloader_config=S3DownloaderConfig(),
        source_connection_config=S3ConnectionConfig(
            access_config=S3AccessConfig(
                key=os.getenv("AWS_ACCESS_KEY_ID"),
                secret=os.getenv("AWS_SECRET_ACCESS_KEY")
            )
        ),

        # Unstructured API configuration
        partitioner_config=PartitionerConfig(
            partition_by_api=True,
            api_key=os.getenv("UNSTRUCTURED_API_KEY"),
            partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
            strategy="fast",
        ),

        # Document chunking options
        chunker_config=ChunkerConfig(
            chunking_strategy="by_title",
            chunk_max_characters=512,
        ),

        # Embedding with Amazon Bedrock
        embedder_config=EmbedderConfig(
            embedding_provider="aws-bedrock",
            embedding_model_name="amazon.titan-embed-text-v1",
            embedding_aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            embedding_aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        ),

        # OpenSearch connection and uploading configuration
        destination_connection_config=OpenSearchConnectionConfig(
            hosts=[os.getenv("OPENSEARCH_HOST")],
            username=os.getenv("OPENSEARCH_USERNAME"),
            use_ssl=True,
            access_config=OpenSearchAccessConfig(
                password=os.getenv("OPENSEARCH_PASSWORD")
            )
        ),
        stager_config=OpenSearchUploadStagerConfig(
            index_name=os.getenv("OPENSEARCH_INDEX_NAME")
        ),
        uploader_config=OpenSearchUploaderConfig(
            index_name=os.getenv("OPENSEARCH_INDEX_NAME")
        )
    ).run()

