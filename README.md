# Automatic Paper Checker

**Description:**  
The Automatic Paper Checker is a tool designed to evaluate student answers by comparing them to a set of model answers provided in PDF format. Utilizing the Sentence Transformers library, this tool assesses the similarity between the student's responses and the correct answers, providing a score ranging from 0 to 100 based on the degree of match.

**Technologies Used:**  
- **Sentence Transformers:** For encoding and comparing text using pre-trained models.
- **PyPDF2:** For extracting text from PDF files.

**Features:**  
- **Text Extraction:** Reads and extracts text from PDF files containing student answers and correct answers.
- **Similarity Scoring:** Uses a pre-trained SBERT model to compute the semantic similarity between the student's responses and the correct answers.
- **Automated Evaluation:** Provides a score from 0 to 100 based on the similarity score, reflecting the accuracy of the student’s answers compared to the model answers.

**Challenges Overcome:**  
Implementing accurate text extraction from PDF files and ensuring reliable similarity scoring required integrating and fine-tuning the use of pre-trained language models. Handling various formats and ensuring consistent scoring were key aspects that needed attention.

**Outcome:**  
The Automatic Paper Checker streamlines the grading process by automating the evaluation of student answers. It offers a practical solution for assessing textual responses based on semantic similarity, providing a quick and objective scoring mechanism.
