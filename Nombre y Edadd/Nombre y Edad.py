nombre = raw_input('como te llamas? ')
try:
    anhos = int(raw_input('Hola %s, Cuantos años tienes?' % nombre))
    anhos = anhos + 1
    print 'En tu proximo cumpleaños tendras %d años' % (anhos)
except ValueError:
    print 'Eso no es una edad.'
