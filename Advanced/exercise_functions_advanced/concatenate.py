def concatenate(*args, **kwargs):
    sentence = ''.join(args)

    for key in kwargs:
         sentence = sentence.replace(key, kwargs[key])

    return sentence

print(concatenate("Soft", "UNI", "Is", "Grate"  , "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))