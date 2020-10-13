from GUI import UI

def displayNumericMenu(menuOptions, indexZero=False):
    numericMenu, optionNumber = [], 1 - indexZero
    for menuOption in menuOptions:
        print(f'{optionNumber}. {menuOption}')
        optionNumber += 1

def updateQComboBoxOptions(QComboBox, Options):
    if QComboBox == 'CENTERS':
        UI.generateCentersNames_Box(5, ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'])