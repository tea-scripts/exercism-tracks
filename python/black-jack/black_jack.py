"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

face_cards = {"J", "Q", "K", "10"}


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card == "A":
        value = 1
    elif card in face_cards:
        value = 10
    else:
        value = int(card)

    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        value = card_one, card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        value = card_one
    else:
        value = card_two

    return value


def is_ace(card):
    """Determine if a card is an ace card.

    :param card: str
    :return: bool

    """
    if card == "A":
        return True
    return False


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ace = 11
    max_cards = 21
    sum_of_cards = value_of_card(card_one) + value_of_card(card_two)

    if (sum_of_cards + ace) > max_cards:
        ace_value = 1
    elif is_ace(card_one) or is_ace(card_two):
        ace_value = 1
    else:
        ace_value = 11

    return ace_value


def ten_card(card_one, card_two):
    """Determine if a card has a value of 10
    :param card_one, card_two: str
    :return: bool
    """
    card_one_and_two = [card_one, card_two]
    if any(item in face_cards for item in card_one_and_two):
        return True
    return False


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    is_ten_card = ten_card(card_one, card_two)
    is_ace_card = is_ace(card_one) or is_ace(card_two)

    if is_ten_card and is_ace_card:
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    same_value = value_of_card(card_one) == value_of_card(card_two)

    if same_value:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    sum_of_cards = value_of_card(card_one) + value_of_card(card_two)

    if 9 <= sum_of_cards <= 11:
        return True
    return False
