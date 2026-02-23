# projeto em andamento

# perfumarias
change_hat(Hats.Pumpkin_Hat)
pet_the_piggy()
do_a_flip()


# arar o terreno
def arar() :
	x = 0
	for i in range (get_world_size()) :
		while(x < get_world_size()) :
			if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin :
				harvest()
			if get_ground_type() != Grounds.Soil :
				till()
			move(North)
			x += 1
		x = 0
		move(East)

# aguar as plantas		
def aguar() :
	if get_water() < 0.5 and num_items(Items.Water) > 0 :
			use_item(Items.Water)

# fertilizar a terra
def fertilizar() :
	if get_entity_type() == None and num_items(Items.Fertilizer) > 0 :
		use_item(Items.Fertilizer)

# plantar cenouras		
def plantar_cenoura() :
	if num_items(Items.Hay) >= 32 and num_items(Items.Wood) > 32 :
		plant(Entities.Carrot)
		
# plantar aboboras
def plantar_aboboras() :
	if num_items(Items.Carrot) >= 16 :
		plant(Entities.Pumpkin)

# plantar arvore e arbusto
def plantar_madeiras() :
	# quando x for ímpar
	if (get_pos_x() + 1) % 2 == 0 :
		# quando y for ímpar
		if (get_pos_y() + 1) % 2 == 0 :
			plant(Entities.Bush)
		else: 
			plant(Entities.Tree)
		# quando x for par
	else:
		# quando y for par
		if (get_pos_y() + 1) % 2 == 1 :
			plant(Entities.Bush)
		else: 
			plant(Entities.Tree)


# valores para a abobora gigante	
a = 0
medida_abobora = 10
area_abobora = medida_abobora * medida_abobora

# valores para a plantacao de cactus
cac = False
medida_cactus = 5
posicao_inicial_x_cactus = 0
posicao_inicial_y_cactus = 11

# quando emular uma fazendo nova tira o # antes de clear() e de arar()
clear()
arar() 

# plantar e colher
while(True) :
	for i in range(get_world_size()) :
		
		# colher
		if get_pos_x() == 0 and get_pos_y() == 0 :
			a = 0   # posiciao inicial da abobora gigante
			
		if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin :
			if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Cactus :
				harvest()
			if get_entity_type() == Entities.Pumpkin :
				a += 1
			if a == area_abobora:
				harvest()
			if get_pos_x() == posicao_inicial_x_cactus + medida_cactus - 1 and get_pos_y() == posicao_inicial_y_cactus + medida_cactus - 1 and cac == True :
				harvest()
		
		# plantar
		fertilizar()
		aguar()
		
		if get_pos_x() < (10*get_world_size()/16) :
			
			if (get_pos_y() < medida_abobora and get_pos_x() < medida_abobora) :
				plantar_aboboras()
						
			elif get_pos_x() >= posicao_inicial_x_cactus and get_pos_x() < posicao_inicial_x_cactus + medida_cactus and get_pos_y() >= posicao_inicial_y_cactus and get_pos_y() < posicao_inicial_y_cactus + medida_cactus :
				
				if get_entity_type() == Entities.Cactus :
					if get_pos_x() == posicao_inicial_x_cactus and get_pos_y() == posicao_inicial_y_cactus :
						cac = True
					if get_pos_y() < posicao_inicial_y_cactus + medida_cactus - 2 :
						if measure() > measure (North) :
							swap(North)
							cac = False
					if get_pos_y() == posicao_inicial_y_cactus + medida_cactus - 1 :
						if measure() < measure(South) :
							swap(South)
							cac = False
					if get_pos_x() < posicao_inicial_x_cactus + medida_cactus - 2 :
						if measure() > measure (East) :
							swap(East)
							cac = False
					if get_pos_x() == posicao_inicial_x_cactus + medida_cactus - 1 :
						if measure() < measure (West) :
							swap(West)
							cac = False
				
				plant(Entities.Cactus)
				
			else :
				plantar_madeiras()
			
		elif get_pos_x() < (13*get_world_size()/16) : 
			plant(Entities.Grass)
			
		else:
			plantar_cenoura()
			
		move(North)
		
	move(East)
	
	
	
