p = int(input('Em que ano nasceu o seu competidor??'))
i = 2024 - p
if i < 9:
    print('O seu filho está classificado na categória MIRIM, visto que ele tem {} ano(s)'.format(i))
elif  9 < i > 14:
    print('O seu filho está classificado na categória INFANTIL, visto que ele tem {} ano(s)'.format(i))
elif  14 < i > 19:
    print('O seu filho está classificado na categória JUNIOR, visto que ele tem {} ano(s)'.format(i))
elif  19 < i > 20:
    print('O seu filho está classificado na categória SÊNIOR, visto que ele tem {} ano(s)'.format(i))
else:
    i > 20
    print('O seu filho está classificado na categória MASTER, visto que ele tem {} ano(s)'.format(i))