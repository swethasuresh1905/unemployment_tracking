import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load saved model
model = joblib.load('models/random_forest_unemployment.pkl')

# Load merged dataset for visualizations
merged_df = pd.read_csv('data/cleaned/merged_unemployment_data.csv')

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Input Features")
estimated_employed = st.sidebar.number_input("Estimated Employed", min_value=0, value=1000000)
estimated_labour_participation_rate = st.sidebar.number_input("Labour Participation Rate (%)", min_value=0.0, value=40.0)
region = st.sidebar.selectbox("Region", merged_df['region'].unique())
area = st.sidebar.selectbox("Area", merged_df['area'].unique())

# Prepare input dataframe
input_df = pd.DataFrame({
    'estimated_employed':[estimated_employed],
    'estimated_labour_participation_rate_percent':[estimated_labour_participation_rate],
    'region':[region],
    'area':[area]
})

# One-hot encode to match training
input_df_encoded = pd.get_dummies(input_df)
for col in model.feature_names_in_:
    if col not in input_df_encoded.columns:
        input_df_encoded[col] = 0
input_df_encoded = input_df_encoded[model.feature_names_in_]

# Predict
prediction = model.predict(input_df_encoded)[0]
st.subheader("Predicted Unemployment Rate (%)")
st.write(round(prediction, 2))

# -----------------------------
# Visualizations
# -----------------------------
st.subheader("Average Unemployment Rate by Region")
avg_region = merged_df.groupby('region')['estimated_unemployment_rate_percent'].mean().sort_values(ascending=False)
fig1, ax1 = plt.subplots(figsize=(10,5))
sns.barplot(x=avg_region.index, y=avg_region.values, palette='viridis', ax=ax1)
ax1.set_ylabel("Unemployment Rate (%)")
ax1.set_xlabel("Region")
plt.xticks(rotation=45)
st.pyplot(fig1)

st.subheader("Unemployment Rate Over Time for Selected Region")
region_data = merged_df[merged_df['region']==region].sort_values('date')
fig2, ax2 = plt.subplots(figsize=(12,5))
sns.lineplot(x='date', y='estimated_unemployment_rate_percent', data=region_data, marker='o', ax=ax2)
ax2.set_xlabel("Date")
ax2.set_ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("Rural vs Urban Average Unemployment Rate")
rural_vs_urban = merged_df.groupby('area')['estimated_unemployment_rate_percent'].mean()
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(x=rural_vs_urban.index, y=rural_vs_urban.values, palette=['green','blue'], ax=ax3)
ax3.set_ylabel("Unemployment Rate (%)")
st.pyplot(fig3)

st.subheader("Predicted vs Actual Unemployment Rates (Test Set)")
# Compute predictions on test set for visualization
features = ['estimated_employed', 'estimated_labour_participation_rate_percent', 'region', 'area']
X = pd.get_dummies(merged_df[features], drop_first=True)
y = merged_df['estimated_unemployment_rate_percent']
# Ensure columns match
for col in model.feature_names_in_:
    if col not in X.columns:
        X[col] = 0
X = X[model.feature_names_in_]

y_pred = model.predict(X)
results = pd.DataFrame({'Actual': y, 'Predicted': y_pred})
results['Error_Type'] = results.apply(lambda row: 'Overpredicted' if row['Predicted']>row['Actual'] else 'Underpredicted', axis=1)

fig4, ax4 = plt.subplots(figsize=(10,6))
sns.scatterplot(x='Actual', y='Predicted', hue='Error_Type', data=results, alpha=0.6, palette={'Overpredicted':'red','Underpredicted':'blue'}, ax=ax4)
ax4.plot([results['Actual'].min(), results['Actual'].max()],
         [results['Actual'].min(), results['Actual'].max()],
         'k--', lw=2)
ax4.set_xlabel("Actual Unemployment Rate")
ax4.set_ylabel("Predicted Unemployment Rate")
st.pyplot(fig4)
