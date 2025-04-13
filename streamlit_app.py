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
    
    /* Table styling */
    .inventory-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
    }
    
    .inventory-table th {
        background-color: #0b1936;
        color: #5799f7;
        padding: 12px 15px;
        text-align: left;
    }
    
    .inventory-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #2d3b5e;
    }
    
    .purchase-button {
        background-color: #1c275c;
        color: #73abfa !important;
        padding: 8px 15px;
        border-radius: 5px;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .purchase-button:hover {
        background-color: #2d3b5e;
        color: #8fbfff !important;
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

def check_password():
    """Password check for shop access"""
    if 'access_level' not in st.session_state:
        st.session_state['access_level'] = None

    def password_entered():
        if st.session_state["shop_password"] == st.secrets["PW"]:
            st.session_state["shop_password_correct"] = True
            st.session_state["access_level"] = "Verified"
        else:
            st.session_state["shop_password_correct"] = False

    if "shop_password_correct" in st.session_state:
        if st.session_state["shop_password_correct"]:
            return True, st.session_state["access_level"]

    st.title("🛍️ Mainframe Shop")
    st.markdown("### Vendor portal authentication")
    st.text_input(
        "Password", 
        type="password",
        on_change=password_entered,
        key="shop_password"
    )
    
    if "shop_password_correct" in st.session_state:
        if not st.session_state["shop_password_correct"]:
            st.error("Incorrect vendor code")
    
    return False, None

def main():
    # Password check
    password_correct, access_level = check_password()
    if not password_correct:
        return
    
    # Main content
    st.title("🛍️ Mainframe Shop")
    st.link_button("Back to **Mainframe AI**", "https://mainframe.streamlit.app")
    st.divider()
    
    # Inventory table
    st.markdown("### Available Components")
    
    # Table header
    st.markdown("""
    <table class="inventory-table">
        <tr>
            <th>Title</th>
            <th>ID</th>
            <th>Category</th>
            <th>Description</th>
            <th>Purchase</th>
        </tr>
    """, unsafe_allow_html=True)
    
    # Table rows
    for item in INVENTORY_DATA:
        st.markdown(f"""
        <tr>
            <td><strong>{item['Title']}</strong></td>
            <td><strong>{item['ID']}</strong></td>
            <td>{item['Category']}</td>
            <td>{item['Description']}</td>
            <td>
                <a href="{PURCHASE_LINK}" class="purchase-button" target="_blank">Purchase</a>
            </td>
        </tr>
        """, unsafe_allow_html=True)
    
    # Close table
    st.markdown("</table>", unsafe_allow_html=True)
    st.divider()

if __name__ == "__main__":
    main()
