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
<img width="737" height="626" alt="download" src="https://github.com/user-attachments/assets/019117bc-8899-4e13-adc5-698b75cb8ab8" />


---

### 2. ROC Curve (Random Forest)  
<img width="1045" height="1222" alt="download" src="https://github.com/user-attachments/assets/c85725ca-2783-4140-988f-8d290514b9cb" />


---

### 3. Precision-Recall Curves (Random Forest)  
Demonstrates strong performance across all 7 classes.  
<img width="692" height="549" alt="download" src="https://github.com/user-attachments/assets/178d8371-ff5d-4f9b-b253-ffc163a2d02e" />


### 4. Feature Importances (Random Forest)
Demonstrates how important features are.
<img width="1045" height="1222" alt="download" src="https://github.com/user-attachments/assets/40b50b3f-176b-4efe-9420-3a0a5aef0bfe" />


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
