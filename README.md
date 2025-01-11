# Chatbot Application Documentation

## Overview

This project implements a chatbot application using Gradio, which allows users to interact with different language models. The application supports models from Ollama and Hugging Face, and it can process documents from various sources such as PDFs, web URLs, and YouTube links.

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/captain-peroxide/QUICKSELL.git
   cd QUICKSELL
   ```

2. **Install Required Packages:**
   Make sure you have gradio and any other dependencies installed. You can do this using pip:
   ```bash
   pip install gradio
   ```

3. **Local Imports:**
   Ensure that the following modules are available in your project:
   - models.llms (for model handling)
   - controllers.chatbot_controller (for chatbot logic)

## Usage

To run the chatbot application, execute the following command in your terminal:
```bash
python main.py
```
Once the application is running, open your web browser and navigate to http://localhost:11434 to interact with the chatbot.

## Components

- **main.py**: Entry point and Gradio interface.
- **controllers/chatbot_controller.py**: Logic for handling chatbot interactions.
- **models/llms.py**: Definitions of language models.
- **vectorstore.py**: (If relevant, based on its content).
- **models/chain.py**: (If relevant, based on its content).
- **models/chatbot.py**: (If relevant, based on its content).

## Examples

Provide examples of how to use the chatbot with different models and document types.


## Overview

This project implements a chatbot application using Gradio, which allows users to interact with different language models. The application supports models from Ollama and Hugging Face, and it can process documents from various sources such as PDFs, web URLs, and YouTube links.

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/captain-peroxide/QUICKSELL.git
   cd QUICKSELL
   
2. **Install Required Packages:**
Make sure you have gradio and any other dependencies installed. You can do this using pip:
   ```bash
   pip install gradio
   ```
3.**Local Imports:**
Ensure that the following modules are available in your project:
models.llms (for model handling)
controllers.chatbot_controller (for chatbot logic)

**Usage**
To run the chatbot application, execute the following command in your terminal:
   ```bash
   python main.py
   ```
Replace your_script_name.py with the name of your Python file containing the code.
Once the application is running, open your web browser and navigate to http://localhost:11434 to interact with the chatbot.
