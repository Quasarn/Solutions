def non_empty(funk):
    p = [i for i in funk() if i is not '' and i is not None]
    return p


@non_empty
def get_pages():
    return ['sfgdf', '', 'dsgdfg', '', 'dfhgfdhfghj', None]
print(get_pages)
