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
            "Purchase": "[$5/Y; $0.50/M]({PURCHASE_LINK})"
        },
        {
            "Title": "Silver Level",
            "ID": "AI_010",
            "Description": "Minimal access to Bronze Level features with greater customizability and camera & voice integration",
            "Purchase": "[$8/Y; $0.75/M]({PURCHASE_LINK})"
        },
        {
            "Title": "Gold Level",
            "ID": "AI_011",
            "Description": "Greater access to Silver Level features with prebuilt commands for (1) FRQ writing, (2) APHG Flashcard creation, (3) Cornell notetaking and more",
            "Purchase": "[$10/Y; $1/M]({PURCHASE_LINK})"
        },
        {
            "Title": "Platinum Level",
            "ID": "AI_100",
            "Description": "Greater access to Gold Level features with unrestricted file types (image, video, document, etc.) and unlimited file uploads",
            "Purchase": "[$15/Y; $2/M]({PURCHASE_LINK})"
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
    "English I Noteguides": [
        {
            "Title": "'The Odyssey' Notes",
            "ID": "E1_001",
            "Description": "Book-by-book summary of 'The Odyssey'",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        }
    ],
    "Pre-AP Biology Noteguides": [
        {
            "Title": "Chapter 1: The Science of Biology",
            "ID": "BIO_001",
            "Description": "Full, in-depth study & review noteguide for Chapter 1 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 2: The Chemistry of Life",
            "ID": "BIO_002",
            "Description": "Full, in-depth study & review noteguide for Chapter 2 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 3: The Biosphere",
            "ID": "BIO_003",
            "Description": "Full, in-depth study & review noteguide for Chapter 3 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 4: Ecosystems & Communities",
            "ID": "BIO_004",
            "Description": "Full, in-depth study & review noteguide for Chapter 4 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 5: Populations",
            "ID": "BIO_005",
            "Description": "Full, in-depth study & review noteguide for Chapter 5 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 6: Humans in the Biosphere",
            "ID": "BIO_006",
            "Description": "Full, in-depth study & review noteguide for Chapter 6 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 7: Cell Structure and Function",
            "ID": "BIO_007",
            "Description": "Full, in-depth study & review noteguide for Chapter 7 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 8: Photosynthesis",
            "ID": "BIO_008",
            "Description": "Full, in-depth study & review noteguide for Chapter 8 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 9: Cellular Respiration & Fermentation",
            "ID": "BIO_009",
            "Description": "Full, in-depth study & review noteguide for Chapter 9 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 10: Cell Growth and Division",
            "ID": "BIO_010",
            "Description": "Full, in-depth study & review noteguide for Chapter 10 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 11: Introduction to Genetics",
            "ID": "BIO_011",
            "Description": "Full, in-depth study & review noteguide for Chapter 11 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 12: DNA",
            "ID": "BIO_012",
            "Description": "Full, in-depth study & review noteguide for Chapter 12 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 13: RNA and Protein Synthesis",
            "ID": "BIO_013",
            "Description": "Full, in-depth study & review noteguide for Chapter 13 of Pre-AP Biology",
            "Purchase": "[$2]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 14: Human Heredity",
            "ID": "BIO_014",
            "Description": "Full, in-depth study & review noteguide for Chapter 14 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 15: Genetic Engineering",
            "ID": "BIO_015",
            "Description": "Full, in-depth study & review noteguide for Chapter 15 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 16: Darwin’s Theory of Evolution",
            "ID": "BIO_016",
            "Description": "Full, in-depth study & review noteguide for Chapter 16 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 17: Evolution of Populations",
            "ID": "BIO_017",
            "Description": "Full, in-depth study & review noteguide for Chapter 17 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 18: Classification",
            "ID": "BIO_018",
            "Description": "Full, in-depth study & review noteguide for Chapter 18 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 20: Viruses & Prokaryotes",
            "ID": "BIO_020",
            "Description": "Full, in-depth study & review noteguide for Chapter 20 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 22: Introduction to Plants",
            "ID": "BIO_022",
            "Description": "Full, in-depth study & review noteguide for Chapter 22 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 23: Plant Structure & Function",
            "ID": "BIO_023",
            "Description": "Full, in-depth study & review noteguide for Chapter 23 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 24: Plant Reproduction & Response",
            "ID": "BIO_024",
            "Description": "Full, in-depth study & review noteguide for Chapter 24 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 25: Introduction to Animals",
            "ID": "BIO_025",
            "Description": "Full, in-depth study & review noteguide for Chapter 25 of Pre-AP Biology",
            "Purchase": "[$0.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 27: Animal Systems I",
            "ID": "BIO_027",
            "Description": "Full, in-depth study & review noteguide for Chapter 27 of Pre-AP Biology",
            "Purchase": "[$1.50]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 28: Animal Systems II",
            "ID": "BIO_028",
            "Description": "Full, in-depth study & review noteguide for Chapter 28 of Pre-AP Biology",
            "Purchase": "[$2]({PURCHASE_LINK})"
        },
        {
            "Title": "Chapter 30: The Human Body",
            "ID": "BIO_030",
            "Description": "Full, in-depth study & review noteguide for Chapter 30 of Pre-AP Biology",
            "Purchase": "[$1]({PURCHASE_LINK})"
        },
        {
            "Title": "All Pre-AP Biology Noteguides + 'The Hot Zone' Summary",
            "ID": "BIO_1000",
            "Description": "All chapter noteguides for Pre-AP Biology with an added chapter-by-chapter summary of 'The Hot Zone'",
            "Purchase": "[$18]({PURCHASE_LINK})"
        }
    ]
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
