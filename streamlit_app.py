import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    .inventory-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        color: #ffffff;
    }
    
    .inventory-table th, .inventory-table td {
        padding: 12px 15px;
        text-align: left;
        border: 1px solid #2d3b5e;
    }
    
    .inventory-table th {
        background-color: #0b1936;
        color: #5799f7;
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

def render_table(category, items):
    """Generates HTML table for a specific category."""
    table_html = f"""
    <h2 style="color:#5799f7;">{category}</h2>
    <table class="inventory-table">
        <thead>
            <tr>
                <th>Title</th>
                <th>ID</th>
                <th>Description</th>
                <th>Purchase</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for item in items:
        table_html += f"""
            <tr>
                <td>{item['Title']}</td>
                <td>{item['ID']}</td>
                <td>{item['Description']}</td>
                <td><a href="{PURCHASE_LINK}" class="purchase-button" target="_blank">Purchase</a></td>
            </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    return table_html

def main():
    st.title("🛍️ Mainframe Shop")
    
    # Render tables for each category using st.components.v1.html
    for category, items in INVENTORY_DATA.items():
        table_html = render_table(category, items)
        
        # Use components.html to render the table properly
        components.html(table_html, height=400, scrolling=True)

if __name__ == "__main__":
    main()
