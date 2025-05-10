#Legenda:   to -> takeoff, decolagem
#           ld -> landing, pouso
#           zf -> zero fuel, sem combustível

#=======================
#DEFINIÇÃO DE FUNÇÕES ==
#=======================
# Ainda vai receber números mais realísticos, mas o que importa é que será uma função!
def max_and_min_cg_to(weight_to):
    max = 34
    min = 7
    if(weight_to>62500):
        return [-999,-998]
    if(weight_to<300000):
        return [-999,-998]
    return [min, max]

# Ainda vai receber números mais realísticos, mas o que importa é que será uma função!
def max_and_min_cg_ld(weight_ld):
    max = 34
    min = 7
    if(weight_ld>54000):
        return [-999,-998]
    if(weight_ld<300000):
        return [-999,-998]
    return [min, max]

# Ainda vai receber números mais realísticos, mas o que importa é que será uma função!
def max_and_min_cg_zf(weight_zf):
    max = 34
    min = 7
    if(weight_zf>52000):
        return [-999,-998]
    if(weight_zf<300000):
        return [-999,-998]
    return [min, max]

# Ainda vai receber números mais realísticos, mas o que importa é que será uma função!
def arm_fuel(total_fuel_weight):
    full_tank_weight = 18000
    cg_full_tank_weight = 18
    cg_tank_empty = 25
    return cg_tank_empty+(cg_full_tank_weight-cg_tank_empty)*(total_fuel_weight/full_tank_weight)

# Ainda falta implementar, mas o que importa é que será uma função. Seu objetivo será testar se o resultado do Gurobi realmente é feasible
def is_solution_realy_feasible(x_a_1,x_a_2,x_a_3,x_c_1,x_c_2,x_c_3,x_i_1,x_i_2,x_i_3,x_aft_cargo,x_fwd_cargo):
    return false

#===================================
#PARÂMETROS DO PROBLEMA/ENUNCIADO ==
#===================================
# Ainda vai receber números mais realísticos, mas o que importa é que serão dados fixos!
bow = 30000 #Basic Operational Weight - kg
arm_bow = 26 #Braço do bow - m
fuel_trip = 12000 #Fuel Trip - kg
fuel_reserve = 1500 #Fuel Reserve - kg
w_avg_a = 90 #Peso médio de um adulto - kg
w_avg_c = 40 #Peso médio de uma criança - kg
w_avg_i = 10 #Peso médio de um bebê - kg
w_lug = 32 #Peso médio de uma mala - kg
arm_cabin_1 = 15 #Braço do cabine 1 - m
arm_cabin_2 = 25 #Braço do cabine 2 - m
arm_cabin_3 = 35 #Braço do cabine 3 - m
arm_aft_cargo = 10 #Braço do porão dianteiro - m
arm_fwd_cargo = 30 #Braço do porão traseiro - m
n_a = 100 #Número de adultos no voo
n_c = 10 #Número de crianças no voo
n_i = 2 #Número de bebês no voo
m_1 = 30 #Número máximo de assentos na cabine 1
m_2 = 50 #Número máximo de assentos na cabine 2
m_3 = 50 #Número máximo de assentos na cabine 3
m_aft_cargo = 2500 #Peso máximo limite estrutural cargo dianteiro - kg
m_fwd_cargo = 3000 #Peso máximo limite estrutural cargo traseiro - kg

#=================================================
#VARIÁVEIS DO MODELO, A SER BUSCADO PELO GUROBI ==
#=================================================
x_a_1 = 10 #Número de adultos sentados na cabine 1
x_a_2 = 10 #Número de adultos sentados na cabine 2
x_a_3 = 10 #Número de adultos sentados na cabine 3
x_c_1 = 5 #Número de crianças sentados na cabine 1
x_c_2 = 0 #Número de crianças sentados na cabine 2
x_c_3 = 0 #Número de crianças sentados na cabine 3
x_i_1 = 1 #Número de bebês sentados na cabine 1
x_i_2 = 1 #Número de bebês sentados na cabine 2
x_i_3 = 1 #Número de bebês sentados na cabine 3
x_aft_cargo = 10 #Número de malas no porão dianteiro
x_fwd_cargo = 20 #Número de malas no porão traseiro

