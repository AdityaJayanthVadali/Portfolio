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

    /* ------ BACKTICK/CODE STYLING ------ */
    /* Style inline code blocks (backticks) */
    code {
        background-color: var(--red-accent) !important;
        color: var(--gold-text) !important;
        padding: 2px 6px !important;
        border-radius: 3px !important;
        font-family: monospace !important;
        font-size: 0.9em !important;
    }
    
    /* Style code blocks in markdown */
    .stMarkdown code {
        background-color: var(--red-accent) !important;
        color: var(--gold-text) !important;
    }
    
    /* Pre-formatted code blocks */
    pre code {
        background-color: var(--black-bg) !important;
        color: var(--gold-text) !important;
        border: 1px solid var(--red-accent) !important;
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
                    "Healthcare Normalization Pipeline - PySpark",
                    "Credit Card Transaction System - Lambda Architecture",
                    "Fake Job Posting Detection - NLP Pipeline",
                    "Stock Market Data Medallion Architecture"
                ],
                label_visibility="collapsed"  # hide small caption
            )

    # ---------------------------------------
    # RIGHT COLUMN ▸  Main Project Content
    # ---------------------------------------
    with right:
        if project == "Candy Store ETL":
            st.header("Candy Store ETL")

            st.markdown(
                    """
                    <a href="https://github.com/AdityaJayanthVadali/Candy-Store-ETL/tree/main" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: red;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            GitHub
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
                
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

        elif project == "Healthcare Normalization Pipeline - PySpark":
            st.header("Healthcare Normalization Pipeline - PySpark")

            st.markdown(
                    """
                    <a href="https://github.com/AdityaJayanthVadali/Healthcare-Normalization-PySpark/tree/main" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: red;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            GitHub
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("""

            ### Project Overview
            This project focuses on developing a data processing system for healthcare datasets. Its primary goal is to normalize legacy, flat-structured healthcare data into a dimensional data model, which includes **10 dimension tables** and **1 fact table**. The system leverages Apache Spark for scalable data processing to manage patient records, visit information, diagnoses, treatments, and billing details.

            ### Dataset Information
            The system is designed to process healthcare patient data from either MySQL or CSV sources. The dataset encompasses comprehensive healthcare records, including:
            - Patient demographics
            - Contact information
            - Visit specifics
            - Insurance and billing details
            - Primary and secondary diagnoses
            - Treatments
            - Prescriptions
            - Lab orders

            ### Data Model
            The normalized data model is structured as a **snowflake schema**, optimizing it for efficient querying and data management. It comprises ten dimension tables:

            - `dim_patient` - patient demographics
            - `dim_insurance` - insurance plan details
            - `dim_billing` - billing and payment information
            - `dim_provider` - healthcare provider details
            - `dim_location` - clinic and room information
            - `dim_primary_diagnosis` - primary diagnosis codes
            - `dim_secondary_diagnosis` - secondary diagnosis codes
            - `dim_treatment` - treatment details
            - `dim_prescription` - prescription details
            - `dim_lab_order` - lab test information

            A central `fact_visit` table contains visit records and links to all these dimension tables.

            ### Key Functionalities and Processes
            The system's core functions include:
            1. **Loading healthcare data** from CSV or MySQL into Spark DataFrames
            2. **Normalizing data** into the predefined dimensional model
            3. **Saving all tables** as individual CSV files after normalization
            4. **Performing data integrity checks**:
            - Verifying uniqueness of primary keys
            - Ensuring referential integrity between fact and dimension tables
            - Reporting any detected data quality issues

            The `data_processor.py` file contains the logic for creating and populating these tables, while `main.py` orchestrates the overall process.

            ### Technical Requirements
            To run this application, the following are required:

            **Python packages:**
            - `pyspark==3.4.0`
            - `python-dotenv==1.0.0`
            - `mysql-connector-python==9.2.0`

            **Additional requirements:**
            - Java Development Kit (JDK 8 or higher)
            - MySQL Connector JAR file for Spark-MySQL interaction

            The `load_sql.py` script provides functionality for loading CSV data directly into a MySQL table using Pandas and SQLAlchemy.

            ### Tableau Dashboard Analysis

            The Tableau dashboard provides a comprehensive visualization of the healthcare data after it has been transformed into a dimensional model. This dashboard was designed with the perspective of a **financial/insurance audit team** in mind, aiming to provide at-a-glance business intelligence related to demographics and insurance for informed decision-making.
            
            ### Dashboard Components

            - **Location/Visit Analysis**: This component features a horizontal bar chart that illustrates the distribution of visits across different clinic locations. It segments each bar by visit type (e.g., Emergency, Routine, Follow-up), allowing for a quick comparison of the most commonly utilized services at each facility.
            """)
            st.image("projects/healthcare-pyspark/LocationVisit.png")   
            st.image("projects/healthcare-pyspark/visittype_legend.png")

            st.markdown("""- **Gender/Age Group Distribution**: This visualization is a stacked bar chart that breaks down patients by gender and age group. It clearly delineates between adult and senior populations, helping to identify demographic patterns in healthcare utilization.""")
            st.image("projects/healthcare-pyspark/genderagegroup.png", width = 800)
            st.image("projects/healthcare-pyspark/age_legend.png")
            st.markdown(""" - **Insurance Coverage**: A treemap visualization is used to present the distribution of insurance coverage types among the patient population. The size of each rectangle on the treemap indicates the relative number of patients covered by each insurance type, making it easy to identify the most prevalent insurance plans.""")
            st.image("projects/healthcare-pyspark/insurancecoverage.png", width = 800)
            st.markdown("""- **Yearly Visits by Age Group**: This small table displays temporal trends in visits across different years, categorized by age group. This time-series view is useful for identifying changing patterns in healthcare utilization across various demographic segments over time.""")
            st.image("projects/healthcare-pyspark/visitagegroup.png", width = 800)
            st.markdown("""- **Insurance Payer Analysis**: This bar chart shows the count of patients associated with each insurance provider. It helps to identify the major insurance partners and their relative importance to the healthcare system.""")
            st.image("projects/healthcare-pyspark/insirancepayer.png", width = 800)

        elif project == "Credit Card Transaction System - Lambda Architecture":
            st.header("Credit Card Transaction System – Lambda Architecture")
            st.markdown(
                    """
                    <a href="https://github.com/AdityaJayanthVadali/Credit-Card-Lambda" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: red;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            GitHub
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("""
            ### Project Overview
            This project implements a comprehensive credit card transaction processing system using Lambda Architecture, combining real-time stream processing with batch processing capabilities. The system processes transactions from April 1-4, 2025, managing credit card validations, balance updates, and credit score calculations through a sophisticated pipeline that mimics real-world financial processing systems.

            ### Architecture & Components
            The system follows Lambda Architecture with three distinct layers: **Stream Layer** for real-time transaction validation using Apache Kafka, **Batch Layer** for end-of-day processing and reconciliation, and **Serving Layer** for data persistence in MySQL. Key components include a Kafka producer that simulates transaction generation, a consumer that validates transactions in real-time, and a batch processor that performs comprehensive daily updates.

            ### Stream Processing Pipeline
            The stream layer utilizes Kafka for real-time transaction processing. The producer (`producer.py`) reads transactions from CSV files and sends them chronologically to Kafka, simulating realistic timing with configurable speed factors. The consumer (`consumer.py`) validates each transaction against three rules: transaction amount must be < 50% of credit limit, merchant location must be within acceptable distance from customer address, and accumulated pending balance cannot exceed credit limit. Approved transactions are marked as "pending" while declined ones are logged with specific rejection reasons.

            ### Batch Processing Operations
            At the end of each day, the batch processor (`batch_processor.py`) performs comprehensive updates: approving all pending transactions, updating card balances, recalculating credit scores based on utilization percentages, and adjusting credit limits for customers with declining scores. The credit score adjustment follows a tiered system ranging from +15 points for excellent utilization (≤10%) to -25 points for very high utilization (>70%). Credit limits are reduced proportionally when scores drop, with reductions of 5-15% based on the severity of the score decrease.

            ### Data Management & Verification
            The system maintains data integrity through multiple mechanisms. The database handler (`database.py`) manages MySQL operations, creating and maintaining tables for customers, cards, credit card types, and transactions. All processed data is saved both as CSV files (day-specific and consolidated) and in MySQL tables. A comprehensive verification module (`verify_days.py`) ensures all daily transactions are properly processed and stored, checking for missing files and date consistency across all outputs.

            ### Technical Implementation
            The orchestration is managed by `main.py`, which coordinates the entire pipeline: initializing the database, managing producer and consumer processes for each day, triggering batch processing, and running verification. The system uses flag files for inter-process communication and includes robust error handling with detailed logging. Helper functions in `helper.py` provide business logic for location validation, credit score calculations, and credit limit adjustments. The modular design allows for easy maintenance and debugging of individual components.
            """)

        elif (project == "Fake Job Posting Detection - NLP Pipeline"):  # Fake Job Posting Detection – NLP Pipeline
            st.header("Fake Job Posting Detection – NLP Pipeline")
            st.markdown(
                    """
                    <a href="https://github.com/AdityaJayanthVadali/Fake-Job-Posting-Detection" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: red;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            GitHub
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("""
            ### Project Overview
            This project develops a machine learning model to classify job postings as either legitimate or fraudulent, addressing the growing concern of fake job advertisements. The system processes textual features from job descriptions and requirements to predict fake listings, utilizing a structured machine learning pipeline for binary text classification with a focus on achieving high F1 scores for the fraudulent class.

            ### Dataset & Features
            The project uses a job posting dataset (`job_train.csv`) containing 8,490 entries with 8 features including title, location, description, requirements, telecommuting status, company logo presence, questions availability, and the target variable (fraudulent). The `description` and `requirements` text fields were specifically selected as primary features due to their contextual relevance in identifying fraudulent postings, with missing values replaced by empty strings during preprocessing.

            ### Technical Implementation
            The solution implements a complete NLP pipeline using TF-IDF vectorization for text feature extraction. The TfidfVectorizer concatenates description and requirements into a single text string, configured with English stop words removal, L2 normalization, and n-gram range of (1,5) to capture contextual patterns. An SGDClassifier (Stochastic Gradient Descent) was chosen for its efficient runtime and competitive F1 scores, with class balancing to handle potential data imbalance.

            ### Model Optimization
            Hyperparameter tuning was performed using RandomizedSearchCV with 200 iterations, optimizing for F1 score. The parameter space included L2 regularization with alpha values ranging from 10^-6 to 10^2 and max iterations from 500 to 5000. The system utilized all available CPU cores for parallel computation, achieving an optimal balance between performance and runtime efficiency.

            ### Performance Results
            The model achieved a strong F1 score of 0.794258 for the fraudulent class (label 1), demonstrating effective identification of fake postings while maintaining balance between precision and recall. The entire training and evaluation process completed efficiently in approximately 2.26 minutes, well within the 30-minute runtime constraint. This performance metric is particularly suitable for the imbalanced dataset nature of fraud detection.

            ### Code Architecture
            The project follows a modular design with three main components: `project.py` contains the my_model class encapsulating the entire ML pipeline including preprocessing and classification; `my_evaluation.py` provides comprehensive evaluation metrics beyond basic accuracy; and `test.py` serves as the main execution script handling data loading, model training, and performance evaluation. The system is designed to work with restricted package dependencies (scikit-learn, nltk, gensim, pandas, numpy) as per course requirements.
            """)

        elif(project == "Stock Market Data Medallion Architecture"):
            st.header("Stock Market Data Medallion Architecture")
            st.markdown(
                    """
                    <a href="https://github.com/AdityaJayanthVadali/Stock-Market-Data-Medallion-Architecture/tree/main" target="_blank" style="
                        text-decoration: none;
                    ">
                        <span style="
                            background-color: #FFD700;
                            color: red;
                            font-weight: 600;
                            padding: 0.3em 0.8em;
                            border-radius: 999px;
                            font-size: 0.9em;
                            border: 1px solid #333;
                        ">
                            GitHub
                        </span>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("""
            ### Project Overview
            This project implements a Medallion Architecture for processing stock market data using PySpark. The system demonstrates a complete data engineering pipeline that ingests raw stock data from multiple sources (MySQL and MongoDB), transforms it through Bronze, Silver, and Gold layers, and produces business-ready analytics at various time granularities. The architecture showcases best practices in data lake design, processing stock transactions generated every second into structured analytical datasets.

            ### Data Sources & Architecture
            The system integrates data from two primary sources: MySQL database containing company information and market index data, and MongoDB storing transaction records in JSON format. Following the Medallion Architecture pattern, the Bronze Layer captures raw data including user transactions, market information, and stock registration details. The Silver Layer contains cleaned, enriched, and structured hourly stock data, while the Gold Layer provides aggregated summaries optimized for reporting and business intelligence applications.

            ### Technical Implementation
            The project utilizes PySpark for distributed data processing, with the `DataProcessor` class handling all transformations. The `ingest_data` method loads data from both databases using appropriate connectors (JDBC for MySQL, MongoDB Spark connector). The system implements a weighted average price calculation using the formula `(sum of shares * price) / total shares` for accurate pricing metrics. All processing strictly uses PySpark functions as per requirements, avoiding pandas or other Python packages for data manipulation.

            ### Data Processing Pipeline
            The transformation pipeline begins with hourly aggregation using `aggregate_hourly_transactions`, which groups transactions by hour and ticker, calculating total volume and weighted average prices. The Silver Layer joins this hourly data with company information and market index values. The system then progressively aggregates data into daily, monthly, and quarterly summaries using PySpark's `date_trunc` and aggregation functions, maintaining proper column naming and formatting as specified in the requirements.

            ### Output & Results
            The system generates four CSV files saved to the configured output path: hourly_stock_data.csv, daily_stock_data.csv, monthly_stock_data.csv, and quarterly_stock_data.csv. Each output follows specific formatting requirements with columns including datetime/date/month/quarter, ticker, company_name, avg_price (rounded to 2 decimals), volume, and market_index. The quarterly data uses a special format "YYYY Q#" for quarter representation. All outputs include preview displays showing the first 5 rows for verification.

            ### Configuration & Deployment
            The project uses environment variables managed through `.env` files for database credentials and paths. A `config.yaml` file defines all configuration parameters including MySQL and MongoDB connection strings, table names, and output paths. The system requires the MySQL Connector JAR for Spark JDBC connectivity and proper MongoDB Spark connector packages. The main orchestration script handles the complete workflow from session creation through all processing stages, ensuring proper resource cleanup upon completion.
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