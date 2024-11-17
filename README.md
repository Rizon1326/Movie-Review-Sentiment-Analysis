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
 ### 1. Clone the repository: 
       https://github.com/Rizon1326/Movie-Review-Sentiment-Analysis.git      
 ### 2. Navigate to the project directory:
       cd Resume_Detection
 ### 3. Install dependencies:
       pip install -r requirements.txt
 ### 4. Run the app:
       streamlit run app.py
       
# 📂 File Structure
 ```bash
   📦resume-screening-matching
 ┣ 📂uploads
 ┣ 📜app.py
 ┣ 📜clf.pkl
 ┣ 📜tfidf.pkl
 ┣ 📜requirements.txt
 ┗ 📜README.md
```

# 🧰 Dependencies
 - Streamlit: The frontend framework used to create the web application.
 - NLTK: For text preprocessing, including tokenization and stopword removal.
 - Scikit-learn: To perform TF-IDF vectorization and cosine similarity calculations.
 - PyPDF2: For extracting text from PDF resumes.
 - docx2txt: For extracting text from DOCX files.

# 🎨 Screenshots 
https://github.com/user-attachments/assets/11fad675-0f4a-474c-b77b-b4da69e62ac9

# 📋 How to Use
  ## Resume Screening:
   - Navigate to the "Resume Screening" page from the sidebar.
   - Upload your resume and get instant feedback on the predicted job category.
  ## Resume Matching:
   - Navigate to the "Resume Matching" page from the sidebar.
   - Input the job description and upload resumes to find the best matches for the position.
     
# 👨‍💻 Author
 ###  @Rizon
 
# 💡 Fun Fact
 - This app uses cosine similarity to match resumes to a job description. Cosine similarity measures the angle between two vectors in a multi-dimensional space, making it perfect for comparing text documents!





 

   


