def analyze_message(message):
    message_lower = message.lower()

    risk_score = 0
    reasons = []

    # Prize or winning scams
    prize_keywords = ["won", "winner", "prize", "lottery", "reward", "congratulations"]
    if any(keyword in message_lower for keyword in prize_keywords):
        risk_score += 25
        reasons.append("Unexpected prize or winning message")

    # Payment requests
    payment_keywords = [
        "pay", "payment", "fee", "transfer",
        "send money", "deposit"
    ]
    if any(keyword in message_lower for keyword in payment_keywords):
        risk_score += 25
        reasons.append("Requests money or a payment")

    # Urgency
    urgency_keywords = [
        "urgent", "immediately", "now",
        "limited time", "act fast"
    ]
    if any(keyword in message_lower for keyword in urgency_keywords):
        risk_score += 20
        reasons.append("Creates urgency or pressure")

    # Suspicious links
    link_keywords = [
        "click", "link", "http://", "https://",
        "verify here"
    ]
    if any(keyword in message_lower for keyword in link_keywords):
        risk_score += 20
        reasons.append("Contains a request or link to click")

    # Account threats
    account_threats = [
        "account blocked",
        "account suspended",
        "account will be closed",
        "verify your account"
    ]
    if any(keyword in message_lower for keyword in account_threats):
        risk_score += 25
        reasons.append("Threatens account suspension or requests verification")

    # Sensitive information
    sensitive_keywords = [
        "otp",
        "password",
        "pin",
        "cvv",
        "card number"
    ]
    if any(keyword in message_lower for keyword in sensitive_keywords):
        risk_score += 25
        reasons.append("Requests or mentions sensitive information")

    # Impersonation patterns
    impersonation_keywords = [
        "bank representative",
        "customer support",
        "government official",
        "income tax department"
    ]
    if any(keyword in message_lower for keyword in impersonation_keywords):
        risk_score += 20
        reasons.append("May impersonate an organization or authority")

    # Cap the maximum score
    risk_score = min(risk_score, 100)

    # Decide the risk level
    if risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 25:
        risk_level = "SUSPICIOUS"
    else:
        risk_level = "LOW"

    return risk_score, risk_level, reasons