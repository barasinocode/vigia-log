from data_cleaning import load_and_clean_data
from detection_rules import analyze_security_events


def main():
    print("Vigia Log")
    print("Iniciando análise...")

    df = load_and_clean_data("data/raw/login_logs.csv")

    result = analyze_security_events(df)

    result.to_csv(
        "data/processed/security_events.csv",
        index=False
    )

    print("Análise concluída.")
    print("Arquivo gerado em:")
    print("data/processed/security_events.csv")


if __name__ == "__main__":
    main()