def mad_libs():
    print("Let's play Mad Libs! Please provide the following words:\n")

    # Collect user inputs
    adjective1 = input("Adjective: ")
    noun1 = input("Noun: ")
    verb_past = input("Verb (past tense): ")
    adverb = input("Adverb: ")
    adjective2 = input("Another adjective: ")
    noun2 = input("Another noun: ")
    noun3 = input("One more noun: ")
    verb = input("Verb: ")
    adjective3 = input("Final adjective: ")

    # Story template
    story = f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    It {verb_past} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic {noun3} towering above my head.
    Feeding that animal made me hungry. I went to get a {verb} scoop of ice cream.
    It filled my stomach. Afterwards, I had to run to catch our {adjective3} bus home.
    It was a really fun day!
    """

    print("\n🎉 Here's your Mad Libs story:\n")
    print(story)

# Run the game
mad_libs()
