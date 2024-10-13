# Movie-Review-Sentiment-Analysis
# 📄 Resume Screening and Matching Application
This project is a Streamlit-based web app that enables two functionalities:

- 1.Resume Screening: Automatically categorize resumes into different job profiles using a pre-trained model.
- 2.Resume Matching: Matches uploaded resumes against a provided job description to identify the most suitable candidates based on cosine similarity.

# ⚙️ Features
 ### Resume Screening:
 - Upload resumes in .txt or .pdf format.
 - Automatically predicts the job category based on the content.
 - Provides fun facts or tips related to the predicted category.

 ### Resume Matching::
 - Upload multiple resumes (in .pdf, .docx, or .txt formats).
 - Compare resumes to a job description using TF-IDF vectorization and cosine similarity.
 - Display the top-matching resumes.

# 🛠️ Installation
 ### 1.Clone the repository: 
       https://github.com/Rizon1326/Movie-Review-Sentiment-Analysis.git      
 ### 2.Navigate to the project directory:
       cd resume-screening-matching
 ### 3.Clone the repository:
       pip install -r requirements.txt
 ### 4.Install dependencies:
       streamlit run app.py

# 📂 File Structure
   📦resume-screening-matching
 ┣ 📂uploads
 ┣ 📜app.py
 ┣ 📜clf.pkl
 ┣ 📜tfidf.pkl
 ┣ 📜requirements.txt
 ┗ 📜README.md

 

   


