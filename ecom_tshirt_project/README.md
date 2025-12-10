# E-Commerce T-Shirt Analytics (SQLite + Python + Streamlit)
This is a complete, runnable project that builds a small analytics pipeline for a T-Shirt e-commerce business.
It uses **SQLite** for the database so you can run it locally without installing a database server.
The project includes:
- `schema.sql` : SQL schema for tables
- `etl.py` : ETL script to load sample CSVs into SQLite and run sample analytics queries
- `app_streamlit.py` : Streamlit app to view basic dashboards
- `requirements.txt` : Python dependencies
- Sample CSVs in `data/` folder

## Quick start
1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # mac/linux
   venv\Scripts\activate     # windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run ETL to create the SQLite DB and load sample data:
   ```bash
   python etl.py
   ```
   This creates `tshirt.db` in the project folder.
4. Run Streamlit dashboard:
   ```bash
   streamlit run app_streamlit.py
   ```
5. Explore & modify sample CSVs in `data/` to test different scenarios.

## Files
- `etl.py` : loads CSVs from `data/` into `tshirt.db`, prints sample analytics
- `app_streamlit.py` : streamlit dashboard using the sqlite DB
- `data/` : sample CSV files

## Notes
- This is a minimal, interview-ready project. You can swap SQLite for MySQL/Postgres by changing SQLAlchemy connection strings.
- If you want, I can extend this with Docker, CI, or a full React frontend.
