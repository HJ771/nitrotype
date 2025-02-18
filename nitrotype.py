import random

WORDS = [
    "argentina", "brazil", "canada", "denmark", "egypt", "france", "germany",
    "hungary", "india", "japan", "kenya", "luxembourg", "mexico", "netherlands",
    "oman", "portugal", "qatar", "russia", "spain", "turkey", "ukraine",
    "vietnam", "wales", "xiamen", "yemen", "zimbabwe"
]

NUM_WORDS = 15  

def typing_test():
    selected_words = random.sample(WORDS, NUM_WORDS)
    mistakes = 0

    print("Typing Test! Type the words exactly as shown.")

    for word in selected_words:
        print(f"\nType this word: {word}")
        user_input = input("Your input: ").strip()

        if user_input == word:
            print("BIEN WILLYYYY!")
        else:
            print("Yo creo que esta mal!")
            mistakes += 1

    accuracy = ((NUM_WORDS - mistakes) / NUM_WORDS) * 100
    print("\nTerminaste wilson!")
    print(f"Total mistakes: {mistakes}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()

