# 📌 **Pokémon ETL Data Engineering Pipeline**

This project is a complete **Data Engineering ETL pipeline** built using **Python, Pandas, SQLite, and SQL**.
It demonstrates real-world skills in **Extracting**, **Transforming**, **Loading**, **Data Modeling**, and **SQL Analytics**.

---

## 🚀 **Project Overview**

This pipeline performs the full ETL lifecycle:

1. **Extract** data from the PokéAPI (REST API)
2. **Transform** the raw data using Pandas
3. **Load** the cleaned data into a **SQLite Data Warehouse**
4. Build a **Star Schema** (Fact + Dimension tables)
5. Run several **analytical SQL queries** to generate insights

This is a perfect beginner–to–intermediate Data Engineering project suitable for portfolios and job applications.

---

## 🧱 **Project Architecture**

```
        EXTRACT     →      TRANSFORM       →       LOAD       →     ANALYTICS
 PokéAPI (REST)         Pandas Cleaning        SQLite DB          SQL Queries
                        Rename Columns        Star Schema        Insights & Stats
```

---

## 🛠️ **Tech Stack**

* **Python 3**
* **Pandas**
* **Requests**
* **SQLite**
* **SQL (Analytical Queries)**
* **Data Modeling (Star Schema)**

---

## 🗂️ **Repository Structure**

```
pokemon-etl-pipeline/
│
├── src/
│     ├── extract_pokemon.py
│     ├── transform_load.py
│     └── pokemon_queries.py
│
├── data/
│     ├── raw_pokemon.csv
│     └── pokemon.db
│
├── README.md
└── requirements.txt
```

---

## 📥 **1. Extract Step**

**File:** `src/extract_pokemon.py`

* Connects to the PokéAPI
* Extracts Pokémon data:

  * `id`, `name`, `base_experience`, `height`, `weight`
* Saves raw data to:

  ```
  data/raw_pokemon.csv
  ```

---

## 🧹 **2. Transform Step**

**File:** `src/transform_load.py`

* Cleans and renames columns
* Prepares fields for Fact and Dimension tables
* Displays transformed dataframe

---

## 🗃️ **3. Load Step (SQLite Data Warehouse)**

**File:** `src/transform_load.py`
Creates Star Schema tables:

### ⭐ **Dimension Table**

```
dim_pokemon
(pokemon_id, pokemon_name)
```

### ⭐ **Fact Table**

```
fact_pokemon_stats
(id, pokemon_id, base_experience, height, weight)
```

Writes both tables into:

```
data/pokemon.db
```

---

## ⭐ **Star Schema Diagram**

```
              dim_pokemon
            (pokemon_id, pokemon_name)
                    |
                    |
              fact_pokemon_stats
    (pokemon_id, base_experience, height, weight)
```

---

## 📊 **4. SQL Analytics**

**File:** `src/pokemon_queries.py`

Queries included:

* Top 10 Pokémon by base experience
* Average height & weight
* Count of rows in Fact & Dimension tables

Example output:

```
pokemon_id  pokemon_name  base_experience
----------- ------------- ----------------
6           charizard     240
9           blastoise     239
3           venusaur      236
...
```

---

## ▶️ **How to Run the Project**

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Extract raw data

```
python src/extract_pokemon.py
```

### 3. Transform + Load to SQLite

```
python src/transform_load.py
```

### 4. Run SQL analysis

```
python src/pokemon_queries.py
```

---

## 💡 **Why This Project Is Valuable**

This project demonstrates essential **Data Engineering skills**:

✔ API ingestion
✔ Data cleaning & transformation
✔ Database design
✔ Star Schema modeling
✔ SQL analytics
✔ Python scripting
✔ Understanding ETL pipelines end-to-end

Ideal for roles such as:

* **Data Engineer**
* **Data Analyst**
* **Business Intelligence Engineer**
* **ETL Developer**

---

## 🔮 **Future Improvements**

* Orchestrate pipeline with **Apache Airflow**
* Store raw data in **AWS S3**
* Load clean data into **BigQuery / Redshift**
* Add a BI dashboard (Power BI / Tableau)
* Automate extract step on a schedule

---

## 👤 **Author**

Asem Ahmed
Data Engineering & Data Analytics Enthusiast

