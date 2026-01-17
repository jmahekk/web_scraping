# web_scraping

# Clone the repo
git clone https://github.com/username/web_scraping.git
cd tweets-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Usage Example
python main.py

# Technical Approach

## 1. Dataset

- Source: Kaggle (CSV file with tweet data)
- Fields: Date, Tweet, Stock Name, Company Name
- 
## 2. Data Processing

- **Cleaner Module**: Lowercase text, remove special characters, emojis, URLs.
- **Deduplicator Module**: Remove duplicate tweets based on text content.
- **Storage**: Save processed data as Parquet for efficient I/O.

## 3. Analysis Workflow

- Load processed data from Parquet.
- Compute tweet counts per stock or company.
- Generate visualizations like bar charts, line charts, or trends over time.
- Sample output saved in `data/analysis/sample_analysis.png`.

## 4. Challenges & Solutions

- Handling missing or malformed data: Used `dropna()` and basic regex cleaning.
- Large CSV files: Parquet format used to optimize storage and speed.
