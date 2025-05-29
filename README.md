# Agentic AI Assistant

This is my first Agentic AI project developed as part of the Governor House IT Course. The project implements an intelligent AI assistant using the `agents` library in Python, integrated with a generative AI model. The assistant is designed to process natural language queries and perform tasks using custom tools, such as a mathematical calculator.

## Features
- **Conversational AI Agent**: Built using the `agents` library to handle user queries interactively.
- **Custom Calculator Tool**: Includes a `calculate_numbers` tool that performs basic arithmetic operations (addition, subtraction, multiplication, division) with robust error handling.
- **Secure Configuration**: Uses `python-dotenv` to manage API keys securely via environment variables.
- **Efficient Project Management**: Utilizes `uv` for dependency management and virtual environment setup.
- **Modular Design**: Structured with `RunConfig` and `Agent` components for scalability and reusability.

## Prerequisites
To run this project, you need:
- Python 3.8 or higher
- `uv` (Python package and environment manager)
- A valid API key for a generative AI model (e.g., Google Gemini or OpenAI)
- A `.env` file with your API key

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/agentic-ai-assistant.git
   cd agentic-ai-assistant
   ```

2. **Set Up Virtual Environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure `pyproject.toml` is configured, then run:
   ```bash
   uv sync
   ```

4. **Configure API Key**:
   Create a `.env` file in the project root with your API key:
   ```
   gemini_api_key=your_actual_gemini_api_key
   # or
   openai_api_key=your_actual_openai_api_key
   ```

## Usage
1. **Run the Application**:
   ```bash
   uv run src/explore_uv/main.py
   ```

2. **Example Queries**:
   - Mathematical operations:
     ```bash
     Calculate 5 + 3
     # Expected output: 8.0
     ```
     ```bash
     Calculate 10 / 2
     # Expected output: 5.0
     ```
   - Note: The current implementation does not support real-time weather queries. For weather data, consider integrating an external API like OpenWeatherMap.

3. **Customizing the Agent**:
   - Modify the `instructions` in `Agent` to change the assistant's behavior.
   - Add new tools by defining functions with the `@function_tool` decorator.

## Project Structure
```
agentic-ai-assistant/
├── src/
│   └── explore_uv/
│       └── main.py        # Main application code
├── .env                   # Environment variables (API keys)
├── pyproject.toml         # Project dependencies and configuration
└── README.md              # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the project's style and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Governor House IT Course**: For providing the foundation and guidance for this project.
- **DeepSeek**: For additional support in troubleshooting and code optimization.
- **Open-Source Community**: For the amazing libraries like `agents` and `python-dotenv`.

---

Happy to share my first step into Agentic AI! Feel free to explore the code, provide feedback, or suggest new features. Let's build smarter AI together! 🚀