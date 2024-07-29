# CoDivas' HackerRamp: WeForShe Project

## Problem Statement

Today, most of the online shoppers are between the age bracket of 18-40, and this number keeps increasing every year as fast fashion gains momentum and people find reasons to buy more frequently from the comfort of their homes. Targeting this age group means reducing their need for visiting physical stores. With the growing database of clothing items, customers are struggling to find clothes that keep up with current trends and also align with their personal preferences. Not being able to see how clothes will look on one’s own body is a big hassle when shopping online. It makes it hard to mix and match items and get a sense of how they’ll look together.

## Solution

To address these common issues, we aim to leverage the technological advancements Myntra has made in image search, as well as its advanced recommendation system, by incorporating our own innovative technologies in the following ways:

- We developed an interactive platform prototype that helps users visualise their choice of clothing on themselves.
- This prototype also provides visualizations of complementary outfit elements. For example, when a user selects a top, we will also show how different shoes, pants, and other accessories would look with it.
- This is implemented through identification of current trends while keeping in mind user preferences and recommending the outfits accordingly.
- Clicking ✔️ or ❌will help update the internal memory, allowing the platform to refine recommendations and suggest alternative items that better match the user's preferences.


## Installation & Usage

To use this project, follow these steps:

1. Backend:
- cd back
- pip install -r requirements.txt
- python ./backend/chromadb_database_creation.py
- python ./backend/sqlite_database_creation.py
- python ./backend/app.py

2. Frontend: 
- cd front
- npm i
- npm start

3. Make your own Gemini API Key and put it in a .env file as "GEMINI_API_KEY"

## Features

1. Data Collection:
- For the product catalog, we utilized a dataset of Myntra products sourced from Kaggle, initially containing approximately 1 million items with images.
- We refined this dataset by first reducing it to 100,000 items and further to 30,000 by focusing exclusively on clothing items, and few accessories. 
- To ensure relevance, we conducted transformations such as identifying the gender using LLMs and categorizing items into classifications like top wear, bottomwear, and dresses.
- Since real-world transactional data was not readily available, we simulated and created dummy transactional data to mimic real-world scenarios. Final Products Dataset (Source Code for Data Generation). We then stored the embeddings for RAG in chromadb and in Sqlite for retrieval from frontend

2. Trend Identification:
- We believe that Myntra, with over 60 million active users, provides a rich dataset from which current and emerging trends can be identified.
- When a particular trend comes into fashion, there is typically a significant increase in the quantity of those items being purchased. 
- By analyzing time-stamped transactional data, we detect these steep jumps in quantity. We calculate these increases to identify emerging trends effectively.
- In addition, we also identify whether this steep jump in the quantity of a particular category is due to seasonal changes or a new fashion trend.
- For example, as shown in the graph on right, we can see that as winter approaches, there is a huge jump in sales recorded for sweatshirts.

3. Virtual Try On:
- To provide users with a realistic preview of how an outfit will look on them, we employ image to image diffusion model to seamlessly overlay selected clothing items onto the user's photo. 
- This advanced virtual try-on feature allows users to effortlessly visualize their chosen garments without the need for a live camera feed, offering a convenient and immersive shopping experience.
- Based on their selection, our recommendation engine based on the identified trends and past user history will suggest other pieces of clothing to complete the outfit. For instance, if a person selects a particular top, our system will recommend matching bottomwear. 
- We refine these recommendations by taking feedback from the user using ticks and crosses, helping us to recommend items the user will actually wear. This mechanism makes sure our recommendation engine stays up to date with all the user preferences and current trends

4. Walking Wardrobe:
- The user types the outfit or clothing item they are looking for in the chat section. LLM Gemini 1.5 - Flash identifies key clothing details from user description and extracts the details.
- Then our model finds matching items in the Chromadb database using cosine similarity and retrieves product images and with the help of RAG model it presents an ensemble outfit.
- The user can then virtually try on the outfits to see how they look.


