# projeto em andamento do cactus

# iniciar o cactus
# set_world_size(5)
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

a1 = False

while(True) :
	for i in range(5) :
	
# colher		
		if can_harvest() :
			if get_entity_type() == Entities.Cactus :
				if get_pos_x() == 0 and get_pos_y() == 0 :
					a1 = True
				if get_pos_y() < 3 :
					if measure() > measure (North) :
						swap(North)
						a1 = False
				if get_pos_y() == 4 :
					if measure() < measure (South) :
						swap(South)
						a1 = False
				if get_pos_x() < 3 :
					if measure() > measure (East) :
						swap(East)
						a1 = False
				if get_pos_x() == 4 :
					if measure() < measure (West) :
						swap(West)
						a1 = False
			if get_pos_x() == 4 and get_pos_y() == 4 and a1 == True :
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

