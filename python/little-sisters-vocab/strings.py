"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    new_vocab_words = [prefix]
    for word in vocab_words[1:]:
        new_vocab_words.append(f"{prefix}{word}")

    return " :: ".join(new_vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    new_word = word[:-4]

    if new_word[-1] == "i":
        restored_word = new_word[:-1]
        return f"{restored_word}y"

    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    suffix = "en"
    extracted_word = sentence.split()[index]
    if extracted_word[-1] == ".":
        sub_extracted_word = extracted_word[:-1]
        return f"{sub_extracted_word}{suffix}"

    return f"{extracted_word}{suffix}"


print(adjective_to_verb("I need to make that bright.", -1))
# print(adjective_to_verb("It got dark as the sun set.", 2))
