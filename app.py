import base64
import streamlit as st
from pathlib import Path

st.markdown(
    """
    <style>
    /* ------ GLOBAL COLORS ------ */
    :root {
        --black-bg: #0b0b0b;   /* deep black */
        --gold-text: #FFD700; /* warriors gold */
        --red-accent: #FF0000;
    }

    /* ------ MAIN APP BACKGROUND & TEXT ------ */
    .stApp {
        background-color: var(--black-bg);
        color: var(--gold-text);
    }

    /* ------ SIDEBAR STYLE ------ */
    [data-testid="stSidebar"] {
        background-color: var(--black-bg) !important;
        color: var(--gold-text) !important;
        border-right: 2px solid var(--red-accent);
    }

    /* Sidebar headings & text */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: var(--gold-text) !important;
    }

    /* Radio dots */
    [data-testid="stSidebar"] .stRadio>div>label>div[data-baseweb="radio"] svg {
        fill: var(--gold-text) !important;
        stroke: var(--gold-text) !important;
    }

    /* Active radio label */
    [data-testid="stSidebar"] .stRadio>div>label.st-13f1q6l {
        color: var(--gold-text) !important;
        font-weight: 600;
    }

    /* ------ GLOBAL HEADINGS ------ */
    h1, h2, h3, h4 { color: var(--gold-text); }

    /* ------ SUBHEADINGS ------ */
    .stMarkdown h2, .stMarkdown h3 { color: #FFCC00; }

    /* ------ TABS STYLING ------ */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid var(--red-accent);
        display: flex;
        gap: 1rem;
        align-items: center;
    }
    .stTabs [data-baseweb="tab"] {
        color: var(--gold-text);
        font-weight: bold;
        padding: 0.75rem 1.25rem;
        border-radius: 12px 12px 0 0;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--red-accent) !important;
        color: black !important;
        box-shadow: inset 0 -3px 0 0 var(--gold-text);
        transform: translateY(1px);
    }

    /* ------ BUTTON & BADGE STYLES ------ */
    .stButton>button {
        background-color: var(--gold-text);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: var(--red-accent);
        color: white;
    }

    a { color: #FFCC00; text-decoration: none; }
    a:hover { color: var(--red-accent); }

    /* ------ EXPANDER STYLES ------ */
    /* Force all expander elements to use gold theme */
    div[data-testid="stExpander"] {
        border: 1px solid var(--gold-text) !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }
    
    /* Expander header - more specific targeting */
    div[data-testid="stExpander"] details {
        background-color: var(--black-bg) !important;
    }
    
    div[data-testid="stExpander"] summary {
        background-color: rgba(255, 215, 0, 0.15) !important;
        color: var(--gold-text) !important;
        font-weight: bold !important;
        padding: 1rem !important;
        cursor: pointer !important;
        list-style: none !important;
        border-bottom: 1px solid var(--gold-text) !important;
    }
    
    div[data-testid="stExpander"] summary:hover {
        background-color: rgba(255, 215, 0, 0.25) !important;
    }
    
    /* Hide default arrow and add custom one */
    div[data-testid="stExpander"] summary::-webkit-details-marker {
        display: none !important;
    }
    
    div[data-testid="stExpander"] summary svg {
        fill: var(--gold-text) !important;
    }
    
    /* Expander content area */
    div[data-testid="stExpander"] div[data-testid="stExpanderContent"] {
        background-color: var(--black-bg) !important;
        padding: 0 !important;
    }
    
    /* Radio group inside expander */
    div[data-testid="stExpander"] .stRadio > label {
        color: var(--gold-text) !important;
        font-weight: 500 !important;
        padding: 0 1rem !important;
    }
    
    /* Radio options - full width cells with inline layout */
    div[data-testid="stExpander"] div[role="radiogroup"] label {
        color: var(--gold-text) !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        padding: 0.75rem 1.25rem !important;
        margin: 0 !important;
        transition: all 0.3s ease !important;
        font-weight: bold !important;
        position: relative !important;
        border-radius: 8px !important;
    }
    
    div[data-testid="stExpander"] div[role="radiogroup"] label:hover {
        background-color: rgba(255, 215, 0, 0.1) !important;
    }
    
    /* Selected radio option - matches tab style */
    div[data-testid="stExpander"] div[role="radiogroup"] label:has(input:checked) {
        background-color: var(--red-accent) !important;
        color: black !important;
        font-weight: bold !important;
        box-shadow: inset 0 -3px 0 0 var(--gold-text) !important;
        transform: translateY(1px) !important;
    }
    
    /* Radio circles styling */
    div[data-testid="stExpander"] div[data-baseweb="radio"] {
        background-color: transparent !important;
        margin-right: 0.5rem !important;
        flex-shrink: 0 !important;
        position: relative !important;
    }
    
    div[data-testid="stExpander"] div[data-baseweb="radio"] > div:first-child {
        border: 2px solid var(--gold-text) !important;
        background-color: transparent !important;
        width: 16px !important;
        height: 16px !important;
        position: relative !important;
    }
    
    /* Selected radio circle */
    div[data-testid="stExpander"] label:has(input:checked) div[data-baseweb="radio"] > div:first-child {
        background-color: black !important;
        border-color: black !important;
    }
    
    /* Inner dot for selected radio - properly positioned */
    div[data-testid="stExpander"] label:has(input:checked) div[data-baseweb="radio"] > div:first-child::after {
        content: "" !important;
        display: block !important;
        width: 6px !important;
        height: 6px !important;
        border-radius: 50% !important;
        background-color: var(--red-accent) !important;
        position: absolute !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
    }
    
    /* Hover state for unselected options */
    div[data-testid="stExpander"] div[role="radiogroup"] label:not(:has(input:checked)):hover {
        background-color: rgba(255, 215, 0, 0.15) !important;
        color: #FFCC00 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Page config
st.set_page_config(page_title="Aditya Jayanth Vadali", layout="wide")

# ---- SIDEBAR NAVIGATION ----
tabs = st.tabs(["🏠 Home", "📁 Projects", "📫 Contact"])

# ---- HOME TAB ----
with tabs[0]:
    col1, col2 = st.columns([1.2, 4])  # Make image column slightly wider

    with col1:
        st.image("assets/profile.jpg", width=300)  # Increased image width

    with col2:
        st.title("Aditya Jayanth Vadali")
        st.subheader("Data Scientist | ML Engineer | Python Developer")
        st.markdown("""
Hello! I'm Aditya Jayanth Vadali, a passionate and results-driven Data Scientist with a Master's in Data Science from Rochester Institute of Technology. With a strong foundation in machine learning, data engineering, and analytics, I thrive on transforming complex data into actionable insights and innovative solutions.

My experience at Fidelity Investments as a Technology Intern focused on developing robust data pipelines and deploying impactful machine learning models, significantly improving forecasting accuracy and streamlining reporting efforts. I'm adept at leveraging a diverse tech stack, including Python, AWS, Streamlit, Snowflake, and various ML frameworks, to build scalable and efficient data-driven applications.

I'm particularly proud of my work on A.L.I.N.A. (All In Nutritional Assistant) , an AI-powered nutrition tracker that I co-created, demonstrating my ability to lead and develop full-stack solutions from conception to deployment. With a keen eye for detail and a commitment to continuous learning, I'm excited to contribute my skills to challenging data science and machine learning initiatives.
        """, unsafe_allow_html=True)


# ---- PROJECTS TAB ----
with tabs[1]:  # 📁 Projects
    
    # ── 2-column layout (expander on the left) ──────────────────────────
    left, right = st.columns([1.3, 3.7])

    # ---------------------------------------
    # LEFT COLUMN  ▸  Collapsible Expander
    # ---------------------------------------
    with left:
        with st.expander("Project", expanded=True):
            project = st.radio(
                label="Select Project",
                options=[
                    "Candy Store ETL",
                    "Healthcare Normalization Pipeline",
                    "Credit Card Transaction System - Lambda Architecture",
                    "Fake Job Posting Detection - NLP Pipeline"
                ],
                label_visibility="collapsed"  # hide small caption
            )

    # ---------------------------------------
    # RIGHT COLUMN ▸  Main Project Content
    # ---------------------------------------
    with right:
        if project == "Candy Store ETL":
            st.header("Candy Store ETL")
            st.markdown("""


#### Project Introduction

The Candy Store Analytics System is an automated data processing system developed for Tiger's Candy, a rapidly growing candy store. The primary goal of this project is to implement a batch processing logic for daily online order transactions, which includes validating transaction details, verifying inventory levels, and ensuring successful order shipments. Additionally, the system forecasts future sales and profits using historical data.

#### Dataset Description

The project utilizes a dataset spanning from February 1st to 10th, 2024, which includes customer information, product details, and raw order transactions. The customer dataset contains unique identifiers, names, contact information, and addresses for each customer. The products dataset provides details about the candies, such as product ID, name, category, subcategory, sales price, cost to make, and current stock levels. Raw order transactions are provided as JSON files, detailing transaction IDs, customer IDs, timestamps, and lists of purchased items with product IDs, names, and quantities.

#### Data Loading

Initial data loading involves migrating CSV files containing customer and product information into MySQL, and JSON transaction files into MongoDB. The system then loads this data from both MySQL and MongoDB into a Spark session for processing, displaying previews and dimensions of the loaded dataframes.

#### Batch Processing ETL

The system implements daily batch processing of order transactions, meaning each day's transactions are imported, processed, and validated, with results combined after a 10-day period. This process transforms raw transaction data into structured orders and order line items tables, while also managing inventory by verifying stock levels and canceling orders for out-of-stock items.

#### Sales Forecasting

The system includes capabilities for sales and profit forecasting. It utilizes the Prophet forecasting algorithm through a custom implementation, providing accuracy metrics like Mean Absolute Error (MAE) and Mean Squared Error (MSE). The processed daily sales and profit numbers are fed into this model to predict future sales and profits, and these forecasting results are saved into a dedicated table.

#### Apache Airflow DAG

An Apache Airflow Directed Acyclic Graph (DAG) is implemented to orchestrate the entire data processing pipeline. This DAG automates the workflow, including setting up the environment, processing daily transactions, generating daily summaries, and producing sales and profit forecasts, following a similar structure to the `main.py` script.

#### Technical Implementation Notes

The system primarily uses PySpark for distributed data processing, connecting to both MongoDB for transaction data and MySQL for product and customer information. The forecasting component is built around the `ProphetForecaster` class, which offers a streamlined interface to Facebook's Prophet library for time series analysis.

#### Error Handling

Robust error handling is a key feature of the system. It is designed to gracefully manage missing data, provide detailed error reports, validate transactions thoroughly, and perform data quality checks to ensure data integrity throughout the pipeline.

#### Best Practices

The project demonstrates adherence to several software development best practices, including the use of strong typing with type hints for code clarity, comprehensive error handling mechanisms, clear separation of concerns for modularity, and detailed logging and reporting for better monitoring and debugging.
            """)

        elif project == "Healthcare Normalization Pipeline":
            st.header("Healthcare Normalization Pipeline")
            st.markdown("""
            - ⚙️ PySpark batch pipeline for flat EHR records  
            - 🏗️ Airflow-orchestrated stages into Snowflake schema  
            - ✅ 10 dimension tables + 1 fact table
            """)

        elif project == "Credit Card Transaction System - Lambda Architecture":
            st.header("Credit Card Transaction System – Lambda Architecture")
            st.markdown("""
            - 💳 Kafka stream for real-time validation  
            - 🗂️ Batch reconciliation layer in Spark  
            - 📊 MySQL for stateful customer & card data
            """)

        else:  # Fake Job Posting Detection – NLP Pipeline
            st.header("Fake Job Posting Detection – NLP Pipeline")
            st.markdown("""
            - 📝 Collected 17 k job ads; cleaned & vectorized text  
            - 🤖 BERT fine-tuned for fake/real classification (94 % F1)  
            - 📦 Packaged as REST-style micro-service
            """)





with tabs[2]: 
            c1, c2 = st.columns(2)
            with c1 :
                st.markdown(
                    """
                    <a href="https://brotracker.mine.bz" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: black;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            🥗 A.L.I.N.A.
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
                


                st.markdown(
                    """
                    <a href="https://www.linkedin.com/in/adityajayanthvadali" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: black;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            💼 LinkedIn
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            
            with c2: 
                    with open("assets/Aditya_Jayanth_Vadali_Resume.pdf", "rb") as f:
                        st.download_button(
                            label="📄 Download My Resume",
                            data=f,
                            file_name="Aditya_Jayanth_Vadali_Resume.pdf",
                            mime="application/pdf"
                        )

                    with open("assets/Aditya_Jayanth_Vadali_Resume.pdf", "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                    pdf_display = f"""
                    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf">
                    </iframe>
                    """

                    st.markdown(pdf_display, unsafe_allow_html=True)