#==========================================================
#PARÂMETROS CALCULADOS A PARTIR DAS VARI[AVEIS DO MODELO ==
#==========================================================
weight_to = bow+fuel_trip+fuel_reserve+   x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i+       x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i   + x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i   +(x_aft_cargo+x_fwd_cargo)*w_lug
weight_ld = bow+fuel_reserve+   x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i+       x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i   + x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i   +(x_aft_cargo+x_fwd_cargo)*w_lug
weight_zf = bow+   x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i+       x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i   + x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i   +(x_aft_cargo+x_fwd_cargo)*w_lug

cg_to = (bow*arm_bow+(fuel_trip+fuel_reserve)*arm_fuel(fuel_trip+fuel_reserve)+(x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i)*arm_cabin_1+       (x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i)*arm_cabin_2     + (x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i)*arm_cabin_3    +    x_aft_cargo*w_lug*arm_aft_cargo + x_fwd_cargo*w_lug*arm_fwd_cargo )/weight_to
cg_ld = (bow*arm_bow+(fuel_reserve)*arm_fuel(fuel_reserve)+(x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i)*arm_cabin_1+       (x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i)*arm_cabin_2     + (x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i)*arm_cabin_3    +    x_aft_cargo*w_lug*arm_aft_cargo + x_fwd_cargo*w_lug*arm_fwd_cargo )/weight_ld
cg_zf = (bow*arm_bow+(x_a_1*w_avg_a+x_c_1*w_avg_c+x_i_1*w_avg_i)*arm_cabin_1+       (x_a_2*w_avg_a+x_c_2*w_avg_c+x_i_2*w_avg_i)*arm_cabin_2     + (x_a_3*w_avg_a+x_c_3*w_avg_c+x_i_3*w_avg_i)*arm_cabin_3    +    x_aft_cargo*w_lug*arm_aft_cargo + x_fwd_cargo*w_lug*arm_fwd_cargo )/weight_zf

[cg_to_max, cg_to_min] = max_and_min_cg_to(weight_to)
[cg_ld_max, cg_ld_min] = max_and_min_cg_ld(weight_ld)
[cg_zf_max, cg_zf_min] = max_and_min_cg_zf(weight_zf)


#========================
#FUNÇÃO MULTI-OBJETIVO ==
#========================
#maximize
f = (cg_to+cg_ld)/2


#=======================
#RESTRIÇÕES DO MODELO ==
#=======================
x_a_1+x_a_2+x_a_3=n_a
x_c_1+x_c_2+x_c_3=n_c
x_i_1+x_i_2+x_i_3=n_i

x_a_1+x_c_1<=m_1
x_a_2+x_c_2<=m_2
x_a_3+x_c_3<=m_3

x_a_1>=x_c_1+x_i_1
x_a_2>=x_c_2+x_i_2
x_a_3>=x_c_3+x_i_3

x_a_1 >=0 #E é inteira!
x_a_2 >=0 #E é inteira!
x_a_3 >=0 #E é inteira!
x_c_1 >=0 #E é inteira!
x_c_2 >=0 #E é inteira!
x_c_3 >=0 #E é inteira!
x_i_1 >=0 #E é inteira!
x_i_2 >=0 #E é inteira!
x_i_3 >=0 #E é inteira!
x_aft_cargo>=0 #E é inteira!
x_fwd_cargo>=0 #E é inteira!

x_aft_cargo+x_fwd_cargo = n_a+n_c

x_aft_cargo*w_lug <= m_aft_cargo
x_fwd_cargo*w_lug <= m_fwd_cargo

cg_to <= cg_to_max
cg_to >= cg_to_min

cg_ld <= cg_ld_max
cg_ld >= cg_ld_min

cg_zf <= cg_zf_max
cg_zf >= cg_zf_min

