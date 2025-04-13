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
    
    st.title("🛍️ Mainframe Shop")
    st.link_button("Back to **Mainframe AI**", "https://mainframe.streamlit.app")
    
    # Render tables for each category
    for category, items in INVENTORY_DATA.items():
        st.markdown(f"## {category}")  # Heading for the category
        
        # Convert the data into a DataFrame for display with st.table
        df = pd.DataFrame(items)
        
        # Display the table without index
        st.table(df.style.hide(axis="index"))

if __name__ == "__main__":
    main()
