-- =========================================
-- VIGIA LOG - CONSULTAS DE ANÁLISE
-- =========================================


-- 1. TOTAL DE EVENTOS
SELECT COUNT(*) AS total_eventos
FROM login_events;


-- 2. TOTAL DE FALHAS DE LOGIN
SELECT COUNT(*) AS total_falhas
FROM login_events
WHERE status = 'FAILED';


-- 3. EVENTOS POR NÍVEL DE RISCO
SELECT
    risk_level,
    COUNT(*) AS quantidade
FROM login_events
GROUP BY risk_level
ORDER BY quantidade DESC;


-- 4. IPS COM MAIS FALHAS
SELECT
    ip_address,
    COUNT(*) AS failed_attempts
FROM login_events
WHERE status = 'FAILED'
GROUP BY ip_address
ORDER BY failed_attempts DESC;


-- 5. EVENTOS DE ALTO RISCO
SELECT
    timestamp,
    username,
    ip_address,
    status,
    risk_score,
    risk_level
FROM login_events
WHERE risk_level = 'HIGH'
ORDER BY risk_score DESC;


-- 6. POSSÍVEIS ATAQUES DE FORÇA BRUTA
SELECT
    ip_address,
    failed_attempts,
    risk_score,
    risk_level
FROM login_events
WHERE brute_force_alert = TRUE
ORDER BY failed_attempts DESC;


-- 7. IPS TENTANDO ACESSAR VÁRIAS CONTAS
SELECT
    ip_address,
    accounts_attempted,
    risk_score,
    risk_level
FROM login_events
WHERE multiple_accounts_alert = TRUE
ORDER BY accounts_attempted DESC;


-- 8. POSSÍVEIS CONTAS COMPROMETIDAS
SELECT
    timestamp,
    username,
    ip_address,
    status,
    risk_score,
    risk_level
FROM login_events
WHERE possible_compromise_alert = TRUE
ORDER BY timestamp DESC;


-- 9. USUÁRIOS COM MAIS FALHAS
SELECT
    username,
    COUNT(*) AS total_falhas
FROM login_events
WHERE status = 'FAILED'
GROUP BY username
ORDER BY total_falhas DESC;


-- 10. RESUMO DE ALERTAS
SELECT
    SUM(CASE WHEN brute_force_alert = TRUE THEN 1 ELSE 0 END)
        AS alertas_brute_force,

    SUM(CASE WHEN multiple_accounts_alert = TRUE THEN 1 ELSE 0 END)
        AS alertas_multiplas_contas,

    SUM(CASE WHEN possible_compromise_alert = TRUE THEN 1 ELSE 0 END)
        AS possiveis_comprometimentos
FROM login_events;