 🎙️ Vidhi_Chatbot

 An interactive AI-powered chatbot built with Streamlit, peechRecognition, and pyttsx3, integrated with Ollama for LLM responses.
 The chatbot supports voice input and speech output, providing a modern conversational UI.

 ✨ Features

 * 🎤 Voice Input using `SpeechRecognition`
 * 🗣️ Text-to-Speech Output using `pyttsx3`
 * 💬 LLM Integration with Ollama
 * 🌐 Streamlit UI for modern chat experience
 * ⚡ Works as both text & voice assistant

 📂 Project Structure

 📦 vidhi_chatbot
 ┣ 📜 app.py              # Main chatbot application
 ┣ 📜 requirements.txt    # Dependencies
 ┗ 📜 README.md           # Project documentation

 🚀 Installation

  1. Clone the repo
  bash
  git clone https://github.com/your-username/vidhi_chatbot.git
  cd vidhi_chatbot

  2. Create a virtual environment (recommended)
  bash
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows

  3. Install dependencies
  bash
  pip install -r requirements.txt

 ⚠️ If you face issues installing PyAudio on Windows:

 * Download the `.whl` from [PyAudio unofficial builds](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
 * Install it with:

  bash
  pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
  
 ▶️ Run the App
 bash
 streamlit run app.py

⚡ Usage
1. Start the app.
2. Use the microphone button to give voice input.
3. The chatbot will process speech → text → Ollama response → speech output.

🛠️ Tech Stack

* Python 3.9+
* Streamlit → Frontend
* SpeechRecognition → Voice input
* pyttsx3 → Voice output
* Ollama → LLM engine
* LangChain + ChromaDB → Memory / Context

📜 License
 This project is licensed under the MIT License.

🎓 Conclusion

Overall, working on this project has been a valuable learning experience.
I gained practical skills in:
Python development
Voice recognition and text-to-speech
LLM integration with Ollama
Building interactive apps using Streamlit
This chatbot project gave me exposure to real-world challenges in AI and automation, and helped me grow my technical and problem-solving skills. I am grateful for the opportunity to build it and excited to keep improving it further

✨ Made with ❤️ by Vidhi

👉 Do you want me to also add screenshots / demo GIF section in README so it looks even more impressive on GitHub?
