# code-review-agent

Code Review Application

This is an intelligent application used to review source code automatically.  
The system analyzes the provided code, compresses important context, applies best-practice rules, and then uses a Large Language Model service to generate fast and accurate improvement suggestions.

Users can paste code, upload files, or provide a folder path.  
The application returns rule violations along with AI-generated review feedback.

---

The system requires:

A supported operating system such as Windows, Linux, or macOS.  
Python  
Access to a running Large Language Model service  
Core libraries such as Streamlit and Requests for UI and communication.

---

## Installing:

cloning repo command:  
git clone <git repository url>.git

virtual environment command:  
python -m venv <virtual environment name>

activate environment (Windows):  
<virtual environment name>\Scripts\activate

install dependencies:  
pip install -r requirements.txt

---

## Executing Program:

To run the project, use the following command (ensure the virtual environment is active):

streamlit run app.py

This command will start the web interface and you should be able to access the application from your browser.

---

Once the application is running, you can:

- Paste your source code  
- Upload files  
- Provide a folder path  

The system will display rule-based findings and detailed AI suggestions.

---

Please ensure that you have followed the installation and setup instructions before attempting to run the project.

---

## Help

Common issues may include:

Service connection problems if the LLM server is not running or reachable.  
Missing dependencies if required libraries are not properly installed.  
Invalid paths if the folder location is incorrect.

---

## Authors:
HET MAYUR THORIA