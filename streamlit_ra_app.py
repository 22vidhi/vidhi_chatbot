"""
Streamlit Cloud Deployment Entry Point for RA Agent
"""

import streamlit as st

# Page configuration for Streamlit Cloud
st.set_page_config(
    page_title="RA Agent - Regulatory Affairs Automation",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for RA Agent
if "ra_initialized" not in st.session_state:
    st.session_state.ra_initialized = False

def main():
    # App Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; text-align: center; margin-bottom: 0.5rem;">
            🔬 Regulatory Affairs Agent
        </h1>
        <p style="color: white; text-align: center; opacity: 0.9; margin-bottom: 0;">
            AI-Powered Regulatory Document Generation & Automation
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Company/Security Notice
    st.markdown("""
    <div style="background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 8px;
                padding: 1rem; margin-bottom: 1rem;">
        <h4 style="color: #856404; margin-bottom: 0.5rem;">🔒 Regulatory Compliance</h4>
        <p style="color: #856404; margin: 0; font-size: 0.9em;">
            This tool is designed for regulatory affairs professionals only.
            All outputs require professional review before regulatory submission.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize RA Agent
    if not st.session_state.ra_initialized:
        try:
            from ra_agent.ra_ui import display_ra_main
            st.session_state.ra_initialized = True
        except ImportError as e:
            st.error(f"❌ RA Agent initialization failed: {e}")
            st.info("Please ensure all dependencies are installed.")
            return

    # Main RA Agent Interface
    try:
        from ra_agent.ra_ui import display_ra_main
        display_ra_main()

    except Exception as e:
        st.error(f"❌ RA Agent Error: {str(e)}")

        # Fallback: Show basic functionality
        st.subheader("🧪 Basic RA Agent Test")
        with st.expander("System Status"):
            st.code(f"""
RA Agent Status: {st.session_state.ra_initialized}
Error Details: {str(e)}
            """)

        # Basic functionality test
        test_prompt = st.text_area("Test RA Query", "Generate a CSR outline for regulatory submission")
        if st.button("Test RA Processing"):
            st.info("This is a basic test. Full RA functionality requires proper setup.")
            st.write("Test prompt received:", test_prompt)

if __name__ == "__main__":
    main()
