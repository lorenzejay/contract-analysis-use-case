import os
from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
import openai
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import PointStruct
import uuid

load_dotenv()
# Setup Qdrant client + openai client
COLLECTION_NAME = "contracts_business_latest"
doc_converter = DocumentConverter(allowed_formats=[InputFormat.PDF])  # Allow PDF format
qdrant_url = os.getenv("QDRANT_URL")
qdrant_api_key = os.getenv("QDRANT_API_KEY")
openai_client = openai.Client(
    api_key=os.getenv("OPENAI_API_KEY"),
)
client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
embedding_model = "text-embedding-3-small"

# Define the folder where PDFs are stored
pdf_folder = "knowledge/contracts/"
# Initialize documents and metadata lists
documents, metadatas = [], []
points = []
# Loop through all PDFs in the folder and process them
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        print(f"Processing {pdf_path}")

        result = doc_converter.convert(pdf_path)

        # Chunk the converted document
        for chunk in HybridChunker().chunk(result.document):
            print("chunk", chunk)
            embedding_result = openai_client.embeddings.create(
                input=chunk.text, model=embedding_model
            )
            vector = embedding_result.data[0].embedding
            documents.append(chunk.text)
            metadatas.append(chunk.meta.export_json_dict())
            point_id = str(uuid.uuid4())
            points.append(
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={
                        "text": chunk.text,
                        "metadata": chunk.meta.export_json_dict(),
                    },
                )
            )
print("points", points)
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)
client.upsert(collection_name=COLLECTION_NAME, points=points)

# Retrieve and print results from Qdrant
points = client.search(
    collection_name=COLLECTION_NAME,
    query_vector=openai_client.embeddings.create(
        input=["What is the best to use for vector search scaling?"],
        model=embedding_model,
    )
    .data[0]
    .embedding,
    limit=10,
)

for i, point in enumerate(points):
    print(f"=== {i} ===")
    print(point.document)
