print("🛡️ Welcome to SmartPay Guard!")

message = input("Enter the suspicious message: ")

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

print("\n--- Analysis Result ---")
print("Risk Score:", risk_score)

if risk_score >= 50:
    print("⚠️ Risk Level: HIGH")
elif risk_score >= 25:
    print("⚠️ Risk Level: SUSPICIOUS")
else:
    print("✅ Risk Level: LOW")

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)