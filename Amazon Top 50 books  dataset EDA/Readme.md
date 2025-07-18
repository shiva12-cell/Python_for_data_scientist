# 📚 Amazon Top 50 Bestselling Books (2009–2019) – EDA Project

This project presents a detailed **Exploratory Data Analysis (EDA)** on Amazon's Top 50 bestselling books across 11 years. The goal is to uncover patterns in book sales, identify successful features (price, rating, reviews), and derive actionable business insights using real-world data analysis techniques.

---

## 🧾 Dataset Overview

- **Source**: `bestsellers with categories.csv`
- **Years Covered**: 2009–2019
- **Total Entries**: 550 books
- **Features**:
  - `Name`: Book title
  - `Author`: Author of the book
  - `User Rating`: Rating (0–5 scale)
  - `Reviews`: Number of user reviews
  - `Price`: Listed price in USD
  - `Year`: Year the book was a bestseller
  - `Genre`: Fiction or Non-Fiction

---

## 🧠 Objectives

- Analyze which genres, authors, and books dominated the decade
- Find pricing and review patterns for top-performing books
- Engineer new features to support deeper insights
- Recommend which books should be promoted to increase revenue

---

## 🛠️ Feature Engineering

New features added to the dataset:

| Column | Description |
|--------|-------------|
| `Expensive` | Flag if price > $200 |
| `Top10_Review` | Flag for books in the top 10% of review count |
| `Price_Zscore` | Standardized Z-score for price comparison |

---

## 📊 Key Explorations & Visualizations

- 📚 **Genre Trends** – Fiction vs Non-Fiction over the years
- 🧑‍💼 **Top Authors** – Jeff Kinney, Gary Chapman, etc.
- 💵 **Price Patterns** – Effect of pricing on review count
- 🌟 **High Review & High Rating Cross-section**
- 📆 **Bestseller Year Distribution**

---

## 🔍 Business Insights

- ⭐ Books with high ratings **(≥ 4.8)** and high reviews are prime for promotion
- 💡 Books from **recent years (2015–2019)** perform better in engagement
- 📈 Certain authors dominate the charts across multiple years
- 💰 Avoid promoting overpriced books unless backed by strong brand (author)

---

## 📢 Promotion Strategy

To boost sales and customer satisfaction, focus on books that:
- Have **high ratings (≥ 4.8)**
- Are in the **top 10% of review count**
- Are **moderately priced (< $100)**
- Are from the **last 5 years**
- Belong to authors with repeated success

---

## 📁 Folder Structure

Amazon_Top50_Books_EDA/
│
├── Amazon_Top50_EDA.ipynb
├── bestsellers with categories.csv
├── README.md
└── plots/
├── genre_distribution.png
├── top_authors.png
└── price_vs_reviews.png

yaml
Copy code

---

## ✅ Skills Used

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Data Cleaning and EDA
- Feature Engineering
- Business Insight Generation
- Data Storytelling

---

## 🚀 Status

📌 **Completed** — This project is part of my Data Analyst portfolio

---

## 💼 Author

**Shiva Upadhyay**
Aspiring Data Analyst | Self-Learner |

---
