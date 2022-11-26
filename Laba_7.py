from loguru import logger

logger.remove(handler_id=None)
logger.add('laba_7.log', format='{time} {level} {message}', level='INFO', rotation='10 KB', compression='zip')

k = 0
l = 0
m = 0
n = 0
figure1 = ''
figure2 = ''

while figure1 == '':
    try:
        figure1 = str(input('Введите тип фигуры: ферзь, ладья, слон или конь = '))
        if (figure1 != 'ферзь') and (figure1 != 'ладья') and (figure1 != 'слон') and (figure1 != 'конь'):
            print('Ошибка ввода!')
            logger.error('figure1 = ' + str(figure1))
            figure1 = ''
    except ValueError:
        print('Ошибка ввода!')
        logger.error('figure1 = ' + str(figure1))
logger.info('figure1 = ' + str(figure1))

while k == 0:
    try:
        k = int(input('Введите номер клетки 1 фигуры по горизонтали целым числом от 1 до 8 = '))
        if k > 8 or k < 1 or k % 1 > 0:
            print('Ошибка ввода!')
            logger.error('k = ' + str(k))
            k = 0
    except ValueError:
        print('Ошибка ввода!')
        logger.error('k = ' + str(k))
logger.info('k = ' + str(k))

while l == 0:
    try:
        l = int(input('Введите номер клетки 1 фигуры по вертикали целым числом от 1 до 8 = '))
        if l > 8 or l < 1 or l % 1 > 0:
            print('Ошибка ввода!')
            l = 0
            logger.error('l = ' + str(l))
    except ValueError:
        print('Ошибка ввода!')
        logger.error('l = ' + str(l))
logger.info('l = ' + str(l))

while figure2 == '':
    try:
        figure2 = str(input('Введите тип фигуры: ферзь, ладья, слон или конь = '))
        if (figure2 != 'ферзь') and (figure2 != 'ладья') and (figure2 != 'слон') and (figure2 != 'конь'):
            print('Ошибка ввода!')
            logger.error('figure2' + str(figure2))
            figure2 = ''
    except ValueError:
        print('Ошибка ввода!')
        logger.error('figure2 = ' + str(figure2))
logger.info('figure2 = ' + str(figure2))

while m == 0:
    try:
        m = int(input('Введите номер клетки 2 фигуры по горизонтали целым числом от 1 до 8 = '))
        if m > 8 or m < 1 or m % 1 > 0:
            print('Ошибка ввода!')
            logger.error('m = ' + str(m))
            m = 0
    except ValueError:
        print('Ошибка ввода!')
        logger.error('m = ' + str(m))
logger.info('m = ' + str(m))

while n == 0:
    try:
        n = int(input('Введите номер клетки 2 фигуры по вертикали целым числом от 1 до 8 = '))
        if n > 8 or n < 1 or n % 1 > 0:
            print('Ошибка ввода!')
            logger.error('n = ' + str(n))
            n = 0
    except ValueError:
        print('Ошибка ввода!')
        logger.error('n = ' + str(n))
logger.info('n = ' + str(n))

#ответ на вопрос а
if (k + l) % 2 == 0:
    color1 = 0
else:
    color1 = 1
if (m + n) % 2 == 0:
    color2 = 0
else:
    color2 = 1

if color2 == color1:
    answera = 'Фигуры находятся на клетках одинакового цвета'
else:
    answera = 'Фигуры находятся на клетках разных цветов'
logger.info('answera = ' + str(answera))
print('Ответ на вопрос a -', answera, end="\n\n")

#создание шахматного поля
A = []
for i in range(8, 0, -1):
    b = []
    if i % 2 == 0:
        for j in range(8, 0, -1):
            if j % 2 == 0:
                b.append('#')
            else:
                b.append('_')
        A.append(b)
    else:
        for j in range(8, 0, -1):
            if j % 2 == 0:
                b.append('_')
            else:
                b.append('#')
        A.append(b)

#присвоение символов фигурам и постановка на шахматное поле
if figure1 == 'ферзь':
    figure1 = '♛'
if figure1 == 'ладья':
    figure1 = '♜'
if figure1 == 'слон':
    figure1 = '♝'
if figure1 == 'конь':
    figure1 = '♞'

