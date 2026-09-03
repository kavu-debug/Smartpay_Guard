def analyze_message(message):
    message_lower = message.lower()

    risk_score = 0
    reasons = []

    # Prize or winning scams
    if "won" in message_lower or "prize" in message_lower:
        risk_score += 25
        reasons.append("Unexpected prize or winning message")

    # Payment requests
    if "pay" in message_lower or "fee" in message_lower:
        risk_score += 25
        reasons.append("Requests money or a payment")

    # Urgency
    if "urgent" in message_lower or "immediately" in message_lower:
        risk_score += 20
        reasons.append("Creates urgency")

    # Suspicious links
    if "click" in message_lower or "link" in message_lower:
        risk_score += 20
        reasons.append("Contains a request to click a link")

    # New pattern: account threats
    if "account blocked" in message_lower or "account suspended" in message_lower:
        risk_score += 25
        reasons.append("Threatens account suspension or blocking")

    # New pattern: requests sensitive information
    if "otp" in message_lower or "password" in message_lower:
        risk_score += 25
        reasons.append("Requests sensitive information")

    # Decide the risk level
    if risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 25:
        risk_level = "SUSPICIOUS"
    else:
        risk_level = "LOW"

    return risk_score, risk_level, reasons