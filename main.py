# Install required libraries
# pip install sentence-transformers
# pip install PyPDF2

from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader
import sys

# Load the pre-trained SBERT model
model = SentenceTransformer('stsb-roberta-large')

# Function to score similarity between two sentences
def score(sentence1, sentence2):
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
    sc = cosine_scores.item()
    if sc <= 0:
        return 0
    elif 0 < sc <= 0.1:
        return 1
    elif 0.1 < sc <= 0.2:
        return 1
    elif 0.2 < sc <= 0.3:
        return 2
    elif 0.3 < sc <= 0.4:
        return 3
    elif 0.4 < sc <= 0.5:
        return 4
    elif 0.5 < sc <= 0.6:
        return 5
    elif 0.6 < sc <= 0.7:
        return 6
    elif 0.7 < sc <= 0.8:
        return 7
    else:
        return 8

# Function to extract text from PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Get file paths from command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <student_answers_file_path.pdf> <model_answers_file_path.pdf>")
    sys.exit(1)

student_answers_file_path = sys.argv[1]
model_answers_file_path = sys.argv[2]

# Extract text from PDF files
student_answers_text = extract_text_from_pdf(student_answers_file_path)
model_answers_text = extract_text_from_pdf(model_answers_file_path)

# Print the extracted text
print("Student Answers:")
print(student_answers_text)
print("\nModel Answers:")
print(model_answers_text)

# Calculate and print the score
score_value = score(student_answers_text, model_answers_text)
print("\nScore:", score_value)
