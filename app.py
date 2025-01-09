import streamlit as st
from Multi_agent_langflow import run_flow

# Set up page configuration
st.set_page_config(
    layout="centered", 
    page_title="Flipkart Multi-Agent Customer Support", 
    page_icon="🚀"
)

# Header Section
c1, c2 = st.columns([0.2, 1.8])

with c1:
    st.image("images/flipkart_logo.png", width=70)
with c2:
    st.caption("")
    st.title("Flipkart Multi-Agent Customer Support")

# Sidebar Section
st.sidebar.markdown("---")
st.sidebar.write(
    """
    **Created by [Harishwar T G](https://www.linkedin.com/in/harishwartg/)**

    This project leverages **LangFlow** and **AstraDB** to deliver intelligent customer support via multiple agents:
    - **DB Lookup Agent:** Provides order and product details.
    - **RAG Agent:** Retrieves answers from FAQs.
    - **Google Web Search Agent:** Suggests and compares products.

    [GitHub Repository](https://github.com/HarishwarTG/Multi_Agent_Customer_Support)
    """
)
st.sidebar.markdown("---")

# Main Content Section
st.markdown(
    """
    Welcome to the Flipkart Multi-Agent Customer Support! Our intelligent agents are here to assist with your queries:
    - Check your **order and product details**.
    - Get **instant answers** to FAQs.
    - Compare and suggest products using **Google Web Search**.
    """
)

# Input Section
st.markdown("---")
st.write("### Chat Interface")
message = st.text_area("Message", placeholder="Ask something about your orders, products, or comparisons...")

if st.button("Run Flow"):
    if not message.strip():
        st.error("Please enter a message.")
    else:
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
                response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                st.markdown(f"**Response:** {response_text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer Section
st.markdown("---")
st.write(
    """
    ### Supported Features:
    - Retrieve accurate order and product information.
    - Get detailed product comparisons and recommendations.
    - Answer FAQs efficiently.

    *Disclaimer:* This is a demonstration project for learning purposes.
    """
)
