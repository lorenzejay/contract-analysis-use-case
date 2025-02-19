import os

from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter


from dotenv import load_dotenv


import weaviate
from weaviate.classes.init import Auth
import weaviate.classes as wvc

load_dotenv()
# Setup Qdrant client + openai client
COLLECTION_NAME = "contracts_business_latest"
doc_converter = DocumentConverter(allowed_formats=[InputFormat.PDF])  # Allow PDF format
weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

with weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
    headers={"X-OpenAI-Api-key": openai_api_key},
) as client:
    if client.is_ready():
        if not client.collections.exists(COLLECTION_NAME):
            collection = client.collections.create(
                name=COLLECTION_NAME,
                vectorizer_config=wvc.config.Configure.Vectorizer().text2vec_openai(),
                generative_config=wvc.config.Configure.Generative.openai(),
            )
        else:
            collection = client.collections.get(COLLECTION_NAME)

        contracts_objs = list()

        pdf_folder = "knowledge/contracts/"
        for filename in os.listdir(pdf_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder, filename)
                print(f"Processing {pdf_path}")

                result = doc_converter.convert(pdf_path)

                # Chunk the converted document
                for chunk in HybridChunker().chunk(result.document):
                    chunk_dict = {
                        "text": chunk.text,
                        "properties": {
                            "source_file": filename,
                            "heading": chunk.meta.headings[0]
                            if chunk.meta.headings
                            else "",
                            "page_number": chunk.meta.doc_items[0].prov[0].page_no
                            if chunk.meta.doc_items
                            else None,
                        },
                    }
                    contracts_objs.append(chunk_dict)
        collection.data.insert_many(contracts_objs)
