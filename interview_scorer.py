import random

def ai_response(msg, status="info", confidence=None):
    if status == "success":
        print(f"✅ {msg}")
    elif status == "fail":
        print(f"❌ {msg}")
    elif status == "warn":
        print(f"⚠️ {msg}")
    else:
        print(f"🧠 {msg}")

    if confidence is not None:
        print(f"🧠 AI Confidence: {confidence}%")
        bar_filled = int(confidence / 5)
        bar = "🟩" * bar_filled + "⬜" * (20 - bar_filled)
        print(bar)


#Interview questions
questions = [
    "Why do you want to work in tech?",
    "What's your greatest strength as a developer?",
    "How do you handle bugs and errors in code"
]

total_score = 0

for question in questions:
    input(f"\n {question} ")
    score = random.randint(1, 5)
    total_score += score
    print(f"📝 AI scored this answer: {score}/5")

# Feedback based on total score 
confidence_score = random.randint (70, 95)
print("\nAnalyzing your interview performance...\n")
if total_score >= 13:
    ai_response("You nailed the interview! Expect a callback soon.", status="success", confidence=confidence_score)
elif total_score >= 8:
    ai_response("Decent answers. You're on the right track, keep improving!", status="warn", confidence=confidence_score)
else:
    ai_response("Needs stronger, clearer answers. Practice more!", status="fail", confidence=confidence_score)

print("\n=== End of Interview Simulation ===")