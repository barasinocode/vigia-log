import pandas as pd

df = pd.read_csv("data/processed/security_events.csv")

print("\n=== RESUMO VIGIA LOG ===")
print(f"Total de eventos: {len(df)}")
print(f"Falhas de login: {(df['status'] == 'FAILED').sum()}")
print(f"Eventos HIGH: {(df['risk_level'] == 'HIGH').sum()}")
print(f"Eventos MEDIUM: {(df['risk_level'] == 'MEDIUM').sum()}")
print(f"Eventos LOW: {(df['risk_level'] == 'LOW').sum()}")

print("\n=== ALERTAS ===")
print(f"Força bruta: {df['brute_force_alert'].sum()}")
print(f"Múltiplas contas por IP: {df['multiple_accounts_alert'].sum()}")
print(
    "Possível comprometimento:",
    df["possible_compromise_alert"].sum()
)

print("\n=== IPS COM MAIS FALHAS ===")
failed = (
    df[df["status"] == "FAILED"]
    .groupby("ip_address")
    .size()
    .sort_values(ascending=False)
)

print(failed.head(10))

import matplotlib.pyplot as plt


# =========================
# GRÁFICO 1 - NÍVEL DE RISCO
# =========================

risk_counts = df["risk_level"].value_counts()

plt.figure(figsize=(7, 4))
risk_counts.plot(kind="bar")

plt.title("Eventos por Nível de Risco")
plt.xlabel("Nível de risco")
plt.ylabel("Quantidade de eventos")

plt.tight_layout()
plt.show()


# =========================
# GRÁFICO 2 - IPS COM MAIS FALHAS
# =========================

failed_by_ip = (
    df[df["status"] == "FAILED"]
    .groupby("ip_address")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(8, 4))
failed_by_ip.plot(kind="bar")

plt.title("IPs com Mais Falhas de Login")
plt.xlabel("IP")
plt.ylabel("Quantidade de falhas")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# =========================
# GRÁFICO 3 - EVENTOS POR HORA
# =========================

events_by_hour = (
    df.groupby("hour")
    .size()
    .sort_index()
)

plt.figure(figsize=(8, 4))
events_by_hour.plot(kind="line", marker="o")

plt.title("Eventos por Hora do Dia")
plt.xlabel("Hora")
plt.ylabel("Quantidade de eventos")

plt.tight_layout()
plt.show()

import os
import matplotlib.pyplot as plt

# Garantir que a pasta docs exista
os.makedirs("docs", exist_ok=True)


# =========================
# GRÁFICO 1 - NÍVEL DE RISCO
# =========================

risk_counts = df["risk_level"].value_counts()

plt.figure(figsize=(7, 4))
risk_counts.plot(kind="bar")

plt.title("Eventos por Nível de Risco")
plt.xlabel("Nível de risco")
plt.ylabel("Quantidade de eventos")

plt.tight_layout()

plt.savefig(
    "docs/risk_levels.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()


# =========================
# GRÁFICO 2 - IPS COM MAIS FALHAS
# =========================

failed_by_ip = (
    df[df["status"] == "FAILED"]
    .groupby("ip_address")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(8, 4))
failed_by_ip.plot(kind="bar")

plt.title("IPs com Mais Falhas de Login")
plt.xlabel("IP")
plt.ylabel("Quantidade de falhas")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "docs/failed_logins_by_ip.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()


# =========================
# GRÁFICO 3 - EVENTOS POR HORA
# =========================

events_by_hour = (
    df.groupby("hour")
    .size()
    .sort_index()
)

plt.figure(figsize=(8, 4))
events_by_hour.plot(
    kind="line",
    marker="o"
)

plt.title("Eventos por Hora do Dia")
plt.xlabel("Hora")
plt.ylabel("Quantidade de eventos")

plt.tight_layout()

plt.savefig(
    "docs/events_by_hour.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()


print("\nGráficos gerados com sucesso:")
print("docs/risk_levels.png")
print("docs/failed_logins_by_ip.png")
print("docs/events_by_hour.png")



