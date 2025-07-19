import random


def ai_response(msg, status="info", confidence=None):
    if status == "success":
        print(f"\u2705 {msg}")
    elif status == "fail":
        print(f"\u274C {msg}")
    elif status == "warn":
        print(f"\u26A0 {msg}")
    else:
        print(f"🧠 {msg}")

        if confidence is not None:
            print(f"🧠 AI Confidence: {confidence}%")
            bar_filled = int(confidence / 5)
            bar = "🟩" * bar_filled + "⬜️" * (20 - bar_filled)
            print(bar)


print("=== AI Loan Approval Predictor===")

age = int(input("Enter your age: "))
income = int(input("Enter monthly income ($): "))
credit_score = int(input("Enter credit score (300-850): "))

confidence_score = random.randint(70, 95)

# Simulated "AI model" logic

ai_response("Analyzing user input with AI logic...",
            status="info", confidence=confidence_score)
if age >= 21 and income >= 3000 and credit_score >= 650:
    ai_response("Approved: You meet all AI prediction thresholds",
                status="success")
elif 600 <= credit_score < 650 or 3000 <= income < 3500:
    ai_response(
        "Warning: You're borderline. Improve credit or income.", status="warn")
elif age < 21:
    ai_response("Rejected: Too young for approval.", status="fail")
elif credit_score < 600:
    ai_response("Rejected: Credit score too low.", status="fail")
elif income < 3000:
    ai_response("Rejected: Not enough income.", status="fail")
else:
    ai_response("Rejected: Multiple weak factors.", status="fail")

    print("=== End of Simulation ===")
