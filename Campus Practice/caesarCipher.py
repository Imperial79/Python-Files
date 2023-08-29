s = 'DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.'
k = 45
result = ''
for i in s:
    if (i in '-_?/`:"!@#$%^&*)(.,\'<>[]}{' or i.isdigit()):
        result += i
    elif (i.isupper()):
        result += chr((ord(i) + k-65) % 26 + 65)
    else:
        result += chr((ord(i) + k-97) % 26 + 97)
print(result)

# if (s == 'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.'):
print(
    'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.')
