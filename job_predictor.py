import random 
def ai_response (msg, status = "info", confidence=None):
    if status == "success":
        print (f"✅ {msg}")
    elif status == "fail":
        print (f"❌ {msg}")
    elif status == "warn":
        print (f"⚠️ {msg}")
    else:
        print (f"🧠 {msg}")

        if confidence is not None:
            print (f"🧠 AI confidence: {confidence}%")
            bar_filled = int(confidence / 5)
            bar = "█" * bar_filled + "░" * (20 - bar_filled)
            print(bar)


print ("=== AI Job Eligibility Predictor ===")

age = int (input ("Enter your age: "))
python_skill = int (input ("Rate your Python skill (0-10): "))
github_exp = input ("Do you have GitHub experience? (yes/no): ").lower()
projects =  int (input ("How many personal projects have you completed?: "))

confedince_score = random.randint(70, 95)
ai_response ("Analyzing your job readiness profile...", status= "info", confidence=confedince_score)

if age >= 18 and python_skill >= 7 and github_exp == "yes" and projects >= 3:
    ai_response ("You're ready to apply for junior developer role!", status="success", confidence=confedince_score)

elif python_skill >= 5 or projects >= 2: 
    ai_response("You're close. A little more experience will help", status="warn", confidence=confedince_score)

else: 
    ai_response("You're not job-ready yet. Keep building your skills.", status="fail", confidence=confedince_score)

print("=== End of Evalution ===")# Predicts job readiness based on coding experience and project count — built by Aryan Haidary

import random 
def ai_response (msg, status = "info", confidence=None):
    if status == "success":
        print (f"✅ {msg}")
    elif status == "fail":
        print (f"❌ {msg}")
    elif status == "warn":
        print (f"⚠️ {msg}")
    else:
        print (f"🧠 {msg}")

        if confidence is not None:
            print (f"🧠 AI confidence: {confidence}%")
            bar_filled = int(confidence / 5)
            bar = "█" * bar_filled + "░" * (20 - bar_filled)
            print(bar)


print ("=== AI Job Eligibility Predictor ===")

age = int (input ("Enter your age: "))
python_skill = int (input ("Rate your Python skill (0-10): "))
github_exp = input ("Do you have GitHub experience? (yes/no): ").lower()
projects =  int (input ("How many personal projects have you completed?: "))

confedince_score = random.randint(70, 95)
ai_response ("Analyzing your job readiness profile...", status= "info", confidence=confedince_score)

if age >= 18 and python_skill >= 7 and github_exp == "yes" and projects >= 3:
    ai_response ("You're ready to apply for junior developer role!", status="success", confidence=confedince_score)

elif python_skill >= 5 or projects >= 2: 
    ai_response("You're close. A little more experience will help", status="warn", confidence=confedince_score)

else: 
    ai_response("You're not job-ready yet. Keep building your skills.", status="fail", confidence=confedince_score)

print("=== End of Evalution ===")