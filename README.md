# Website Developer Assistant ChatBot

This project aims to assist users in website development tasks by providing guidance and code snippets using natural language processing techniques. It leverages LangChain to utilize an existing chatbot model for understanding user queries and generating relevant responses, including HTML and CSS code snippets.

### Functionality:
- **Web Development Assistance**: Provides guidance and support for creating webpages using HTML and CSS.
- **Code Examples**: Offers code snippets and examples for common web development tasks.
- **Explanation**: Provides explanations and insights into the HTML and CSS code snippets provided.
- **Conversation History**: Maintains a conversation history to track the context and provide relevant responses.

### Features:
- **Prompt-based Interaction**: Utilizes a prompt-based approach for human-chatbot interaction.
- **Chat History**: Keeps track of the conversation history to ensure context continuity.
- **Intelligent Responses**: Utilizes a language model to generate intelligent and contextually relevant responses.

### Usage:
1. **Conversation Interaction**: Users can engage in a conversation with the chatbot by inputting queries related to web development tasks.
2. **Code Example Requests**: Users can request code examples for specific HTML or CSS tasks.
3. **Explanation Queries**: Users can seek explanations for HTML and CSS code snippets provided by the chatbot.

### Technologies Used:
- **Language Models**: Utilizes Hugging Face's Transformers library for natural language processing tasks.
- **Streamlit**: Provides a user-friendly interface for interacting with the chatbot.
- **Python**: Implemented in Python programming language.
- **HTML/CSS**: Provides examples and explanations related to web development tasks.

### Code Structure:
- **Main Script**: Contains the main script for running the chatbot using Streamlit.
- **Model Initialization**: Initializes the language model and tokenizer for text generation tasks.
- **Prompt Templates**: Defines prompt templates for chatbot interactions and conversation history tracking.
- **Conversation Chain**: Manages the conversation flow and maintains conversation history.
- **Memory Management**: Utilizes a memory buffer to store and retrieve conversation history.

### Usage Instructions:
1. Ensure all dependencies are installed (`streamlit`, `transformers`, etc.).
2. Run the main script (`main.py`) to start the Streamlit application.
3. Input queries related to web development tasks and engage in conversation with the chatbot.
4. Explore code examples, seek explanations, and interact with the chatbot to accomplish web development tasks efficiently.

## Contributing
If you'd like to contribute to this repository by adding new chatbots or improving existing ones, please feel free to submit a pull request. We welcome contributions from the community to enhance the functionality and usability of our chatbots.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
