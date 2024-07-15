# Salary Prediction of Data Professions

## Introduction

This repository contains a machine learning model for predicting salary/CTC (Cost to Company) of Data Professions based on various features. The dataset includes information about 
1. `FIRST NAME`: First name
2. `LAST NAME`: Last name
3. `SEX`: Gender
4. `DOJ`: Date of joining the company
5. `CURRENT DATE`: Current date of data
6. `DESIGNATION`: Job role/designation
7. `AGE`: Age
8. `SALARY`: Target variable, the salary of the data professional
9.`UNIT`: Business unit or department
10. `LEAVES USED`: Number of leaves used
11. `LEAVES REMAINING`: Number of leaves remaining
12. `RATINGS`: Ratings or performance ratings
13. `PAST EXP`: Past work experience
The project includes data preprocessing, exploratory data analysis, and training of multiple machine learning models to identify the best performing model.

##  Problem Statement:
Create a machine learning model which will help the company in determining the salary of Data Professions using the given data.

## Features

- **Increased Accuracy**: AI/ML models extract complex patterns and trends not apparent with traditional methods, leading to more accurate predictions.
- **Timely Predicting**: AI/ML models process large datasets quickly, enabling timely Salary Prediction for the newly hired employees.
- **Scalability**: The models can handle large datasets, making them scalable for different regions and time periods.
- **Cost-Effective**: The models require minimal physical infrastructure and can be implemented using cloud-based services.



## Dataset
You are given employee data (here)as well as various other features that can be responsible for determining the employee's salary, such as :
1. `FIRST NAME`: First name
2. `LAST NAME`: Last name
3. `SEX`: Gender
4. `DOJ`: Date of joining the company
5. `CURRENT DATE`: Current date of data
6. `DESIGNATION`: Job role/designation
7. `AGE`: Age
8. `SALARY`: Target variable, the salary of the data professional
9.`UNIT`: Business unit or department
10. `LEAVES USED`: Number of leaves used
11. `LEAVES REMAINING`: Number of leaves remaining
12. `RATINGS`: Ratings or performance ratings
13. `PAST EXP`: Past work experience

## Model Creation

1. **Data Cleaning and Preprocessing**:
   - Handle missing values using random sample imputation.
   - Visualize data for outliers and distributions.
   - Encode target labels and normalize data.
   - Plot correlation heatmap.
   - Remove outliers and analyze data for the best fit line.

2. **Data Splitting**:
   - Split data into training and testing sets using `sklearn`'s `train_test_split`.

3. **Model Training**:
   - Select Random Forest Regresssor for its high R-Squared Value (0.6594).
   - Evaluate model using R-Squared Error,Mean Squared Error.

4. **Model Saving and Deployment**:
   - Save the model using `pickel`.
   - Deploy the model using Flask on Render.


## Deployment

The model is deployed using Flask on Render.
## Usage

To use this project:

1. **Install dependencies:**:
   ```sh
   pip install -r requirements.txt

2. **Run the Flask app**:
   ```sh
   python app.py

3. **Access the web app**:
   ```sh
   Open your web browser and go to http://localhost:5000


## Screenshots

### Index Page
![SalaryOutput (2)](https://github.com/user-attachments/assets/ab4e1878-d600-4107-84a7-a546265141ae)


![SalaryOutput0 (2)](https://github.com/user-attachments/assets/be2b73b9-db09-4ac7-b0dd-9a5f75fa854a)



### Result Page
![SalaryOutput1 (2)](https://github.com/user-attachments/assets/f7a47a9f-ee60-44ce-a79e-cf028b4a7192)



