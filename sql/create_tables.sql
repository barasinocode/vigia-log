CREATE TABLE IF NOT EXISTS login_events (

    id SERIAL PRIMARY KEY,

    timestamp TIMESTAMP NOT NULL,

    username VARCHAR(100),

    ip_address VARCHAR(50),

    country VARCHAR(100),

    status VARCHAR(20),

    device VARCHAR(100),

    event_date DATE,

    event_hour INTEGER,

    failed_attempts INTEGER,

    accounts_attempted INTEGER,

    risk_score INTEGER,

    risk_level VARCHAR(20),

    brute_force_alert BOOLEAN,

    multiple_accounts_alert BOOLEAN,

    possible_compromise_alert BOOLEAN

);