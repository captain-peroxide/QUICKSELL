# QUICKSELL
Documentation for ChatBot Application Using Gradio
Overview
This project is a chatbot interface built using Gradio, designed to process and retrieve information from various document types using different AI models like Ollama and HuggingFace. Users can configure the chatbot with their preferred model, specify document sources, and interact with the chatbot through an intuitive chat interface.

Features
Model Selection:

Supports two model sources:
Ollama: Requires a locally running Ollama server.
HuggingFace: Requires an API key for hosted models.
Supports specific models for each source:
Ollama: orca-mini
HuggingFace: llama2:latest
Document Input Options:

PDF: Allows file upload for document processing.
WEB: Accepts a URL to fetch web-based content.
YouTube: Accepts a URL to fetch transcripts or captions from YouTube videos.
Dynamic Interface:

Toggles API key visibility based on the selected model source.
Adjusts input fields based on the selected document type (URL or file input).
Interactive Chat:

Integrates a chatbot capable of understanding and responding to user queries based on processed documents.
Project Structure
plaintext
Copy code
.
├── models
│   ├── llms.py                  # Defines AI models (OllamaModel, HFModel)
├── controllers
│   ├── chatbot_controller.py    # Manages chatbot logic, integrates models
├── app.py                       # Main application script
├── requirements.txt             # Project dependencies
Code Walkthrough
1. Model Selection
The user can choose between Ollama and HuggingFace models. Based on the selection:

An API key input field is shown for HuggingFace.
A dropdown menu updates to display models specific to the selected source.
python
Copy code
def filter_model_types(model_type):
    api_key_field = model_type != "Ollama"
    return gr.Text(placeholder="Input your API key", visible=api_key_field), gr.Dropdown(value=chatbot.model_types[model_type][0],
                                                                               choices=chatbot.model_types[model_type])
2. Document Input
The user can select document types (PDF, Web, or YouTube) for processing. Depending on the selection:

A file upload field is shown for PDF.
A URL input field is shown for Web or YouTube.
python
Copy code
def filter_doc_types(doc_type):
    url_field = False
    file_field = False

    if doc_type == "PDF":
        file_field = True
    else:
        url_field = True
    return gr.Textbox("URL", visible=url_field), gr.File(visible=file_field)
3. Chat Interface
The chatbot logic is defined in the ChatBotController class, which:

Initializes with a selected model.
Processes document retrieval and query responses.
Communicates with the frontend via gr.ChatInterface.
python
Copy code
chatbot = ChatBotController(OllamaModel("orca-mini"))

gr.ChatInterface(chatbot.predict)
How to Run
Prerequisites
Python Installation:

Install Python (version 3.8 or higher).
Install the required packages using the following command:
bash
Copy code
pip install -r requirements.txt
Ollama Server:

Start the Ollama server locally if using Ollama models:
bash
Copy code
ollama serve
HuggingFace API Key:

Obtain an API key from HuggingFace if using HuggingFace models.
Steps to Launch
Run the application:
bash
Copy code
python app.py
Open the Gradio interface at http://localhost:11434 in your web browser.
Usage Instructions
1. Configure Model
Select a model source (Ollama or HuggingFace).
Choose a specific model from the dropdown.
If using HuggingFace, enter your API key.
2. Select Document Source
Choose the document type (PDF, WEB, or YouTube).
Upload a file or provide a URL, depending on the selected type.
3. Interact with the Chatbot
Use the chat interface to ask questions or retrieve information based on the uploaded/processed document.
Dependencies
Gradio: For creating the user interface.
Requests: For handling API calls.
LangChain Community Integration: For model processing and inference.
Install dependencies using:

bash
Copy code
pip install -r requirements.txt
Known Issues
ConnectionError:

Ensure the Ollama server is running if using Ollama models.
Check if the correct port (11434) is open.
Timeout Issues:

Increase the timeout settings in the requests library.
Future Improvements
Add support for additional model sources.
Enhance document processing with support for text extraction and summarization.
Optimize the chatbot's response time for large documents.
License
This project is licensed under the MIT License.






You said:
write a readme code for the same
ChatGPT said:
ChatGPT
ChatBot Application Using Gradio
This project is a Gradio-based chatbot interface that enables users to interact with AI models to process and retrieve information from various document types. It supports model sources like Ollama and HuggingFace and document types including PDF, Web, and YouTube.

Features
Model Selection: Choose between Ollama and HuggingFace models.
Document Processing: Input documents via file upload or URLs.
Dynamic Interface: Adjusts fields based on user selections.
Interactive Chat: Query processed documents through a chat interface.
Installation
Prerequisites
Python 3.8 or higher
Dependencies listed in requirements.txt
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-repository/chatbot-gradio.git
cd chatbot-gradio
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
(Optional) Start the Ollama server if using Ollama models:

bash
Copy code
ollama serve
Usage
Run the application:

bash
Copy code
python app.py
Open the Gradio interface in your browser:

plaintext
Copy code
http://localhost:11434
Configure the model:

Select the Model Source (Ollama or HuggingFace).
Choose the specific model.
Provide an API key if required (HuggingFace only).
Input a document:

Select the Document Type (PDF, Web, or YouTube).
Upload a file or provide a URL.
Interact with the chatbot via the chat interface.

Project Structure
plaintext
Copy code
.
├── models
│   ├── llms.py                  # Defines AI models (OllamaModel, HFModel)
├── controllers
│   ├── chatbot_controller.py    # Manages chatbot logic, integrates models
├── app.py                       # Main application script
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
Example
Model Selection:

Select Ollama as the source and orca-mini as the model.
Document Input:

Upload a PDF file for processing.
Chat Interaction:

Ask questions related to the content of the uploaded document.
Dependencies
Install dependencies with:

bash
Copy code
pip install -r requirements.txt
Key libraries:

Gradio: For building the user interface.
Requests: For API communication.
Known Issues
Ollama Connection: Ensure the server is running if using Ollama models.
Timeout Errors: May occur with large documents or network issues.
Future Work
Add support for more AI model sources.
Enhance document summarization and text processing.
Optimize performance for large document inputs.
License
This project is licensed under the MIT License.
