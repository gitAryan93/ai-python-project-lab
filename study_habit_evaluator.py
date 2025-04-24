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
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        print(bar)


# === AI Study Habit Evaluator ===
print("=== AI Study Habit Evaluator ===")

study_hours = float(input("How many hours did you study today? "))
sleep_hours = float(input("How many hours did you sleep last night? "))
mood = input(
    "How are you feeling today? (motivated/tired/burned out): ").lower()

confidence_score = random.randint(70, 95)
ai_response("Analyzing your study habits...",
            status="info", confidence=confidence_score)

if study_hours >= 5 and sleep_hours >= 7 and mood == "motivated":
    ai_response("You're crushing it! Keep this up and success is inevitable.",
                status="success", confidence=confidence_score)
elif 3 <= study_hours < 5 or 5 <= sleep_hours < 7 or mood == "tired":
    ai_response("Decent effort, but try improving sleep or staying consistent with study time.",
                status="warn", confidence=confidence_score)
else:
    ai_response("Warning! Your current habits may slow your progress. Let's fix that!",
                status="fail", confidence=confidence_score)

print("\n=== End of Habits Evaluation ===")
