import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('D:\Onlinepython\customer.csv')
print(data.head())
print("Missing values per column:\n", data.isnull().sum())
print("\nData types:\n", data.dtypes)
duplicates = data.duplicated().sum()
print(f'\nDuplicate rows: {duplicates}')
data = data.drop_duplicates()
print("\nSummary statistics:\n", data.describe())
categorical_features = ['State', 'Area code', 'International plan', 'Voice mail plan', 'Churn']
for feature in categorical_features:
    plt.figure(figsize=(10, 5))
    sns.countplot(x=feature, data=data)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=90)  # Rotate x-axis labels by 90 degrees
    plt.show()
for feature in categorical_features:
    if feature != 'Churn':
        plt.figure(figsize=(10, 5))
        ax = sns.countplot(x=feature, hue='Churn', data=data, palette='Set1')
        plt.title(f'{feature} by Churn')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.xticks(rotation=90)
        plt.legend(title='Churn')
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 3),
                        textcoords='offset points')
        plt.show()
for feature in categorical_features:
    if feature != 'Churn':
        plt.figure(figsize=(10, 5))
        ax = sns.countplot(x=feature, hue='Churn', data=data, palette='Set1')
        plt.title(f'{feature} by Churn')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.xticks(rotation=90)
        plt.legend(title='Churn')
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 3),
                        textcoords='offset points')
        plt.show()