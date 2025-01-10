

# 🚗 Used German Cars Market Analysis & Price Prediction



Welcome to the **Used German Cars Market Analysis** project! 🚘  
This repository is a deep dive into the German used car market to uncover insights, clean messy data, and build a machine learning pipeline to predict car prices accurately. If you’re a data enthusiast or machine learning fan, you’ll love this project!

---

## 📌 Project Highlights

✨ **Data Collection:**  
- The core dataset was sourced from [Kaggle]([https://www.kaggle.com/](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices)). Missing values were then filled using **web scraping** from [Auto-Data.net](https://www.auto-data.net/en/) to enhance data quality.

✨ **Exploratory Data Analysis (EDA):**  
- Created stunning **univariate and multivariate visualizations** to uncover trends and patterns in the used car market.  

✨ **Feature Engineering:**  
- Added a new feature, `brand_category`, categorizing car brands into:
  - `Unknown`
  - `Cheap Brands`
  - `Cheap Midrange Brands`
  - `Midrange Luxury Brands`  
- Applied **Ordinal Encoding** to ensure the correct order was maintained.  

✨ **Prediction Pipeline:**  
- Built and evaluated a machine learning pipeline.  
- Best model: **Voting Regressor** combining:
  - `HistGradientBoostingRegressor`  
  - `RandomForestRegressor`  
- Achieved higher performance after hyperparameter tuning and cross-validation.

✨ **Key Result:**  
- Adding the `brand_category` feature improved the R² score even further, proving the power of thoughtful feature engineering.

---

## 🎯 Goals
1. Understand the **trends and insights** in the used German car market.
2. Develop a reliable machine learning model to predict car prices with high accuracy.
3. Experiment with **data augmentation** and advanced **feature engineering** to improve model performance.

---

## 🗂️ Project Structure

| **Folder**             | **Description**                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------|
| `data/`                | Contains raw and processed datasets, including the scraped data for missing values.             |
| `notebooks/`           | Jupyter Notebooks showcasing data exploration, visualizations, and experiments.                 |
| `models/`              | Saved models and serialized objects for easy reuse.                                             |
| `scripts/`             | Python scripts for scraping, preprocessing, training, and evaluating the model.                 |
| `visualizations/`      | Plots and charts generated during EDA for better understanding of the data.                     |
| `README.md`            | You’re reading it! A full overview of the project.                                              |

---

## 🛠️ Tools & Technologies
- **Programming Language:** Python 🐍  
- **Libraries:**  
  - Pandas, NumPy for data manipulation.  
  - Matplotlib, Seaborn for visualizations.  
  - Scikit-learn for building machine learning models.  
  - BeautifulSoup for web scraping.  
  - Jupyter Notebook for experimentation and prototyping.  

---

## 📈 Workflow

### 1. Data Collection  
- Started with the Kaggle dataset and added additional data using web scraping to handle missing values.  

### 2. Data Cleaning & Feature Engineering  
- Performed initial cleaning: filling missing values, fixing inconsistencies, and converting data types.  
- Introduced a new feature, `brand_category`, to enhance the model's understanding of car brand pricing dynamics.  

### 3. Exploratory Data Analysis  
- Uncovered hidden patterns using insightful plots:  
  - **Univariate analysis** for individual feature trends.  
  - **Multivariate analysis** to study relationships (e.g., price vs. mileage).  

### 4. Machine Learning Pipeline  
- Tried various models and found that the **Voting Regressor** (combining `HistGradientBoostingRegressor` and `RandomForestRegressor`) worked best.  
- Used **cross-validation** to ensure robustness.  

### 5. Model Improvement  
- Ordinal encoding of `brand_category` improved the R² score further, highlighting the importance of custom feature engineering.  

---

## 🔥 Key Visualizations
Here’s a sneak peek of the visualizations created:  
- **Price Distribution:** Histogram showing how car prices vary across the dataset.  
- **Mileage vs. Price:** Scatterplot revealing how mileage impacts price.  
- **Brand Popularity:** Bar chart comparing the number of cars for each brand.  

📊 All visualizations can be found in the `visualizations/` folder.

---

## 🚀 How to Run the Project

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/username/used-german-cars-analysis.git
   cd used-german-cars-analysis
   ```

2. **Install Dependencies**  
   Make sure you have Python 3.8+ installed. Then run:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Notebooks**  
   Explore the project using Jupyter Notebook:  
   ```bash
   jupyter notebook
   ```

4. **Train the Model**  
   Run the training script:  
   ```bash
   python scripts/train_model.py
   ```

---

## 🤝 Contributing
Contributions are welcome! If you have ideas to improve the project or find any bugs, feel free to submit an issue or a pull request.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🧑‍💻 Author
👤 **Abdelrahman Elseht**  
- AI Engineer passionate about data and machine learning.  
- Connect with me on [LinkedIn](https://www.linkedin.com/in/abdelrahman-e-2bbb882a2/) or check out my other projects!  

---

Enjoy exploring the used German cars market! 🚗💨

---
