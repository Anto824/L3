def message_imc(imc):
    if imc<16.5:
        msg = 'dénutrition ou famine'
    elif imc<18.5:
        msg = 'maigreur'
    elif imc<25:
        msg = 'corpulence normale'
    elif imc<30:
        msg = 'surpoids'
    elif imc<35:
        msg = 'obésité modérée'
    elif imc<40:
        msg = 'obésité sévère'
    else:
        msg = 'obésité morbide'
    return msg

def test_imc(tab:list):
    for i in tab:
        print(message_imc(i))



tab = [12,45,32,29,25,23]
test_imc(tab)