book_summaries_dict = {
    "Pride and Prejudice": (
        "Jane Austen’s classic romantic novel centers on Elizabeth Bennet, "
        "a strong-willed young woman navigating love, family expectations, and social class in 19th-century England. "
        "The story explores her evolving relationship with Mr. Darcy, a wealthy but initially proud aristocrat. "
        "Through misunderstandings, witty dialogue, and tender moments of romance, the two characters learn humility, "
        "self-awareness, and the true meaning of love. Themes include romance, love, marriage, family, prejudice, "
        "gender roles, and the tension between social reputation and personal happiness. "
        "It remains one of the most beloved romance novels of all time."
    ),
    "1984": (
        "George Orwell’s dystopian masterpiece paints a terrifying picture of a totalitarian regime under Big Brother, "
        "where individuality, freedom, and love are crushed by absolute state control. "
        "The protagonist Winston Smith longs for truth and romance in a world of surveillance, lies, and fear. "
        "He dares to love Julia and secretly dream of rebellion, only to face brutal consequences. "
        "Themes include government surveillance, censorship, propaganda, individuality vs. conformity, freedom, and resistance. "
        "It is one of the most famous dystopian novels, warning about authoritarianism and the fragility of truth."
    ),
    "The Hobbit": (
        "J.R.R. Tolkien’s beloved fantasy adventure follows Bilbo Baggins, a hobbit who loves comfort but is pulled "
        "into a daring quest with a group of dwarves to reclaim their homeland from the dragon Smaug. "
        "The journey takes Bilbo across wild landscapes filled with trolls, goblins, elves, and giant spiders. "
        "Most famously, he encounters Gollum and discovers the magic ring that will shape the fate of Middle-earth. "
        "Bilbo evolves from a reluctant participant to a clever, courageous adventurer. "
        "Themes include friendship, personal growth, courage, good vs. evil, and the thrill of fantasy adventures."
    ),
    "To Kill a Mockingbird": (
        "Harper Lee’s powerful novel, set in the racially divided American South of the 1930s, explores justice, morality, "
        "and compassion through the eyes of young Scout Finch. Her father, Atticus Finch, is a lawyer defending Tom Robinson, "
        "a Black man falsely accused of assaulting a white woman. As Scout and her brother Jem grow up, they confront issues of "
        "race, prejudice, empathy, and courage. Themes include childhood innocence, the fight for justice, morality, family, "
        "community, and the courage to stand up for what is right. It is a deeply moving story about empathy and human dignity."
    ),
    "The Catcher in the Rye": (
        "J.D. Salinger’s influential coming-of-age novel follows Holden Caulfield, a cynical teenager struggling with identity, "
        "authenticity, alienation, and the transition from childhood to adulthood. After being expelled from school, Holden "
        "wanders New York City searching for meaning, honesty, and connection. He is disillusioned with the superficiality of "
        "society but deeply longs to protect innocence, particularly that of children. Themes include identity, rebellion, "
        "alienation, authenticity, mental health, and the challenges of adolescence. It is a classic story of teenage struggle "
        "and self-discovery."
    ),
    "The Great Gatsby": (
        "F. Scott Fitzgerald’s iconic Jazz Age novel portrays the glitter, ambition, and illusion of the American Dream. "
        "Through narrator Nick Carraway, we meet Jay Gatsby, a mysterious millionaire who hosts dazzling parties in hopes "
        "of rekindling his romance with Daisy Buchanan. Beneath the glamour lies emptiness, corruption, and tragic longing. "
        "Themes include love, wealth, social class, ambition, illusion vs. reality, romance, and the decline of the American Dream. "
        "It is a story of obsession, romance, betrayal, and the cost of chasing dreams."
    ),
    "Brave New World": (
        "Aldous Huxley’s dystopian vision imagines a futuristic society where people are genetically engineered, conditioned for obedience, "
        "and distracted by constant pleasure. Individuality, family, and love are sacrificed for stability. "
        "The novel follows characters like John the Savage, who questions conformity, control, and the absence of authentic love and freedom. "
        "Themes include technology, conformity, dehumanization, consumerism, dystopia, love vs. control, and the cost of progress. "
        "It is a cautionary tale about sacrificing humanity for stability."
    ),
    "The Alchemist": (
        "Paulo Coelho’s philosophical fable follows Santiago, a shepherd boy who dreams of treasure near the pyramids of Egypt. "
        "Guided by omens, mentors, and his own courage, Santiago embarks on a long journey of adventure, discovery, and spiritual growth. "
        "Along the way, he learns lessons about destiny, love, intuition, courage, and following one’s personal legend. "
        "Themes include fate, love, destiny, adventure, spirituality, courage, and perseverance. "
        "It is an uplifting story about self-discovery and the search for meaning."
    ),
    "Life of Pi": (
        "Yann Martel’s novel tells the extraordinary story of Pi Patel, a teenager who survives a shipwreck only to find himself "
        "stranded on a lifeboat with a Bengal tiger named Richard Parker. Pi’s 227-day journey at sea is one of survival, courage, "
        "faith, and the tension between reality and imagination. Themes include survival, storytelling, religion, hope, belief, "
        "and the relationship between humans and nature. It is both an adventure tale and a meditation on spirituality and resilience."
    )
}

def get_summary_by_title(title: str) -> str:
    summary = book_summaries_dict.get(title)
    if summary:
        return summary
    return "Sorry, I couldn't find a detailed summary for that title."

if __name__ == "__main__":
    t = input("Enter book title: ")
    print(get_summary_by_title(t))
