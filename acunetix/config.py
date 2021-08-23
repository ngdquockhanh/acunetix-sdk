API_BASE = 'https://localhost:3443/api/v1'
API_KEY = '1986ad8c0a5b3df4d7028d5f3c06e936cfe6506afbe494759875effe373b35aa7'

TARGET_CRITICALITYS = {
    "critical":"10",
    "high":"20",
    "normal":"10",
    "low":"0",
}   

PROFILES = {
    "full_scan":"11111111-1111-1111-1111-111111111111",
    "high_risk_vuln": "11111111-1111-1111-1111-111111111112",
    "xss_vuln": "11111111-1111-1111-1111-111111111116",
    "sql_injection_vuln": "11111111-1111-1111-1111-111111111113",
    "weak_passwords": "11111111-1111-1111-1111-111111111115",
    "crawl_only": "11111111-1111-1111-1111-111111111117",
}
