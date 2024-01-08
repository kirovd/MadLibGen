def mad_libs_generator():
    # Prompt the user for parts of speech
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")

    # The template story with placeholders
    story_template = f"Today I went to the zoo. I saw a {adjective} {noun} jumping up and down in its tree. He {verb} {adverb} through the large tunnel that led to its {adjective} shelter."

    # Print the completed story
    print("\nHere is your story:")
    print(story_template)

# Run the function
mad_libs_generator()
