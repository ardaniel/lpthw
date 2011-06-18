# define a format string
formatter = "%r %r %r %r"

# pass a few examples to the formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# the quotes in the third line pass because there's an apostrophe in
# the statement; we know what an apostrophe is, but Python only sees a
# single quote.

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
