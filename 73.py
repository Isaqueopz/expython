times = ('Palmeiras','Grêmio','Atlético-mg','Flamengo','Botafogo','Red bull bragantino','Fluminense','Atletico-pr','Internacional','Fortaleza','São paulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba','América-mg')

print(f'os cinco primeiro colocados são {times[0:5]} ')
print(f'os ultimo quatro colocados são {times[16:21]} ') #{times[-4:]}
print(sorted(times))
print('o time do vasco está na {} posição'.format(times.index('Vasco')))