from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from crewai import Agent, Task, Crew
import os


class ChatHistory():
  def __init__(self):
    self.history = ""
  
  def append_user(self, message: str):
    self.history.join("\n\nUser: " + message)
  
  def append_assistant(self, message: str):
    self.history.join("\n\nAssistant: " + message)

  def prompt(self):
    return self.history
  
def get_data():
  print("Loading scraped data...")
  file_loader = TextLoader("signa_scrape_20250813_170121.txt", encoding="utf-8")
  # web_loader = WebBaseLoader("https://www.signa.pt/")
  
  file_docs = file_loader.load()
  # web_docs = web_loader.load()
  return file_docs # + web_docs

def get_vector_storage(chunk_size=1000, chunk_overlap=200):
  docs = get_data()

  print("Splitting data...")
  splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

  print("Dividing data into chunks...")
  chunks = splitter.split_documents(docs)

  embeddings = HuggingFaceEmbeddings()
  vectorstore = FAISS.from_documents(chunks, embeddings)
  return vectorstore.as_retriever()

def get_agent():
  print("Creating agent...")

  llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
  )

  return Agent(
    role="RAG Assistant",
    goal="Answer based on company knowledge without being verbose. Keep the length of the answer to one paragraph.",
    backstory="You know everything about SIGNA company and its services.",
    llm=llm,
  )

def ask_bot(message: str, chat_history: ChatHistory) -> str:

  context_docs = retriever.get_relevant_documents(message)
  context_text = "\n\n".join(doc.page_content for doc in context_docs)

  task = Task(  
    agent = agent,
    description = f"Using the following context: {context_text}\n\nAnd the following chat conversation:{chat_history.prompt()}|\n\nAnswer: {message}",
    expected_output="A clear, concise, non verbose and helpful answer based on the provided context."
  )

  crew = Crew(agents=[agent], tasks=[task])
  answer = crew.kickoff()
  print("Naila output:\n" + answer.raw)

  chat_history.append_user(message)
  chat_history.append_assistant(answer.raw)

  return answer.raw


# Initialize retriever for RAG
retriever = get_vector_storage()

# Initialize retrieval agent for RAG
agent = get_agent()