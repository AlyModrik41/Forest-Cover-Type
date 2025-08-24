# 🌲 Forest Cover Type Classification

This project applies **Machine Learning** techniques to classify forest cover types based on cartographic variables. Using the **Forest Cover Type dataset** (UCI / Kaggle), the task is framed as a **multi-class classification problem** with 7 target classes.

---

## 📌 Project Overview

- **Goal**: Predict the type of forest cover from environmental features (elevation, slope, distances to hydrology, soil type, etc.).
- **Dataset**: Forest Cover Type dataset (7 classes, ~116k samples).
- **Techniques Used**:
  - Data Preprocessing & Feature Engineering  
  - Handling Class Imbalance with **SMOTE**  
  - Model Training with **Random Forest** (baseline & tuned)  
  - Cross-Validation for reliable evaluation  
  - Model Performance Visualization (Confusion Matrix, ROC, PR Curves)

---

## ⚙️ Methods & Features

- **Feature Engineering**  
  - Added new features:  
    - `Horizontal_Distance_Hydrology`  
    - `Vertical_Distance_Hydrology`

- **Cross Validation**  
  - Used **Stratified K-Fold** to preserve class distribution across folds.  
  - Mean CV Accuracy: **95.6%** (± 0.0007)

- **Models**  
  - Random Forest (baseline + tuned)  
  - Gradient Boosting (with SMOTE)  

---

## 📊 Results

### 1. Confusion Matrix  
Shows class-level performance and misclassifications.  
![Confusion Matrix](confusion_matrix.png)

---

### 2. ROC Curve (Random Forest)  
![ROC Curve](images/roc_curve.png)

---

### 3. Precision-Recall Curves (Random Forest)  
Demonstrates strong performance across all 7 classes.  
![Precision-Recall Curve](images/pr_curve.png)

---

## 📈 Key Metrics

- **Overall Accuracy**: ~95%  
- **Macro Avg F1**: ~0.92  
- **Class Performance**:  
  - High performance for frequent classes (1, 2, 3, 7).  
  - Slightly lower for minority classes (4, 5, 6), but improved after SMOTE.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/forest-cover-classification.git
   cd forest-cover-classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```bash
   jupyter notebook "Forest Cover Type.ipynb"
   ```

---

## 📌 Future Improvements
- Try **XGBoost / LightGBM** for efficiency.  
- Hyperparameter tuning with **Optuna / GridSearchCV**.  
- Explore **feature importance** and SHAP explanations.  

---

## 🖼️ Repository Structure
```
├── Forest Cover Type.ipynb   # Main notebook
├── images/                   # Saved plots
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   ├── pr_curve.png
└── README.md                 # Project documentation
```
