# 🔬 Regulatory Affairs (RA) Agent

AI-powered regulatory document generation and automation for pharmaceutical compliance.

## 🚀 Features

### 📝 **Document Generation**
- Clinical Study Report (CSR) outlines
- Investigator Brochures (IB)
- Regulatory Submission documents
- Cover Letters and Labeling Drafts
- Multi-format export (DOCX, PDF)

### 🤖 **AI Integration**
- Google Gemini primary AI
- OpenAI integration support
- Dual AI processing with reconciliation
- Confidence scoring and validation

### 📚 **Knowledge Base**
- RA-approved document storage
- Semantic search with RAG
- ChromaDB vector database
- Multi-format file support (PDF, DOCX, XLSX)

### 🔒 **Compliance & Security**
- Regulatory compliance framework
- Audit trails and traceability
- Professional formal language
- Role-based access controls

## 🛠️ Setup & Deployment

### Prerequisites
- Python 3.8+
- Streamlit Cloud account
- GitHub repository

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ra-agent.git
   cd ra-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   Create `.streamlit/secrets.toml`:
   ```toml
   GOOGLE_API_KEY = "your_google_api_key"
   OPENAI_API_KEY = "your_openai_api_key"  # Optional
   ```

### Local Development

```bash
streamlit run streamlit_ra_app.py
```

## 📦 **Deployment to Streamlit Cloud**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add RA Agent deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Connect your GitHub repository
   - Set entry point to: `streamlit_ra_app.py`
   - Add secrets in Streamlit Cloud dashboard
   - Deploy!

## 🏗️ **Project Structure**

```
ra-agent/
├── streamlit_ra_app.py          # Main deployment entry point
├── ra_agent/                    # RA Agent core module
│   ├── __init__.py
│   ├── ra_core.py              # Core RA functionality
│   ├── ra_ui.py               # Streamlit UI components
│   └── templates/
│       ├── __init__.py
│       └── csr_template.py    # Document templates
├── .streamlit/
│   └── secrets.toml           # API keys
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 **Configuration**

### API Keys Required
- **Google Gemini API**: Primary AI for document generation
- **OpenAI API**: Optional for ChatGPT integration

### Environment Variables
Set these in your Streamlit Cloud dashboard or `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_key_here"
OPENAI_API_KEY = "your_key_here"
```

## 🎯 **Usage**

1. **Document Generation**: Fill out the form with your regulatory requirements
2. **AI Selection**: Choose between Local (Gemini), ChatGPT, or Dual AI mode
3. **Template Selection**: Pick from RA-approved document templates
4. **Generate & Download**: Get production-ready documents in multiple formats

## 📋 **Example Prompt**
```
Generate a structured outline for a Clinical Study Report (CSR)
for Neptunimab targeting the FDA. Use formal language and
include all key sections with placeholder text in brackets.
```

## ⚖️ **Compliance Note**
>This tool is designed for regulatory affairs professionals only.
>All generated content requires professional review and approval
>before any regulatory submission.

## 📞 **Support**
For support or questions about pharmaceutical regulatory requirements,
please consult your RA team or regulatory authorities.