l = abs(l - 9)
A[l - 1][k - 1] = figure1

if figure2 == 'ферзь':
    figure2 = '♕'
if figure2 == 'ладья':
    figure2 = '♖'
if figure2 == 'слон':
    figure2 = '♗'
if figure2 == 'конь':
    figure2 = '♘'

n = abs(n - 9)
A[n - 1][m - 1] = figure2

print(*A, sep="\n", end="\n\n")

#ответ на вопрос б
#ферзь
if figure1 == '♛':
    if k == m or l == n:
        answerb = 'Угрожает'
    elif abs(n - l) == abs(m - k):
        answerb = 'Угрожает'
    else:
        answerb = 'Не угрожает'

#ладья
if figure1 == '♜':
    if k == m or l == n:
        answerb = 'Угрожает'
    else:
        answerb = 'Не угрожает'

#слон
if figure1 == '♝':
    if answera == 'Фигуры находятся на клетках разных цветов':
        answerb = 'Цвет поля слона не совпадает с цветом 2й фигуры, поэтому попасть на поле 2й фигуры невозможно.'
    else:
        if abs(n - l) == abs(m - k):
            answerb = 'Угрожает'
        else:
            answerb = 'Не угрожает'

#конь
if figure1 == '♞':
    if abs(n - l) + abs(m - k) == 3:
        answerb = 'Угрожает'
    else:
        answerb = 'Не угрожает'
logger.info('answerb = ' + str(answerb))
print('Ответ на вопрос б -', answerb, end="\n\n")

#ответ на вопрос в
if (figure1 == '♛' or figure1 == '♜') and answerb == 'Не угрожает':
    if A[l - 1][k] == '#':
        A[l - 1][k - 1] = '_'
    else:
        A[l - 1][k - 1] = '#'

    l = n
elif figure1 == '♝':
    if answera == 'Фигуры находятся на клетках разных цветов':
        answerc = answerb
    else:
        if A[l - 1][k] == '#':
            A[l - 1][k - 1] = '_'
        else:
            A[l - 1][k - 1] = '#'

        if n < l:
            if m > k:
                while abs(l - n) != abs(k - m):
                    l -= 1
                    k += 1
            elif m < k:
                while abs(l - n) != abs(k - m):
                    l -= 1
                    k -= 1
        if n < l and m == k:
            if m >= 5:
                while abs(l - n) != abs(k - m):
                    l -= 1
                    k -= 1
            else:
                while abs(l - n) != abs(k - m):
                    l -= 1
                    k += 1
        if n > l:
            if m > k:
                while abs(l - n) != abs(k - m):
                    l += 1
                    k += 1
            elif m < k:
                while abs(l - n) != abs(k - m):
                    l += 1
                    k -= 1
        if n > l and m == k:
            if m >= 5:
                while abs(l - n) != abs(k - m):
                    l += 1
                    k -= 1
            else:
                while abs(l - n) != abs(k - m):
                    l += 1
                    k += 1
        if n == l:
            if m > k:
                if n >= 5:
                    while abs(l - n) != abs(k - m):
                        l -= 1
                        k += 1
                else:
                    while abs(l - n) != abs(k - m):
                        l += 1
                        k += 1
            if m < k:
                if n >= 5:
                    while abs(l - n) != abs(k - m):
                        l -= 1
                        k += 1
                else:
                    while abs(l - n) != abs(k - m):
                        l += 1
                        k += 1
elif figure1 == '♞' and answerb == 'Не угрожает':
    answerc = 'Ответ на данный вопрос не предусмотрен'
if answerb == 'Угрожает':
    answerc = 'С поля фигуры 1 можно попасть на поле фигуры 2.'
elif answerb == 'Цвет поля слона не совпадает с цветом 2й фигуры, поэтому попасть на поле 2й фигуры невозможно.':
    ancwerc = answerb
else:
    answerc = 'За 1 ход не выйдет. В 1 ход переместить в (' + str(k) + ',' + str(
        abs(l - 9)) + '), 2 ходом попадаем на поле 2й фигуры.'
logger.info('answerc = ' + str(answerc))
A[l - 1][k - 1] = figure1
print(*A, sep="\n", end="\n\n")
print('Ответ на вопрос в -', answerc)
