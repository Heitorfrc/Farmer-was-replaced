# projeto em andamento do cactus

# set_world_size(4) # ainda falta desbloquear
clear()

# arar o terreno
def arar() :
	x = 0
	for i in range (5) :
		while(x < 5) :
			if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin :
				harvest()
			if get_ground_type() != Grounds.Soil :
				till()
			move(North)
			x += 1
		x = 0
		move(South)
		move(South)
		move(South)
		move(South)
		move(South)
		if get_pos_x() < 4 :
			move(East)
		
arar()

move(West)
move(West)
move(West)
move(West)

while(True) :
	for i in range(5) :
	
		a1 = False
		b1 = False
		c1 = False
		d1 = False
	
# colher		
		if can_harvest() :
			if get_entity_type() == Entities.Cactus :
				if get_pos_y() < 3 :
					if measure() > measure (North) :
						swap(North)
						a1 = False
					else :
						a1 = True
				else :
					if measure() < measure (South) :
						swap(South)
						b1 = False
					else :
						b1 = True
				if get_pos_x() < 3 :
					if measure() > measure (East) :
						swap(East)
						c1 = False
					else :
						c1 = True
				else :
					if measure() < measure (West) :
						swap(West)
						d1 = False
					else :
						d1 = True 
			if get_pos_x() == 4 and get_pos_y() == 4 and a1 == True and b1 == True and c1 == True and d1 == True :
				harvest()

# plantar
		plant(Entities.Cactus)
		
		move(North)
	
	move(South)
	move(South)
	move(South)
	move(South)
	move(South)
	if get_pos_x() < 4 :
		move(East)
	else :
		move(West)
		move(West)
		move(West)
		move(West)
		
