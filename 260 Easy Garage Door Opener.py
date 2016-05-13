
def garageDoor(input):
    states = ['CLOSED', 'OPEN', 'OPENING', 'CLOSING', 'STOPPED_WHILE_CLOSING', 'STOPPED_WHILE_OPENING']

    fsm = [[2,0],
           [3,1],
           [5,1],
           [4,0],
           [2,4],
           [3,5]]

    currentState = 0
    print('Door:',states[currentState])
    for i in input.split():
        s = 'Button clicked.'
        if i == 'button_clicked':
            currentState = fsm[currentState][0]
        else:
            s = 'Cycle complete'
            currentState = fsm[currentState][1]
        print('>',s)
        print('Door:',states[currentState])

input = 'button_clicked cycle_complete button_clicked button_clicked button_clicked button_clicked button_clicked cycle_complete'
garageDoor(input)
