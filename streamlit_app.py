import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Mainframe Shop",
    page_icon="./favicon.ico",
    layout="wide"
)

# Google Form URL (replace with actual form URL)
PURCHASE_LINK = "https://forms.google.com"

# Sample inventory data for multiple categories
INVENTORY_DATA = {
    "Mainframe AI": [
        {
            "Title": "Bronze Level",
            "ID": "AI_001",
            "Description": "Basic access to AI chatbot features",
            "Purchase": "[$0.50/M; $5/Y]({PURCHASE_LINK})"
        },
        {
            "Title": "Silver Level",
            "ID": "AI_010",
            "Description": "Minimal access to Bronze Level features with greater customizability and camera & voice integration",
            "Purchase": "[$0.75/M; $8/Y]({PURCHASE_LINK})"
        },
        {
            "Title": "Gold Level",
            "ID": "AI_011",
            "Description": "Greater access to Silver Level features with prebuilt commands for (1) FRQ writing, (2) APHG Flashcard creation, (3) Cornell notetaking and more",
            "Purchase": "[$1/M; $10/Y]({PURCHASE_LINK})"
        },
        {
            "Title": "Platinum Level",
            "ID": "AI_100",
            "Description": "Greater access to Gold Level features with unrestricted file types (image, video, document, etc.) and unlimited file uploads",
            "Purchase": "[$2/M; $15/Y]({PURCHASE_LINK})"
        }
    ],
    "AP Human Geography Noteguides": [
        {
            "Title": "Unit 1: Thinking Geographically",
            "ID": "HG_001",
            "Description": "Full, in-depth study & review noteguide for Unit 1 of AP Human Geography",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 2: Population & Migration Patterns",
            "ID": "HG_010",
            "Description": "Full, in-depth study & review noteguide for Unit 2 of AP Human Geography",
            "Purchase": "[$2.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 3: Cultural Patterns & Processes",
            "ID": "HG_011",
            "Description": "Full, in-depth study & review noteguide for Unit 3 of AP Human Geography",
            "Purchase": "[$5]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 4: Political Patterns & Processes",
            "ID": "HG_100",
            "Description": "Full, in-depth study & review noteguide for Unit 4 of AP Human Geography",
            "Purchase": "[$4.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 5: Agricultural & Rural Land-Use Patterns",
            "ID": "HG_101",
            "Description": "Full, in-depth study & review noteguide for Unit 5 of AP Human Geography",
            "Purchase": "[$7]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 6: Cities & Urban Land-Use Patterns",
            "ID": "HG_110",
            "Description": "Full, in-depth study & review noteguide for Unit 6 of AP Human Geography",
            "Purchase": "[$5]({PURCHASE_LINK})"
        },
        {
            "Title": "Unit 7: Industrialization & Economic Development",
            "ID": "HG_111",
            "Description": "Full, in-depth study & review noteguide for Unit 7 of AP Human Geography",
            "Purchase": "[$6]({PURCHASE_LINK})"
        },
        {
            "Title": "All AP Human Geography Noteguides + FRQ Review Guide",
            "ID": "HG_1000",
            "Description": "All 7 noteguides with an added FRQ review guide",
            "Purchase": "[$15]({PURCHASE_LINK})"
        }
    ],
}

def main():
    
    st.title("🤑 Mainframe Shop")
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
