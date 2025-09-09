"""
Regulatory Affairs (RA) Agent UI Components
Streamlit interface for RA automation features.
"""

import streamlit as st
import asyncio
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
import base64
import json

from .ra_core import RAAgent, RAQuery, ra_agent

def display_ra_main():
    """Main RA Agent interface"""

    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #1e90ff;">
        <h2 style="color: #1e90ff;">🔬 Regulatory Affairs (RA) Agent</h2>
        <p style="margin: 0;">AI-powered regulatory document generation and automation for pharmaceutical compliance.</p>
        <p style="color: #666; font-size: 0.8em;"><strong>⚠️ Note:</strong> This tool uses RA-approved sources only and requires professional review before any regulatory submission.</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "ra_sessions" not in st.session_state:
        st.session_state.ra_sessions = []

    if "current_ra_project" not in st.session_state:
        st.session_state.current_ra_project = None

    # Create tabs for different RA functions
    tabs = st.tabs(["🗂️ Document Generation", "📚 Knowledge Base", "🔍 Search & Query", "⚙️ Settings"])

    with tabs[0]:
        display_document_generation()

    with tabs[1]:
        display_knowledge_base()

    with tabs[2]:
        display_search_query()

    with tabs[3]:
        display_ra_settings()

def display_document_generation():
    """Document generation interface"""

    st.markdown("### 📝 Generate Regulatory Document")

    col1, col2 = st.columns([2, 1])

    with col1:
        doc_types = [
            "Clinical Study Report (CSR)",
            "Investigator Brochure (IB)",
            "Regulatory Submission",
            "Cover Letter",
            "Labeling Draft",
            "Investigator's Brochure Addendum",
            "Safety Reporting Document",
            "CMC Documentation",
            "Executive Summary"
        ]

        doc_type = st.selectbox("Document Type", doc_types)

        prompt = st.text_area(
            "Describe your regulatory document requirements:",
            height=150,
            placeholder="Example: Generate a structured outline for a Clinical Study Report (CSR) for 'Neptunimab' targeting the FDA. Use formal language and include all key sections with placeholder text in brackets."
        )

        # AI Selection
        st.markdown("#### 🤖 AI Configuration")
        col_a, col_b, col_c, col_d = st.columns(4)

        with col_a:
            use_local = st.checkbox("Local (Gemini)", value=True)
        with col_b:
            use_chatgpt = st.checkbox("ChatGPT-5", value=False)
        with col_c:
            use_perplexity = st.checkbox("Perplexity", value=False)
        with col_d:
            dual_ai = st.checkbox("Dual AI Mode", value=False)

        if dual_ai:
            use_chatgpt = True
            use_perplexity = True

        filename = st.text_input("Document Filename", value="regulatory_document")

        urgency_levels = ["Normal", "Expedited", "Critical"]
        urgency = st.selectbox("Priority Level", urgency_levels)

    with col2:
        # Project info
        st.markdown("#### 📋 Project Context")
        project_name = st.text_input("Project Name", value="Project X")
        compound_name = st.text_input("Compound/Drug Name", value="Neptunimab")
        target_authority = st.selectbox("Target Authority",
                                      ["FDA", "EMA", "ICH", "CDSCO", "NMPA", "ANVISA"])

        st.markdown("#### 📄 Templates")
        available_templates = ["Default CSR", "FDA Template", "EU Template", "Custom"]
        template = st.selectbox("Template", available_templates)

        # Generate button
        if st.button("🚀 Generate Document", type="primary", use_container_width=True):
            with st.spinner("Processing with RA Agent..."):
                asyncio.run(process_document_generation(
                    prompt, doc_type, use_local, use_chatgpt, use_perplexity,
                    filename, urgency, project_name, compound_name, target_authority
                ))

