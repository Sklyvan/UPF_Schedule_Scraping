def displayNumericMenu(menuOptions, indexZero=False):
    numericMenu, optionNumber = [], 1 - indexZero
    for menuOption in menuOptions:
        print(f'{optionNumber}. {menuOption}')
        optionNumber += 1