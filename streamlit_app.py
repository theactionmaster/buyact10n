import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Mainframe Shop",
    page_icon="./favicon.ico",
    layout="wide"
)

# Google Form URL (replace with actual form URL)
PURCHASE_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSelL8q9moVB7O6XvmeJW2Th_XLAl6eh8qh9waUuaeX0iqUPkA/viewform?usp=dialog"

FREE_LINK = "https://drive.google.com/drive/folders/1pYmLOavrSBtM196vz3-mymdHiFByvya8?usp=drive_link"

# Sample inventory data for multiple categories
INVENTORY_DATA = {
    "Mainframe AI": [
        {
            "Title": "Bronze Level **(1 MONTH)**",
            "ID": "AIM_001",
            "Description": "Basic access to AI chatbot features (for 1 month)",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Silver Level **(1 MONTH)**",
            "ID": "AIM_010",
            "Description": "Minimal access to Bronze Level features with greater customizability and camera & voice integration (for 1 month)",
            "Purchase": "[$0.75]"
        },
        {
            "Title": "Gold Level **(1 MONTH)**",
            "ID": "AIM_011",
            "Description": "Greater access to Silver Level features with prebuilt commands for (1) FRQ writing, (2) APHG Flashcard creation, (3) Cornell notetaking and more (for 1 month)",
            "Purchase": "[$1]"
        },
        {
            "Title": "Platinum Level **(1 MONTH)**",
            "ID": "AIM_100",
            "Description": "Full access to Gold Level features with unrestricted file types (image, video, document, etc.) and unlimited file uploads (for 1 month)",
            "Purchase": "[$2]"
        },
        {
            "Title": "Bronze Level **(1 YEAR)**",
            "ID": "AIY_001",
            "Description": "Basic access to AI chatbot features (for 1 year)",
            "Purchase": "[$5]"
        },
        {
            "Title": "Silver Level **(1 YEAR)**",
            "ID": "AIY_010",
            "Description": "Minimal access to Bronze Level features with greater customizability and camera & voice integration (for 1 year)",
            "Purchase": "[$8]"
        },
        {
            "Title": "Gold Level **(1 YEAR)**",
            "ID": "AIY_011",
            "Description": "Greater access to Silver Level features with prebuilt commands for (1) FRQ writing, (2) APHG Flashcard creation, (3) Cornell notetaking and more (for 1 year)",
            "Purchase": "[$10]"
        },
        {
            "Title": "Platinum Level **(1 YEAR)**",
            "ID": "AIY_100",
            "Description": "Full access to Gold Level features with unrestricted file types (image, video, document, etc.) and unlimited file uploads (for 1 year)",
            "Purchase": "[$15]"
        }
    ],
    "Free Resources": [
        {
            "Title": "Free Resources",
            "ID": "FR_000",
            "Description": "Textbooks and simple resources provided/linked for free",
            "Purchase": "[Free (click here)]"
        }
    ],
    "AP Human Geography Noteguides": [
        {
            "Title": "Unit 1: Thinking Geographically",
            "ID": "HG_001",
            "Description": "Full, in-depth study & review noteguide for Unit 1 of AP Human Geography",
            "Purchase": "[Free]"
        },
        {
            "Title": "Unit 2: Population & Migration Patterns",
            "ID": "HG_010",
            "Description": "Full, in-depth study & review noteguide for Unit 2 of AP Human Geography",
            "Purchase": "[$2.50]"
        },
        {
            "Title": "Unit 3: Cultural Patterns & Processes",
            "ID": "HG_011",
            "Description": "Full, in-depth study & review noteguide for Unit 3 of AP Human Geography",
            "Purchase": "[$5]"
        },
        {
            "Title": "Unit 4: Political Patterns & Processes",
            "ID": "HG_100",
            "Description": "Full, in-depth study & review noteguide for Unit 4 of AP Human Geography",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Unit 5: Agricultural & Rural Land-Use Patterns",
            "ID": "HG_101",
            "Description": "Full, in-depth study & review noteguide for Unit 5 of AP Human Geography",
            "Purchase": "[$7]"
        },
        {
            "Title": "Unit 6: Cities & Urban Land-Use Patterns",
            "ID": "HG_110",
            "Description": "Full, in-depth study & review noteguide for Unit 6 of AP Human Geography",
            "Purchase": "[$5]"
        },
        {
            "Title": "Unit 7: Industrialization & Economic Development",
            "ID": "HG_111",
            "Description": "Full, in-depth study & review noteguide for Unit 7 of AP Human Geography",
            "Purchase": "[$6]"
        },
        {
            "Title": "All AP Human Geography Noteguides + FRQ Review Guide",
            "ID": "*HG_1000",
            "Description": "All 7 noteguides with an added FRQ review guide",
            "Purchase": "[$15]"
        }
    ],
    "Pre-AP Biology Noteguides": [
        {
            "Title": "Chapter 1: The Science of Biology",
            "ID": "BIO_001",
            "Description": "Full, in-depth study & review noteguide for Chapter 1 of Pre-AP Biology",
            "Purchase": "[Free]"
        },
        {
            "Title": "Chapter 2: The Chemistry of Life",
            "ID": "BIO_002",
            "Description": "Full, in-depth study & review noteguide for Chapter 2 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 3: The Biosphere",
            "ID": "BIO_003",
            "Description": "Full, in-depth study & review noteguide for Chapter 3 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 4: Ecosystems & Communities",
            "ID": "BIO_004",
            "Description": "Full, in-depth study & review noteguide for Chapter 4 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 5: Populations",
            "ID": "BIO_005",
            "Description": "Full, in-depth study & review noteguide for Chapter 5 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 6: Humans in the Biosphere",
            "ID": "BIO_006",
            "Description": "Full, in-depth study & review noteguide for Chapter 6 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 7: Cell Structure and Function",
            "ID": "BIO_007",
            "Description": "Full, in-depth study & review noteguide for Chapter 7 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 8: Photosynthesis",
            "ID": "BIO_008",
            "Description": "Full, in-depth study & review noteguide for Chapter 8 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 9: Cellular Respiration & Fermentation",
            "ID": "BIO_009",
            "Description": "Full, in-depth study & review noteguide for Chapter 9 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 10: Cell Growth and Division",
            "ID": "BIO_010",
            "Description": "Full, in-depth study & review noteguide for Chapter 10 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 11: Introduction to Genetics",
            "ID": "BIO_011",
            "Description": "Full, in-depth study & review noteguide for Chapter 11 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 12: DNA",
            "ID": "BIO_012",
            "Description": "Full, in-depth study & review noteguide for Chapter 12 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 13: RNA and Protein Synthesis",
            "ID": "BIO_013",
            "Description": "Full, in-depth study & review noteguide for Chapter 13 of Pre-AP Biology",
            "Purchase": "[$2]"
        },
        {
            "Title": "Chapter 14: Human Heredity",
            "ID": "BIO_014",
            "Description": "Full, in-depth study & review noteguide for Chapter 14 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 15: Genetic Engineering",
            "ID": "BIO_015",
            "Description": "Full, in-depth study & review noteguide for Chapter 15 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 16: Darwin’s Theory of Evolution",
            "ID": "BIO_016",
            "Description": "Full, in-depth study & review noteguide for Chapter 16 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 17: Evolution of Populations",
            "ID": "BIO_017",
            "Description": "Full, in-depth study & review noteguide for Chapter 17 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 18: Classification",
            "ID": "BIO_018",
            "Description": "Full, in-depth study & review noteguide for Chapter 18 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 20: Viruses & Prokaryotes",
            "ID": "BIO_020",
            "Description": "Full, in-depth study & review noteguide for Chapter 20 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 22: Introduction to Plants",
            "ID": "BIO_022",
            "Description": "Full, in-depth study & review noteguide for Chapter 22 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 23: Plant Structure & Function",
            "ID": "BIO_023",
            "Description": "Full, in-depth study & review noteguide for Chapter 23 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "Chapter 24: Plant Reproduction & Response",
            "ID": "BIO_024",
            "Description": "Full, in-depth study & review noteguide for Chapter 24 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 25: Introduction to Animals",
            "ID": "BIO_025",
            "Description": "Full, in-depth study & review noteguide for Chapter 25 of Pre-AP Biology",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Chapter 27: Animal Systems I",
            "ID": "BIO_027",
            "Description": "Full, in-depth study & review noteguide for Chapter 27 of Pre-AP Biology",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Chapter 28: Animal Systems II",
            "ID": "BIO_028",
            "Description": "Full, in-depth study & review noteguide for Chapter 28 of Pre-AP Biology",
            "Purchase": "[$2]"
        },
        {
            "Title": "Chapter 30: The Human Body",
            "ID": "BIO_030",
            "Description": "Full, in-depth study & review noteguide for Chapter 30 of Pre-AP Biology",
            "Purchase": "[$1]"
        },
        {
            "Title": "All Pre-AP Biology Noteguides + 'The Hot Zone' Summary",
            "ID": "BIO_1000",
            "Description": "All chapter noteguides for Pre-AP Biology with an added chapter-by-chapter summary of 'The Hot Zone'",
            "Purchase": "[$18]"
        }
    ],
    "AP Human Geography Online Paid Materials": [
        {
            "Title": "Mr. Sinn's Ultimate Review Packet",
            "ID": "HGP_001",
            "Description": "All the resources available in Mr. Sinn's Ultimate Review Packet for cheaper",
            "Purchase": "[$15]"
        },
        {
            "Title": "Heimler's History APHG Review Guide",
            "ID": "HGP_011",
            "Description": "All the resources available in the Heimler's History Review Guide for cheaper",
            "Purchase": "[$20]"
        },
        {
            "Title": "Heimler's History Video Noteguides",
            "ID": "HGP_100",
            "Description": "All the resources available in the Heimler's History Video Noteguides for cheaper",
            "Purchase": "[$5]"
        },
        {
            "Title": "Heimler's History Video Review Guide + Noteguides",
            "ID": "HGP_101",
            "Description": "All the resources available in Heimler's History paid APHG materials for cheaper",
            "Purchase": "[$22]"
        },
        {
            "Title": "UWorld Human Geography QBank",
            "ID": "HGP_110",
            "Description": "All the practice questions available in the UWorld APHG question bank for cheaper",
            "Purchase": "[$25]"
        },
        {
            "Title": "5 Steps to a 5 - AP Human Geography (2020 Edition)",
            "ID": "HGP_111",
            "Description": "The 2020 Edition for the 5 Steps to a 5 AP Human Geography book",
            "Purchase": "[$5]"
        },
        {
            "Title": "Barron's AP Human Geography",
            "ID": "HGP_1000",
            "Description": "The Barron's Human Geography book",
            "Purchase": "[$2]"
        },
        {
            "Title": "Princeton Review ASAP Human Geography",
            "ID": "HGP_1001",
            "Description": "The Princeton Review ASAP Human Geography book",
            "Purchase": "[$1.50]"
        },
        {
            "Title": "Princeton Review Human Geography (2021 Edition)",
            "ID": "HGP_1010",
            "Description": "The 2021 Edition of the Princeton Review Official Human Geography book",
            "Purchase": "[$2.50]"
        },
        {
            "Title": "The Cultural Landscape: An Introduction to Human Geography by James M. Rubenstein",
            "ID": "HGP_1011",
            "Description": "The Human Geography information book by James M. Rubenstein",
            "Purchase": "[$1]"
        },
        {
            "Title": "AP Human Geography MOTHERLOAD Packet",
            "ID": "HGP_1100",
            "Description": "The Motherload pakcet with all information needed for AP Human Geography",
            "Purchase": "[$1.75]"
        },
        {
            "Title": "Last-Minute AP Human Geography Review Packet",
            "ID": "HGP_1101",
            "Description": "A full AP Human Geography study guide perfect for a last-minute information review",
            "Purchase": "[$0.50]"
        }
    ],
    "AP Human Geography Project MCTs": [
        {
            "Title": "Project 1 MCT (Redacted Answers)",
            "ID": "HGR_001",
            "Description": "All the questions from the Project 1 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 1 MCT (Answered)",
            "ID": "HGA_001",
            "Description": "All the answers for the Project 1 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Project 2 MCT (Redacted Answers)",
            "ID": "HGR_002",
            "Description": "All the questions from the Project 2 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 2 MCT (Answered)",
            "ID": "HGA_002",
            "Description": "All the answers for the Project 2 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Project 3 MCT (Redacted Answers)",
            "ID": "HGR_003",
            "Description": "All the questions from the Project 3 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 3 MCT (Answered)",
            "ID": "HGA_003",
            "Description": "All the answers for the Project 3 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Project 4 MCT (Redacted Answers)",
            "ID": "HGR_004",
            "Description": "All the questions from the Project 4 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 4 MCT (Answered)",
            "ID": "HGA_004",
            "Description": "All the answers for the Project 4 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Project 5 MCT (Redacted Answers)",
            "ID": "HGR_005",
            "Description": "All the questions from the Project 5 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 5 MCT (Answered)",
            "ID": "HGA_005",
            "Description": "All the answers for the Project 5 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "Project 6 MCT (Redacted Answers)",
            "ID": "HGR_006",
            "Description": "All the questions from the Project 6 APHG MCT",
            "Purchase": "[$3]"
        },
        {
            "Title": "Project 6 MCT (Answered)",
            "ID": "HGA_006",
            "Description": "All the answers for the Project 6 APHG MCT",
            "Purchase": "[$4.50]"
        },
        {
            "Title": "ALL MCTs (Redacted Answers)",
            "ID": "HGR_1000",
            "Description": "All the questions from the APHG MCTs",
            "Purchase": "[$15]"
        },
        {
            "Title": "ALL MCTs (Answered)",
            "ID": "HGA_1000",
            "Description": "All the answers for the APHG MCTs",
            "Purchase": "[$18]"
        }
    ],
    "Pre-AP Algebra 2 Assignments": [
        {
            "Title": "Unit 1 Homeworks (Redacted Answers)",
            "ID": "A2R_001",
            "Description": "All the assignment sheets for Unit 1 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 1 Homeworks (Answered)",
            "ID": "A2A_001",
            "Description": "All the answered assignments for Unit 1 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 1 DOLs",
            "ID": "A2D_001",
            "Description": "All the DOL assignments for Unit 1 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 2 Homeworks (Redacted Answers)",
            "ID": "A2R_002",
            "Description": "All the assignment sheets for Unit 2 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 2 Homeworks (Answered)",
            "ID": "A2A_002",
            "Description": "All the answered assignments for Unit 2 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 2 DOLs",
            "ID": "A2D_002",
            "Description": "All the DOL assignments for Unit 2 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 3 Homeworks (Redacted Answers)",
            "ID": "A2R_003",
            "Description": "All the assignment sheets for Unit 3 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 3 Homeworks (Answered)",
            "ID": "A2A_003",
            "Description": "All the answered assignments for Unit 3 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 3 DOLs",
            "ID": "A2D_003",
            "Description": "All the DOL assignments for Unit 3 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 4 Homeworks (Redacted Answers)",
            "ID": "A2R_004",
            "Description": "All the assignment sheets for Unit 4 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 4 Homeworks (Answered)",
            "ID": "A2A_004",
            "Description": "All the answered assignments for Unit 4 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 4 DOLs",
            "ID": "A2D_004",
            "Description": "All the DOL assignments for Unit 4 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 5 Homeworks (Redacted Answers)",
            "ID": "A2R_005",
            "Description": "All the assignment sheets for Unit 5 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 5 Homeworks (Answered)",
            "ID": "A2A_005",
            "Description": "All the answered assignments for Unit 5 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 5 DOLs",
            "ID": "A2D_005",
            "Description": "All the DOL assignments for Unit 5 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 6 Homeworks (Redacted Answers)",
            "ID": "A2R_006",
            "Description": "All the assignment sheets for Unit 6 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 6 Homeworks (Answered)",
            "ID": "A2A_006",
            "Description": "All the answered assignments for Unit 6 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 6 DOLs",
            "ID": "A2D_006",
            "Description": "All the DOL assignments for Unit 6 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 7 Homeworks (Redacted Answers)",
            "ID": "A2R_007",
            "Description": "All the assignment sheets for Unit 7 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 7 Homeworks (Answered)",
            "ID": "A2A_007",
            "Description": "All the answered assignments for Unit 7 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 7 DOLs",
            "ID": "A2D_007",
            "Description": "All the DOL assignments for Unit 7 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 8 Homeworks (Redacted Answers)",
            "ID": "A2R_008",
            "Description": "All the assignment sheets for Unit 8 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 8 Homeworks (Answered)",
            "ID": "A2A_008",
            "Description": "All the answered assignments for Unit 8 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 8 DOLs",
            "ID": "A2D_008",
            "Description": "All the DOL assignments for Unit 8 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "Unit 9 Homeworks (Redacted Answers)",
            "ID": "A2R_009",
            "Description": "All the assignment sheets for Unit 9 of Pre-AP Algebra 2",
            "Purchase": "[$1]"
        },
        {
            "Title": "Unit 9 Homeworks (Answered)",
            "ID": "A2A_009",
            "Description": "All the answered assignments for Unit 9 of Pre-AP Algebra 2",
            "Purchase": "[$1.25]"
        },
        {
            "Title": "Unit 9 DOLs",
            "ID": "A2D_009",
            "Description": "All the DOL assignments for Unit 9 of Pre-AP Algebra 2",
            "Purchase": "[$0.50]"
        },
        {
            "Title": "All Homeworks (Redacted Answers)",
            "ID": "A2R_1000",
            "Description": "All the assignment sheets for Pre-AP Algebra 2",
            "Purchase": "[$7.50]"
        },
        {
            "Title": "All Homeworks (Answered)",
            "ID": "A2A_1000",
            "Description": "All the answered assignments for Pre-AP Algebra 2",
            "Purchase": "[$8]"
        },
        {
            "Title": "All DOLs",
            "ID": "A2D_1000",
            "Description": "All the DOL assignments for Pre-AP Algebra 2",
            "Purchase": "[$3]"
        }
    ]
}

def main(): 
    st.title("📒 Mainframe Shop") 
    st.link_button("Back to **Mainframe AI**", "https://mainframe.streamlit.app") 

    for category, items in INVENTORY_DATA.items(): 
        st.markdown(f"## {category}") 
        updated_items = [] 
        for item in items: 
            new_item = item.copy() 
            if "Purchase" in new_item: 
                if "Free" in new_item["Purchase"]:  # Check for "Free" specifically 
                    if "Free (click here)" in new_item["Purchase"]:
                        new_item["Purchase"] = f"[Free (click here)]({FREE_LINK})" 
                    else:
                        new_item["Purchase"] = f"[Free]({FREE_LINK})" 
                else: 
                    try: 
                        price_part, link_part = new_item["Purchase"].split("(", 1) 
                        link_part = link_part[:-1]  # Remove trailing ')' 
                        new_item["Purchase"] = f"{price_part}({PURCHASE_LINK})" 
                    except ValueError: 
                        new_item["Purchase"] = f"{new_item['Purchase']}({PURCHASE_LINK})" 

            updated_items.append(new_item) 
        df = pd.DataFrame(updated_items) 
        st.table(df.style.hide(axis="index")) 

if __name__ == "__main__": 
    main()
