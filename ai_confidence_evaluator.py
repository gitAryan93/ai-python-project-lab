def ai_confidence_evaluator():
    print("AI Logic Puzzle: Confidence Evaluator\n")

    answer = input("Is fire cold? (yes/no): ").strip().lower()

    if answer == "yes":
        print("That's incorrect. Fire is hot.")
        print("Confidence Level: 10%")
    elif answer == "no":
        print("Correct. Fire is hot.")
        print("Confidence Level: 95%")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        print("Confidence Level: 50%")


ai_confidence_evaluator()
