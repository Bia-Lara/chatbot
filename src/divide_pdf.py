import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="collection")
chroma_client = chromadb.PersistentClient(path="db")

def divide_text(chunk_len = 1000):
    
    with open('C:/Users/Ana Beatriz/Documents/chatbot/src/teste.txt', 'r', encoding="utf-8") as file:
        text = file.read()

    pedacos = []
    inicio = 0
    while inicio < len(text):
        final = inicio + chunk_len
        pedacos.append(text[inicio:final])
        if final >= len(text):
            inicio = len(text)
        else:
            inicio += chunk_len

    return pedacos

chunks = divide_text()


for i, chunk in enumerate(chunks):
    collection.add(documents=chunk, ids=[str(i)])
   


