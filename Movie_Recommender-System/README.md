# MOVIE RECOMMENDER SYSTEM
In the era of digital streaming platforms, movie recommender systems play a vital role in enhancing user experience and engagement. This data science project focuses on building a movie recommender system using cosine similarity, a common technique in natural language processing and recommendation systems. The goal is to provide users with personalized movie recommendations based on their viewing history and preferences.
This project aims to leverage cosine similarity and "CONTENT BASED" techniques to create a movie recommender system that helps users discover movies tailored to their tastes. By providing personalized recommendations, the project seeks to improve user retention and satisfaction, ultimately benefiting both users and streaming platforms.

# Technique used:
Cosine Similarity

Cosine similarity is a metric used to measure the similarity between two non-zero vectors in an inner product space. It is widely employed in various fields, including natural language processing (NLP), information retrieval, and recommendation systems. In the context of recommendation systems, cosine similarity can be used to determine how similar two items or user preferences are to each other.

Here's how cosine similarity works:

1. **Vector Representation:** Each item (e.g., movies, documents) or user is represented as a vector in a high-dimensional space, where each dimension corresponds to a feature or attribute. For example, in a movie recommender system, the features might include movie genres, actors, directors, or user ratings.

2. **Vector Normalization:** To calculate the cosine similarity, it's essential to normalize the vectors. This involves converting the vectors to unit vectors (vectors with a length or magnitude of 1). Normalization ensures that the similarity measure is not affected by the scale of the vectors.

3. **Cosine Calculation:** The cosine of the angle between two vectors A and B is calculated.

4. **Similarity Score:** The cosine similarity score ranges from -1 to 1:
   - If the vectors are identical, the cosine similarity is 1 (maximum similarity).
   - If the vectors are orthogonal (perpendicular), the cosine similarity is 0 (no similarity).
   - If the vectors are diametrically opposed (180 degrees apart), the cosine similarity is -1 (maximum dissimilarity).

5. **Recommendation:** In recommendation systems, cosine similarity can be used to find items or user preferences that are most similar to a given item or user profile. Items with higher cosine similarity scores are recommended as they are considered more similar to the user's preferences.

# Tools/Technologies used:
1. Jupyter Notebook
2. Python language
3. Numpy library
4. Pandas - Data Cleaning
5. Matplotlib - Data Visualization
6. SkLearn - Model Building
7. Microsoft Excel
8. Streamlit - Framework

# Prerequisites:
1. A prior knowledge of Python programming language along with its libraries for data science such as Numpy, Pandas, Matplotlib, Seaborn, SkLearn & Cosine Similarity is needed.
2. Installation of required libraries

# Process:
1. Import Libraries
2. Load dataset
3. Data Cleaning
4. Data PreProcessing
5. Stemming
6. Count Vectorizer
7. Cosine Similarity
8. Model Building
9. Model Evaluation sample
10. Exporting the model
11. Streamlit deployment

# Output:
![Movies1](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/a2e83ec8-468d-423b-a2cb-133a861d0637)

![Movies2](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/7aadf532-c36c-4a7e-8c0d-5a82f8eb5532)

![Movies3](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/fb224042-a227-40fa-943b-55ae5a7115bf)

![Movies4](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/71da2a6c-a8d9-491f-9d2b-934359601acf)

![Movies5](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/4c4f05ac-84b5-4c1f-aea4-1ae5cdb98855)

![Movies6](https://github.com/Navina-Murugadas/TWSIP/assets/72821323/9649edec-9d39-4fe2-96ac-e440a4c1c2c6)

