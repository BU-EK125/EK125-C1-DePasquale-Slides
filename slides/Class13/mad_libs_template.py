# Class 13 Mad Libs Contest -- starter file
#
# Work through this file top to bottom. Each TODO marks something you
# need to fill in. Don't change WORD_BANK or TEMPLATE.

TABLE_NUMBER = 0  # TODO: set this to your table number

WORD_BANK = {
    "adj":   ["sneaky", "gigantic", "soggy"],
    "noun":  ["toaster", "llama", "professor"],
    "verb":  ["tango", "sneeze", "teleport"],
    "place": ["library", "volcano", "cafeteria"],
}

TEMPLATE = ("The {adj} {noun} loves to {verb} "
            "in the {place}.")


def mad_libs(template, word_bank, choices):
    story = template
    for blank, index in choices.items():
        # TODO: look up the word list for this blank in word_bank,
        # grab the word at this blank's index, then use
        # story.replace() to swap it into story.
        pass
    return story


# TODO: build your own CHOICES below -- same keys as WORD_BANK, each
# mapped to an index into that word's list. Make it as funny as you can!
CHOICES = {
    "adj": 0,
    "noun": 0,
    "verb": 0,
    "place": 0,
}

print(mad_libs(TEMPLATE, WORD_BANK, CHOICES))
