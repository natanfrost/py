formatter = '%r %r %r %r'

# using the raw formatter for printing integer values
print formatter % (1, 2, 3, 4)
# using the raw formatter for printing string values
print formatter % ('one', 'two', 'three', 'four')
# using the raw formatter for printing boolean values
print formatter % (True, False, True, False)
# using the raw formatter for printing it self (also a string)
print formatter % (formatter, formatter, formatter, formatter)
#same as second example
print formatter % (
    'I had this thing.',
    'That you could type up right.',
    "But it didn't sing.", # using double quote outside so I can use single quote inside
    'So I said goognight.'
    )
