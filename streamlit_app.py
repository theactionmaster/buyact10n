import streamlit as st
import pandas as pd

# Sample inventory data for multiple categories
INVENTORY_DATA = {
    "Hardware": [
        {
            "Title": "Quantum Processor X9",
            "ID": "MF-001",
            "Description": "Next-gen quantum processing unit with 128 qubits"
        },
        {
            "Title": "Advanced GPU Zeta",
            "ID": "MF-003",
            "Description": "High-performance GPU for AI workloads"
        },
    ],
    "Peripherals": [
        {
            "Title": "Neural Interface Module",
            "ID": "MF-002",
            "Description": "High-bandwidth neural connectivity interface"
        },
        {
            "Title": "Holographic Display Unit",
            "ID": "MF-004",
            "Description": "Interactive holographic display for immersive experiences"
        },
    ],
}

def main():
    st.title("🛍️ Mainframe Shop")
    
    # Render tables for each category
    for category, items in INVENTORY_DATA.items():
        st.markdown(f"## {category}")  # Heading for the category
        
        # Convert the data into a DataFrame for display with st.table
        df = pd.DataFrame(items)
        
        # Display the table
        st.table(df)

if __name__ == "__main__":
    main()
