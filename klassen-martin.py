class Spieler():
	def __init__(self, name, staerke):
    		self.staerke = staerke
    
                   
mueller = Spieler("mueller", 5)
kimmich = Spiler("kimmich", 5)

def angriff(angreifer, verteidiger):
	if verteidiger.staerke % 2 == 1:
		ballbesitz = -1
	elif vertiediger.staerke % 2 == 0:
		ballbesitz = 0
	elif angreifer.staerke > verteidiger.staerke:
		ballbesitz = 1
	else:
		ballbesitz = 2
            
	print(ballbesitz)