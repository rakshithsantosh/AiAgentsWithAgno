from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb
from agno.knowledge.knowledge import Knowledge

from dotenv import load_dotenv

#load the api key
load_dotenv()

#define the embedder
embedder = OpenAIEmbedder()

#define the chunking stratergy
chunking_stratergy = SemanticChunking(embedder=embedder,chunk_size=1000)

#create the pdf reader
pdf_reader = PDFReader(chunking_stratergy=chunking_stratergy)

# create the vector db
vector_db = LanceDb(uri="vector_db/lancedb",
                    embedder=embedder,
                    table_name="knowledge_table")


# create a knowledge base
knowledge_base = Knowledge(name="Knowledge_Base",
                           description="Contains the book 'Cracking REACT Interviews-Vol 1'",
                           vector_db=vector_db)

if __name__ == "__main__":
    # add content to the knowledge base
    knowledge_base.add_content(path="Cracking REACT Interviews-Vol 1.pdf.pdf",
                            reader=reader)