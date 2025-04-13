import streamlit as st
import pandas as pd

# Google Form URL (replace with actual form URL)
PURCHASE_LINK = "https://forms.google.com"

# Sample inventory data for multiple categories
INVENTORY_DATA = {
    "Hardware": [
        {
            "Title": "Quantum Processor X9",
            "ID": "MF-001",
            "Description": "Next-gen quantum processing unit with 128 qubits",
            "Purchase": f"[Purchase]({PURCHASE_LINK})"
        },
        {
            "Title": "Advanced GPU Zeta",
            "ID": "MF-003",
            "Description": "High-performance GPU for AI workloads",
            "Purchase": f"[Purchase]({PURCHASE_LINK})"
        },
    ],
    "Peripherals": [
        {
            "Title": "Neural Interface Module",
            "ID": "MF-002",
            "Description": "High-bandwidth neural connectivity interface",
            "Purchase": f"[Purchase]({PURCHASE_LINK})"
        },
        {
            "Title": "Holographic Display Unit",
            "ID": "MF-004",
            "Description": "Interactive holographic display for immersive experiences",
            "Purchase": f"[Purchase]({PURCHASE_LINK})"
        },
    ],
}

def main():
    # Back to Mainframe AI button
    st.markdown(
        f'<a href="https://mainframe.streamlit.app" style="text-decoration:none;">'
        f'<button style="background-color:#0b1936; color:#5799f7; padding:10px 20px; border:none; border-radius:5px; font-size:16px;">Back to Mainframe AI</button>'
        f'</a>',
        unsafe_allow_html=True,
    )
    
    st.title("🛍️ Mainframe Shop")
    
    # Render tables for each category
    for category, items in INVENTORY_DATA.items():
        st.markdown(f"## {category}")  # Heading for the category
        
        # Convert the data into a DataFrame for display with st.table
        df = pd.DataFrame(items)
        
        # Display the table without index
        st.table(df.style.hide(axis="index"))

if __name__ == "__main__":
    main()
