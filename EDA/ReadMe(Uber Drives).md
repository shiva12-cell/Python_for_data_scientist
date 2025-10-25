# Uber Rides EDA

## 1. Overview

This exploratory data analysis (EDA) focuses on a dataset of Uber rides to uncover usage patterns, peak hours, and user preferences. The dataset contains **1,156 records** with **7 key columns**.  

### Dataset Columns

- **START_DATE:** Timestamp when the ride started.  
- **END_DATE:** Timestamp when the ride ended.  
- **CATEGORY:** Type of ride (e.g., UberX, UberXL).  
- **PURPOSE:** Reason for the ride (e.g., Business, Leisure).  
- **START:** Pickup location.  
- **STOP:** Dropoff location.  
- **DURATION:** Ride duration in minutes.  

---

## 2. Data Preprocessing

Key steps taken to prepare the data for analysis:

1. **Handling Missing Values:**  
   Missing entries in the `PURPOSE` column were filled with `"Not Specified"`.

2. **Datetime Conversion:**  
   Converted `START_DATE` and `END_DATE` to datetime objects for accurate time-based analysis.

3. **Feature Engineering:**  
   - Extracted **hour** from `START_DATE` to categorize rides into **Morning, Afternoon, Evening, and Night** time slots.  
   - Created a **day-night** category based on ride start times.  

---

## 3. Exploratory Analysis

### a. Ride Count by Category  
Analyzing the distribution of rides across categories helps understand user preferences and demand patterns.

### b. Ride Count by Purpose  
Examining ride purposes reveals why users choose Uber, providing insights for targeted marketing and service optimization.

### c. Ride Count by Time Slot  
Rides were analyzed across different times of the day to identify peak hours, which can inform resource allocation and surge pricing.

### d. Category vs. Purpose  
Cross-analysis of ride categories and purposes highlights which services are preferred for specific activities.  

---

## 4. Key Insights

- **Peak Ride Times:** Most rides occur in the **Afternoon (10 AM - 5 PM)**, indicating peak demand during these hours.  
- **Purpose Distribution:** **Business-related rides** dominate, suggesting a strong professional user base.  
- **Category Preferences:** **UberX** is the most frequently used category, showing its popularity among riders.  

---
