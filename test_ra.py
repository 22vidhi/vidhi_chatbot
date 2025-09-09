"""
Test script for RA Agent functionality
"""

import streamlit as st
import asyncio
from ra_agent.ra_ui import display_ra_main

def main():
    st.set_page_config(
        page_title="RA Agent Test",
        page_icon="🔬",
        layout="wide"
    )

    st.title("🧪 RA Agent Test Environment")

    try:
        display_ra_main()
        st.success("✅ RA Agent loaded successfully!")
    except Exception as e:
        st.error(f"❌ RA Agent Error: {str(e)}")
        st.info("Trying alternative import...")

        try:
            # Fallback import
            import ra_agent.ra_core as ra_core
            ra_agent = ra_core.ra_agent

            st.markdown("### RA Agent Core Test")
            st.write(f"Knowledge Manager: {type(ra_agent.knowledge_manager).__name__}")
            st.write(f"AI Synthesizer: {type(ra_agent.ai_synthesizer).__name__}")
            st.write(f"Document Generator: {type(ra_agent.doc_generator).__name__}")

        except Exception as e2:
            st.error(f"❌ Fallback failed: {str(e2)}")

if __name__ == "__main__":
    main()
