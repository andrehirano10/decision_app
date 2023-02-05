def weigh_decisions():
    decision1 = input("Enter the first decision: ")
    decision2 = input("Enter the second decision: ")

    decision1_rating = 0
    decision2_rating = 0

    self_efficacy = input("Which decision will make you feel more confident and capable? ({} or {}): enter 1 or 2)  ".format(decision1, decision2)).lower()
    if self_efficacy == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    growth = input("Which decision will offer you more opportunities to grow and develop as a person? ({} or {}): ".format(decision1, decision2)).lower()
    if growth == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1

    meaning = input("Which decision will give you greater meaning in life? (choose 1 or 2")
    if meaning == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    regret = input("Are you more likely to regret not make which decision {} or {}? (choose 1 or 2): ".format(decision1, decision2,)).lower()
    if regret == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1
    wise_counsel = input("What would the wisest version of yourself counsel you to do? ({} or {}): ".format(decision1, decision2)).lower()
    if wise_counsel == "1":
        decision1_rating += 1
    else:
        decision2_rating += 1

    if decision1_rating > decision2_rating:
        print("Go ahead with {}: ".format(decision1))
    else:
        print("Go ahead with {}: ".format(decision2))
weigh_decisions()