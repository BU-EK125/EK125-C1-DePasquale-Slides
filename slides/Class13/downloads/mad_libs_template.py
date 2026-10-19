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


# TODO: write a function called mad_libs with three parameters: the
# template, the word bank, and the choices. Then:
#   1. start with story = template
#   2. loop over choices.items() as (blank, index)
#   3. look up the word in word_bank, then use story.replace() to
#      swap it into story
#   4. return story


# TODO: build your own CHOICES below -- same keys as WORD_BANK, each
# mapped to an index into that word's list. Make it as funny as you can!
CHOICES = {
    "adj": 0,
    "noun": 0,
    "verb": 0,
    "place": 0,
}

# TODO: call your function with TEMPLATE, WORD_BANK, and CHOICES, and
# print the result.
print(CALL_YOUR_FUNCTION_HERE)
