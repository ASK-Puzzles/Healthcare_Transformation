# Drug Summary Chatbot

A local AI chatbot for healthcare that processes PDFs about drugs and medicines, providing summaries and explanations.

## Summary
This project allows users to upload PDFs containing information about drugs and medicines. The application extracts text from the uploaded PDFs and uses AI to generate a brief summary and explanation of the content. This can be particularly useful for healthcare professionals, researchers, and patients who need quick and concise information about various drugs and medicines.

## Potential Applications
- **Healthcare Professionals:** Quickly understand the key points of drug information without reading through lengthy documents.
- **Researchers:** Summarize large amounts of drug-related data for research and analysis.
- **Patients:** Get understandable summaries of drug information for better health literacy.
- **Pharmaceutical Companies:** Provide summarized information about new drugs to healthcare providers and customers.

## Installation

### Prerequisites
- Python 3.6+
- Pip (Python package installer)

### Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/ASK-Puzzles/Healthcare_Transformation.git
    cd drug-summary-chatbot
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```sh
    python app.py
    ```

5. **Access the application:**
    - Open a web browser and go to `http://127.0.0.1:5000/`.
    - Upload a PDF file about drugs or medicines.
    - View the summarized content on the result page.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.
