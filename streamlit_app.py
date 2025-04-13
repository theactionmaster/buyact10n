import streamlit as st

# Custom CSS to match Mainframe AI styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    .back-button {
        width: 300px;
        margin-top: 20px;
        padding: 10px 20px;
        font-size: 18px;
        background-color: #0b1936;
        color: #5799f7;
        border: 2px solid #4a83d4;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 15px rgba(74, 131, 212, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Google Form URL (replace with actual form URL)
PURCHASE_LINK = "https://forms.google.com"

# Sample inventory data - customize this in your code
INVENTORY_DATA = [
    {
        "Title": "Quantum Processor X9",
        "ID": "MF-001",
        "Category": "Hardware",
        "Description": "Next-gen quantum processing unit with 128 qubits"
    },
    {
        "Title": "Neural Interface Module",
        "ID": "MF-002",
        "Category": "Peripherals",
        "Description": "High-bandwidth neural connectivity interface"
    }
]

def main():
    # Title Section
    st.title("🛍️ Mainframe Shop")
    
    # Back to AI button
    st.link_button("Back to **Mainframe AI**", "https://mainframe.streamlit.app")
    
    st.divider()
    
    # Inventory Table
    st.markdown("### Available Components")
    
    # Table Header
    st.markdown("""
    | **Title** | **ID** | Category | Description | Purchase |
    |-----------|--------|----------|-------------|----------|
    """, unsafe_allow_html=True)
    
    # Table Rows
    for item in INVENTORY_DATA:
        st.markdown(f"""
        | {item['Title']} | {item['ID']} | {item['Category']} | {item['Description']} | 
        [Purchase]({PURCHASE_LINK}){{target="_blank"}} |
        """, unsafe_allow_html=True)
    
    st.divider()

if __name__ == "__main__":
    main()
