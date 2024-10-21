import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Data da Venda' to datetime format for better analysis
sheet1_df['Data da Venda'] = pd.to_datetime(sheet1_df['Data da Venda'])

# Group by 'Região' and sum the 'Valor Total da Venda (R$)'
region_sales = sheet1_df.groupby('Região')['Valor Total da Venda (R$)'].sum().reset_index()

# Plotting the total sales by region
plt.figure(figsize=(10, 6))
sns.barplot(data=region_sales, x='Região', y='Valor Total da Venda (R$)', palette='viridis')
plt.title('Total Sales Value by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Value (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()