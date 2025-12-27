# 🧭 Weekend Getaway Ranker  

---

## 📌 Project Overview
The **Weekend Getaway Ranker** is a Python-based recommendation engine that suggests the **top weekend travel destinations in India** based on a given **source city**.

The system ranks destinations using a combination of:
- **Proximity (distance proxy based on city/state/zone)**
- **Google review ratings**
- **Popularity (number of Google reviews)**

This project was developed as part of a **Data Engineering assignment round** and focuses on data preprocessing, feature engineering, and ranking logic using **Python and Pandas**.

---

## 🎯 Problem Statement
Build a recommendation engine for local travel based on the **Travel Dataset (India’s Must-See Places)**.

### Requirements:
- Take a **Source City** as input
- Rank the **top weekend destinations**
- Use **distance, rating, and popularity** as ranking factors
- Submit a **GitHub repository** containing:
  - Python script
  - `requirements.txt`
  - Sample output for at least **three different cities**

---

## 📂 Dataset Description
The dataset contains curated information about popular tourist places across India.  
Key columns used in this project include:

- `Zone`
- `State`
- `City`
- `Name`
- `time needed to visit in hrs`
- `Google review rating`
- `Number of google review in lakhs`
- `Best Time to visit`

⚠️ **Note:**  
The dataset does **not** contain latitude/longitude information. Therefore, geographical distance is approximated using a location hierarchy.

---

## 📌 Dataset Source
The dataset used in this project was provided as part of the assignment instructions and is publicly available on Kaggle:

**Travel Dataset – Guide to India’s Must-See Places**  
https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places

---

## 🧠 Key Design Decisions

### 🔹 Distance Approximation (Proxy)
Since exact geographical distance is unavailable, proximity is estimated using a hierarchical approach:

1. **Same City** – Local weekend places (highest priority)
2. **Same State**
3. **Same Zone**
4. **Adjacent Zone**
5. **Far Zones** (lowest priority)

This approach ensures **geographically realistic weekend recommendations** without relying on external APIs.

---

## 📊 Ranking Logic

Each destination is assigned a **final score** using the following weighted formula:

Final Score =
0.45 × Distance Score +
0.35 × Normalized Rating +
0.20 × Normalized Popularity

### Feature Details:
- **Distance Score:** Derived from city/state/zone proximity
- **Rating:** Google review rating (normalized)
- **Popularity:** Number of Google reviews in lakhs (normalized)

Additional filters are applied to improve weekend suitability:
- Time needed to visit ≤ 5 hours
- Google review rating ≥ 4.0

---

## 🛠️ Technologies Used
- Python 3.11.1
- Pandas

---

## 📁 Project Structure

```text

Weekend-Gateway-Ranker/
│
├── data/
│   └── Top_Indian_Places_to_Visit.csv
│
├── src/
│   └── getaway_ranker.py
│
├── requirements.txt
├── sample_output.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```text
pip install -r requirements.txt

```
### 2️⃣ Run the script

From the project root directory:
```text
python src/getaway_ranker.py

```

### 3️⃣ Provide input

- Enter a source city (e.g., Kolkata)
- OR press Enter to automatically run sample cities

## 📄 Sample Output

Sample outputs for three different cities (Kolkata, Delhi, Mumbai) are provided in:
```text
sample_output.txt

```

The sample output includes:

- Destination name
- City
- Rating
- Popularity
- Best time to visit
- Final ranking score
- The output is formatted in a human-readable way for easy evaluation.


---

## ⚠️ Assumptions & Limitations

- Recommendations are limited to destinations available in the dataset.
- Distance is approximated using city/state/zone hierarchy due to lack of coordinates.
- The model is designed for weekend trips, not long-duration travel.
- No real-time or external data sources are used.

---


## ✅ Assignment Requirements Fulfilled

- Input-based ranking system
- Uses Python and Pandas
- Distance, rating, and popularity-based ranking
- Clean data preprocessing and feature engineering
- Sample output for multiple cities
- GitHub-ready project structure


--- 


## 🚀 Future Improvements

Add latitude/longitude for accurate distance calculation
Support budget-based filtering
Export recommendations to CSV
Build a CLI or web interface  


---


## 👨‍💻 Author

**Subham Maity**


🔗 **GitHub**: https://github.com/GitSubham-00

🔗 **LinkedIn**: https://linkedin.com/in/subhammaity

If you found this project useful, feel free to star the repository!
