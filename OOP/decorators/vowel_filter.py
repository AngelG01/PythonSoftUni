def vowel_filter(function):
    def wrapper():
        vowels = function()
        filtered = [x for x in vowels if x.lower() in 'aeiouy']
        return filtered

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
