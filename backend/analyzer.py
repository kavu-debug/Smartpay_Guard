def analyze_message(message):
    message_lower = message.lower()

    risk_score = 0
    reasons = []

    if "won" in message_lower or "prize" in message_lower:
        risk_score += 25
        reasons.append("Unexpected prize or winning message")

    if "pay" in message_lower or "fee" in message_lower:
        risk_score += 25
        reasons.append("Requests money or a payment")

    if "urgent" in message_lower or "immediately" in message_lower:
        risk_score += 20
        reasons.append("Creates urgency")

    if "click" in message_lower or "link" in message_lower:
        risk_score += 20
        reasons.append("Contains a request to click a link")

    if risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 25:
        risk_level = "SUSPICIOUS"
    else:
        risk_level = "LOW"

    return risk_score, risk_level, reasons