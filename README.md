# 🌸 Iris Flower Classification: A Comparative Study

This project involves building a machine learning pipeline to classify Iris flower species based on their physical measurements. The primary goal was to compare multiple classification algorithms to determine which provides the highest accuracy and the most reliable confusion matrix.

---

## 🛠️ Project Workflow

### 1. Data Preparation
* **Loading & Exploration:** Initialized the dataset and inspected data properties (shape, types, and descriptive statistics).
* **Cleaning:** Checked for missing values and handled inconsistencies to ensure data integrity.
* **Encoding:** Converted categorical species strings into numerical values:
    * `Iris-setosa` → **0**
    * `Iris-versicolor` → **1**
    * `Iris-virginica` → **2**

### 2. Modeling & Evaluation
The data was split into training and testing sets to evaluate the performance of five distinct algorithms:
* **Logistic Regression:** Used as the baseline linear model.
* **Random Forest Classifier:** An ensemble method using multiple decision trees.
* **Gradient Boosting Classifier:** A technique that builds trees sequentially to minimize errors.
* **K-Nearest Neighbors (KNN):** A proximity-based classifier.
* **Support Vector Machine (SVM):** A model that finds the optimal hyperplane for classification.

### 3. Performance Metrics
For each model, I extracted:
* **Accuracy Score:** To measure overall correctness.
* **Confusion Matrix:** To visualize misclassifications between specific species.

---

## 📊 Findings & Results

After training and testing all five models, the performance was compared to identify the most robust solution.

| Model | Accuracy | Key Observations |
| :--- | :--- | :--- |
| **Logistic Regression** | [100 %] | Great for linear relationships. |
| **Random Forest** | [98 %] | Highly resistant to overfitting. |
| **Gradient Boosting** | [98 %] | Strong performance on complex patterns. |
| **KNN** | [98 %] | Simple and effective for this dataset size. |
| **SVM** | [100 %] | Excellent boundary separation. |

> **Conclusion:** The best performing model were **[Logistic regression and SVM]**, achieving the highest accuracy with the least amount of confusion between species classes.

---

## Demo

The app is live at (https://digit-recognition-neural-network-hlqdf4clkvrfdgkwhj9ls4.streamlit.app/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/digit-recognition-nn.git
   cd digit-recognition-nn
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web App
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501` and upload digit images to test predictions.

## Project Structure

```
├── app.py                 # Streamlit web application
├── IRIS data cleaning and model training.ipynb  # Jupyter notebook for model training
├── logreg_model.pkl        # Trained logistic regression model
├── requirements.txt       # Python dependencies
└── README.md             # This file
└── iris.csv             # The CSV file
```

## 🚀 Technologies Used
* **Python 3.10**
* **Pandas & NumPy** (Data Manipulation)
* **Scikit-Learn** (Machine Learning)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- sklearn digits dataset for training data
- Streamlit for the web framework
- Open source community for inspiration</content>
<parameter name="filePath">c:\Users\hassa\Iris Flower Classification\README.md



