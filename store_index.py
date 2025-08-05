from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("developer-quickstart-py")

extracted_data = load_pdf("pdfs/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

from langchain_pinecone import PineconeVectorStore
index_name = "developer-quickstart-py"

docsearch = PineconeVectorStore.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name
)
