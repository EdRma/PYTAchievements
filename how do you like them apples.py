import math

#Vervang de 0-en met de juiste berekeningen

trees               = 333                #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(0)       #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = 111                #hoeveel in de zon?

shadeOutputModifier = 80                 #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146                #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 116                #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 16,206             #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 25,752             #hoeveel appels geven alle schaduw bomen?
totalOutput         = 41,958             #hoeveel appels zijn er in totaal?

owners              = 4                  #met hoeveel mensen verdelen we de appels?

eatCount            = 0,5                #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 10,489             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 10,489             #hoeveel appels mag ik verkopen?

print(cut)