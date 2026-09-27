import random

print("Welocome to KBC")

ques = [
    [
        "What is the capital of India?", 
        ["Mumbai", "Kolkata", "New Delhi", "Chennai"], 
        "New Delhi"
    ],
    [
        "How many continents are there in the world?", 
        ["5", "6", "7", "8"], 
        "7"
    ],
    [
        "Which planet is called the Red Planet?", 
        ["Venus", "Mars", "Jupiter", "Saturn"], 
        "Mars"
    ],
    [
        "Who is known as the Father of the Nation in India?", 
        ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Bhagat Singh"], 
        "Mahatma Gandhi"
    ],
    [
        "In which year did India get independence?", 
        ["1945", "1947", "1950", "1952"], 
        "1947"
    ],
    [
        "Which is the largest mammal on Earth?", 
        ["Elephant", "Blue Whale", "Giraffe", "Shark"], 
        "Blue Whale"
    ],
    [
        "What is the chemical symbol for water?", 
        ["CO2", "O2", "H2O", "NaCl"], 
        "H2O"
    ],
    [
        "Who invented the telephone?", 
        ["Thomas Edison", "Albert Einstein", "Alexander Graham Bell", "Nikola Tesla"], 
        "Alexander Graham Bell"
    ],
    [
        "Which bird is known as a symbol of peace?", 
        ["Eagle", "Dove", "Peacock", "Sparrow"], 
        "Dove"
    ],
    [
        "How many players are there in a cricket team on the field?", 
        ["9", "10", "11", "12"], 
        "11"
    ]
]

amounts = [50000, 60000, 75000, 90000, 110000, 135000, 160000, 180000, 195000, 200000]
scr_amt = 0
q_cnt = 0

for amt in amounts:
    ques_pick = random.choice(ques)
    q_cnt += 1
    display_question = ques_pick[0]
    print(f"Qustion {q_cnt}: {display_question}")

    display_options = ques_pick[1]
    # print(display_options)
    opt_cnt = 0
    for j in display_options:
        opt_cnt += 1
        print(f"{opt_cnt}. {j}")

    display_amt = amt
    print(f"Qustion Ammount: ₹{display_amt}\n")

    ans = int(input("Enter your choice (1-4) : ")) - 1
    try:

        if display_options[ans] == ques_pick[2]:
            scr_amt += display_amt
            print("You Win !!")
            print(f"Your Score Ammount: ₹{scr_amt}\n")

        else:
            print("You Lose !!\n")
            break

    except :
        print("Please enter a valid choice\n")




    ques.remove(ques_pick)