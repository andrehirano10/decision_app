def optimal_life_decision():
    positive_decision = 0

    self_efficacy = input("Do you feel confident and capable in making this decision? (yes/no): ").lower()
    if self_efficacy == "yes":
        positive_decision += 1
    else:
        positive_decision += 0
    growth = input("Will this decision help you grow and develop as a person? (yes/no): ").lower()
    if growth == "yes":
        positive_decision += 1
    else:
        positive_decision += 0

    meaning = input("Will this decision bring greater meaning to your life? (yes/no): ").lower()
    if meaning == "yes":
        positive_decision += 1
    else:
        positive_decision += 0
    goals = input("Does this decision align with your personal and professional goals? (yes/no): ").lower()
    if goals == "yes":
        positive_decision += 1
    else:
        goals_rating = 0
    positive_scenario = input("Can you imagine positive outcomes that may come from this decision? (yes/no): ").lower()
    if positive_scenario == "yes":
        positive_decision += 1
    else:
        positive_decision += 0

    wise_counsel = input("Would the wisest version of yourself counsel you to do this? (yes/no): ").lower()
    if wise_counsel == "yes":
        positive_decision += 1
    else:
        positive_decision += 0

    intuition = input("Does your intuition tell you it would be good?  (yes/no): ").lower()
    if intuition == "yes":
        positive_decision += 1
    else:
        positive_decision += 0

    gut = input("Does your head, heart and gut say yes?  (yes/no): ").lower()
    if gut == "yes":
        positive_decision += 1
    else:
        positive_decision += 0

    regret = input("Will you regret not taking this opportunity? (yes/no): ").lower()
    if regret == "yes":
        positive_decision += 1
    else:
        positive_decision += 0


    if positive_decision >= 5:
         print("Go ahead with the decision.")
    else:
        print("Consider reconsidering the decision.")

optimal_life_decision()