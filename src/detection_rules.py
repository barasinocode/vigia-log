def calculate_risk_score(row):
    score = 0

    if row["status"] == "FAILED":
        score += 1

    if row["hour"] < 6 or row["hour"] >= 23:
        score += 2

    return score


def classify_risk(score):
    if score >= 6:
        return "HIGH"

    if score >= 3:
        return "MEDIUM"

    return "LOW"


def analyze_security_events(df):
    df = df.copy()

    df["risk_score"] = df.apply(
        calculate_risk_score,
        axis=1
    )

    df["risk_level"] = df["risk_score"].apply(
        classify_risk
    )

    return df