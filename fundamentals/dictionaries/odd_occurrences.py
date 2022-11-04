words = input().split(' ')
copied_to_lower = [word.lower() for word in words]
alternate = []
odd = [alternate.append(x) for x in copied_to_lower if copied_to_lower.count(x) % 2 != 0 and x not in alternate]
print(' '.join(alternate))
