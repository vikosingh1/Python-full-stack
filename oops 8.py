#multiple Inheritance
class bat:
    batlen="3 feet"
    batbrand="SS"
    batweight="1.5 kg"
class ball:
    blen='150gm'
    bshap='sphere'
    bbrand='kookabura'
class ground:
    ground='dharmshala'
    gtype='green'
    gpitch='22-yard'
    cap=25000
class cricket(bat,ball,ground):
    player=22
    umpire='kumar dharmsena'

print(cricket.gpitch)
