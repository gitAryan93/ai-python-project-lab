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

# === AI Career Coach ===
print("=== Welcome to AI Career Coach ===")

interest = input ("What excites you more? (web / ai / data): ").lower()
skill_level = int(input("On a scale of 1-10, how skilled are you in coding?: "))
mood = input("How are you feeling today? (motivated / tired / curious): ").lower()

confidence_score = random.randint(70, 95)
ai_response("Analyzing your career profile...", status="info", confidence=confidence_score)

if interest == "web" and skill_level >=7:
    ai_response("You're ready to build real-world web apps. Aim for a frontend developer internship!", status="success", confidence=confidence_score)
elif interest == "ai" and skill_level >= 5 and mood == "curious":
    ai_response ("You're on track for AI. Start learning Python libraries like NumPy and scikit-learn.", status= "warn", confidence=confidence_score)
elif interest ==  "data" and skill_level >= 4:
    ai_response ("Consider data analyst projects with real datasets. Start with Pandas and Matplotlib.", status= "warn", confidence=confidence_score)
else:
    ai_response("Start with web development basics to build confidence, then explore other pats!", status= "fail", confidence=confidence_score)

print ("\n=== End of Career Coaching ===")
