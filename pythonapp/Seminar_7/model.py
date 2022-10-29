def calc(text, log):
    try:
        return eval(text)
    except  SyntaxError:
        log.error(f'Синтакситеская ошибка {text}')
        return 'Неверная формула'

# дополнительная функция
def conver(kg, log):
    try:
        return int(kg) * 1000
    except ValueError:
        log.error(f'При конвертации {kg} в граммах возникла ошибка приведения к INT')
        return 'Nan'

