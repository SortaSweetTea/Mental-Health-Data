# Exploratory Data Analysis script for mental health and gaming survey
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../data/cleaned/mental_health_survey_cleaned.csv')
print(df.head())