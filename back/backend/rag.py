import pandas as pd
import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from langchain_google_genai import ChatGoogleGenerativeAI
from gradio_client import Client, handle_file
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chromadb_client = chromadb.PersistentClient(path="./backend/chromadb_database")
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="thenlper/gte-base")

collection = chromadb_client.get_or_create_collection(name="myntra_data", embedding_function=embedding_function) # If not specified, by default uses the embedding function "all-MiniLM-L6-v2"
    

def get_data_from_db(clothing_item):
    result = collection.query(query_texts=clothing_item, n_results=1, include=["documents", "metadatas"])
    
    return {
        "clothing_item_found": result["documents"],
        "image": result["metadatas"][0][0]["img"],
        "main_category": result["metadatas"][0][0]["main_category"]
    }


def get_images_using_llm(query):
    
    prompt = f"""
    You are a clothing store helper bot. You have to figure out what clothing items the user wants to wear. The user has said: "{query}". Please output the clothing items that the user wants to wear in the following format:
    "item1, item2, item3, ..."
    """
    
    response = llm.invoke(prompt)
    final_response = response.content.split(" \n")
    items = final_response[0].split(", ")
    
    print(items)
    print(response.content)
    
    images = []
    categories = []
    for item in items:
        result = get_data_from_db(item)
        images.append(result["image"])
        category = result["main_category"]
        
        if category == "Top Wear":
            category = "Upper-body"
        elif category == "Bottom Wear":
            category = "Lower-body"
        elif category == "Dress (Full Length)":
            category = "Dress"
        else:
            category = None
        
        categories.append(category)
        
    # print(images)
    return images, categories


def viton_api(garment_img, clothing_category, person_img = 'https://levihsu-ootdiffusion.hf.space/file=/tmp/gradio/aa9673ab8fa122b9c5cdccf326e5f6fc244bc89b/model_8.png'):
    client = Client("levihsu/OOTDiffusion")
    
    result = client.predict(
        vton_img=handle_file(person_img),
        garm_img=handle_file(garment_img),
        category=clothing_category,
        n_samples=1,
        n_steps=20,
        image_scale=2,
        seed=-1,
        api_name="/process_dc"
    )
    
    final_image = result[0]["image"]
    print(final_image)
    
    return final_image