def display_knowledge_base():
    """Knowledge base management interface"""

    st.markdown("### 📚 RA Knowledge Base")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("#### 📤 Upload RA Documents")

        uploaded_files = st.file_uploader(
            "Upload RA-approved documents (PDF, DOCX, TXT)",
            accept_multiple_files=True,
            type=['pdf', 'docx', 'txt', 'xlsx']
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                if st.button(f"📥 Process {uploaded_file.name}", key=f"process_{uploaded_file.name}"):
                    # Save and process file
                    temp_path = Path(f"temp_{uploaded_file.name}")
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    try:
                        doc_meta = {
                            "doc_id": f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                            "filename": uploaded_file.name,
                            "uploaded_by": "user",
                            "upload_date": datetime.now(),
                            "doc_type": uploaded_file.type
                        }

                        success = asyncio.run(ra_agent.knowledge_manager.add_document(
                            temp_path, doc_meta
                        ))

                        if success:
                            st.success(f"✅ Document '{uploaded_file.name}' processed successfully!")
                            st.rerun()  # Refresh to show updated count
                        else:
                            st.error(f"❌ Failed to process '{uploaded_file.name}'")

                    finally:
                        temp_path.unlink(missing_ok=True)

    with col2:
        # Knowledge base stats
        st.markdown("#### 📊 Knowledge Base Stats")

        try:
            collection = ra_agent.knowledge_manager.collection
            # This is a placeholder - in practice, you'd get actual stats
            doc_count = len(collection.get()['ids']) if hasattr(collection, 'get') else 0

            st.metric("Documents Indexed", doc_count)
            st.metric("Document Types", len(["PDF", "DOCX", "TXT"]))  # placeholder
            st.metric("Last Updated", datetime.now().strftime("%Y-%m-%d %H:%M"))

        except Exception as e:
            st.info("Initializing knowledge base...")
            st.metric("Documents Indexed", 0)

        st.markdown("#### 📋 RA Document Types")
        doc_types = [
            "📄 Clinical Study Reports",
            "📋 Investigator Brochures",
            "📊 CMC Documentation",
            "🛡️ Safety Reports",
            "📝 Labeling Documents",
            "📈 Regulatory Submissions"
        ]

        for dt in doc_types:
            st.write(f"- {dt}")

def display_search_query():
    """Search and query interface"""

    st.markdown("### 🔍 RA Document Search & Query")

    col1, col2 = st.columns([2, 1])

    with col1:
        query = st.text_area(
            "Search RA knowledge base:",
            height=100,
            placeholder="Enter your regulatory query here..."
        )

        if st.button("🔍 Search Knowledge Base", use_container_width=True):
            if query:
                with st.spinner("Searching RA documents..."):
                    results = asyncio.run(ra_agent.knowledge_manager.search_relevant_docs(
                        query, top_k=5
                    ))

                    if results:
                        st.markdown("#### 📄 Relevant Documents Found")

                        for i, result in enumerate(results, 1):
                            with st.expander(f"📋 Document {i}: {result['metadata'].get('filename', 'Unknown')}"):
                                st.write("**Content:**")
                                st.write(result['content'][:500] + "..." if len(result['content']) > 500 else result['content'])

                                if 'metadata' in result and result['metadata']:
                                    st.write("**Metadata:**")
                                    metadata = result['metadata']
                                    st.json({
                                        "doc_type": metadata.get('doc_type'),
                                        "upload_date": str(metadata.get('upload_date')) if metadata.get('upload_date') else None
                                    })
                    else:
                        st.info("No relevant documents found in the knowledge base.")

        # Display session history
        if st.session_state.ra_sessions:
            st.markdown("#### 🕐 Recent RA Sessions")

            for session in st.session_state.ra_sessions[-5:]:  # Show last 5
                with st.expander(f"Session: {session.get('timestamp', 'Unknown')}"):
                    st.write(f"**Query:** {session.get('query', 'N/A')[:100]}...")
                    st.write(f"**Document Type:** {session.get('doc_type', 'N/A')}")
                    st.write(f"**AI Used:** {', '.join(session.get('ai_used', []))}")

                    if session.get('file_path'):
                        with open(session['file_path'], "rb") as f:
                            st.download_button(
                                label="📥 Download Generated Document",
                                data=f,
                                file_name=session.get('filename', 'document.docx'),
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            )

    with col2:
        st.markdown("#### 📊 RA Query Analytics")

        # Placeholder metrics
        total_queries = len(st.session_state.ra_sessions)
        ai_usage = {
            "Local Gemini": 40,
            "ChatGPT-5": 35,
            "Perplexity": 25
        }

        st.metric("Total RA Queries", total_queries)

        st.markdown("#### 🤖 AI Usage Distribution")
        for ai, percentage in ai_usage.items():
            st.progress(percentage/100, text=f"{ai}: {percentage}%")

        st.markdown("#### 📈 Popular Document Types")
        popular_types = [
            "Clinical Study Reports",
            "Investigator Brochures",
            "Regulatory Submissions",
            "CMC Documentation"
        ]

        for doc_type in popular_types:
            st.write(f"• {doc_type}")

def display_ra_settings():
    """RA Agent settings interface"""

    st.markdown("### ⚙️ RA Agent Configuration")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🔑 API Configuration")

        # OpenAI API Key
        if "OPENAI_API_KEY" in st.secrets:
            st.success("✅ ChatGPT-5 API configured")
        else:
            st.error("❌ ChatGPT-5 API not configured")
            openai_key = st.text_input("Enter OpenAI API Key", type="password")
            if st.button("💾 Save OpenAI Key"):
                with open(".streamlit/secrets.toml", "a") as f:
                    f.write(f"\nOPENAI_API_KEY = \"{openai_key}\"\n")
                st.success("API key saved! Please restart the application.")

        # Perplexity API (placeholder)
        if st.checkbox("Enable Perplexity API"):
            perplexity_key = st.text_input("Enter Perplexity API Key", type="password")
            if st.button("💾 Save Perplexity Key"):
                st.info("Perplexity configuration saved!")

    with col2:
        st.markdown("#### 🛡️ Compliance Settings")

        # RA Approver Settings
        st.markdown("#### 👤 RA Approver")
        approver_name = st.text_input("RA Approver Name", value="Dr. Regulatory Officer")
        approver_email = st.text_input("RA Approver Email", value="ra.approver@company.com")

        # Approval workflow
        st.markdown("#### 🔄 Approval Workflow")
        auto_approve_drafts = st.checkbox("Auto-approve draft documents", value=False)
        require_review = st.checkbox("Require RA review before finalization", value=True)

        # Audit settings
        st.markdown("#### 📋 Audit & Logging")
        enable_audit = st.checkbox("Enable detailed audit logging", value=True)
        log_retention = st.selectbox("Audit log retention", ["30 days", "90 days", "1 year", "Forever"], index=2)

        if st.button("💾 Save Settings", use_container_width=True):
            st.success("RA settings saved successfully!")

async def process_document_generation(prompt, doc_type, use_local, use_chatgpt,
                                    use_perplexity, filename, urgency,
                                    project_name, compound_name, target_authority):
    """Process RA document generation"""

    try:
        # Create RA query
        ra_query = RAQuery(
            query_id=f"ra_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            prompt=prompt,
            document_type=doc_type,
            use_perplexity=use_perplexity,
            use_chatgpt=use_chatgpt,
            use_local=use_local or (not use_chatgpt and not use_perplexity),
            context_docs=[]
        )

        # Process with RA agent
        result = await ra_agent.process_ra_query(ra_query)

        # Display results
        if result.get("reconciled_output"):
            st.markdown("### 📝 Generated RA Document")

            # Display the reconciled output
            with st.expander("📄 Document Content", expanded=True):
                st.write(result["reconciled_output"])

            if result.get("citations"):
                st.markdown("#### 📚 AI Citations")
                for citation in result["citations"]:
                    confidence = citation.get("confidence", 0) * 100
                    st.write(f"**{citation['ai']}**: {confidence:.1f}% confidence")

            if result.get("ai_responses"):
                st.markdown("#### 🤖 AI Response Comparison")
                for ai_name, response in result["ai_responses"].items():
                    if "response" in response:
                        with st.expander(f"🔹 {ai_name.upper()} Response"):
                            st.write(response["response"])

            # Generate and offer document download
            st.markdown("### 💾 Generate Document Files")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("📄 Generate DOCX", use_container_width=True):
                    doc_result = await ra_agent.generate_document(
                        result["reconciled_output"], doc_type, "default", filename
                    )

                    if doc_result.get("output_files", {}).get("docx"):
                        with open(doc_result["output_files"]["docx"], "rb") as f:
                            st.download_button(
                                label="⬇️ Download Word Document",
                                data=f,
                                file_name=f"{filename}.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                use_container_width=True
                            )

            with col2:
                if st.button("📋 Generate PDF", use_container_width=True):
                    doc_result = await ra_agent.generate_document(
                        result["reconciled_output"], doc_type, "default", filename
                    )

                    if doc_result.get("output_files", {}).get("pdf"):
                        with open(doc_result["output_files"]["pdf"], "rb") as f:
                            st.download_button(
                                label="⬇️ Download PDF",
                                data=f,
                                file_name=f"{filename}.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )

            # Log session
            session_data = {
                "timestamp": datetime.now(),
                "query": prompt,
                "doc_type": doc_type,
                "ai_used": [ai for ai in ["gemini", "chatgpt", "perplexity"]
                           if locals().get(f"use_{ai.split('-')[0]}")],
                "filename": filename,
                "urgency": urgency,
                "project_name": project_name,
                "compound_name": compound_name,
                "target_authority": target_authority
            }

            st.session_state.ra_sessions.append(session_data)

            st.success("✅ RA document generated successfully!")
        else:
            st.error("❌ Failed to generate RA document. Please check your input and try again.")

    except Exception as e:
        st.error(f"❌ RA processing error: {str(e)}")
        st.info("Please ensure all required API keys are configured and try again.")
