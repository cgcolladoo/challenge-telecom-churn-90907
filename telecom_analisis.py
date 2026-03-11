import pandas as pd

print("=== TELECOM CHURN ANALYSIS - TASK 90907 ===")

# Carga dataset (ajusta tu CSV)
df = pd.read_csv('telecom_clientes.csv')
print(f"Dataset shape: {df.shape}")
print(df.head(3))

# 1. Suites >= 1
df_suites = df.query('Suites >= 1')
print(f"Suites >=1: {len(df_suites)}")

# 2. Frecuencia Barrio
print("\nTop Barrios:")
print(df['Barrio'].value_counts().head())

# 3. Churn por Comercio
if 'Churn' in df.columns:
    churn_com = df.groupby('Comercio')['Churn'].mean()
    print("\nChurn Comercio:")
    print(churn_com)
else:
    print("\nAnálisis Comercio:")
    print(df['Comercio'].value_counts())

# 4. Riesgo: Area>80 OR Valor<4000
riesgo = df.query('(Area > 80) | (Valor < 4000)')
print(f"\nRiesgo churn: {len(riesgo)}")

# 5. Valor_total
if all(col in df.columns for col in ['Valor', 'Impuesto', 'Descuento']):
    df['Valor_total'] = df['Valor'] + df['Impuesto'] - df['Descuento']
    print("\nValor_total:")
    print(df['Valor_total'].head())

print("\n✅ ANÁLISIS COMPLETO")
print(df.info())
