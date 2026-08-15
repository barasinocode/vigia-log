def add_failed_attempts_count(df):
    df = df.copy()

    failed_counts = (
        df[df["status"] == "FAILED"]
        .groupby("ip_address")
        .size()
    )

    df["failed_attempts"] = (
        df["ip_address"]
        .map(failed_counts)
        .fillna(0)
        .astype(int)
    )

    return df


def add_multiple_accounts_count(df):
    df = df.copy()

    accounts_per_ip = (
        df.groupby("ip_address")["username"]
        .nunique()
    )

    df["accounts_attempted"] = (
        df["ip_address"]
        .map(accounts_per_ip)
        .fillna(0)
        .astype(int)
    )

    return df


def calculate_risk_score(row):
    score = 0

    # Login com falha
    if row["status"] == "FAILED":
        score += 1

    # Login em horário incomum
    if row["hour"] < 6 or row["hour"] >= 23:
        score += 2

    # Possível tentativa de força bruta
    if row["failed_attempts"] >= 5:
        score += 4

    # Mesmo IP tentando acessar várias contas
    if row["accounts_attempted"] >= 3:
        score += 4

    return score


def classify_risk(score):
    if score >= 6:
        return "HIGH"

    if score >= 3:
        return "MEDIUM"

    return "LOW"


def analyze_security_events(df):
    df = add_failed_attempts_count(df)

    df = add_multiple_accounts_count(df)

    df["risk_score"] = df.apply(
        calculate_risk_score,
        axis=1
    )

    df["risk_level"] = df["risk_score"].apply(
        classify_risk
    )

    df["brute_force_alert"] = (
        df["failed_attempts"] >= 5
    )

    df["multiple_accounts_alert"] = (
        df["accounts_attempted"] >= 3
    )

    return df
    