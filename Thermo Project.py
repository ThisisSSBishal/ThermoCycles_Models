import CoolProp
import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI , get_global_param_string

#Input Data
P_list = [10e6,11e6,12e6,13e6,14e6,15e6]          #Pa     #For Maximum pressure
P_percentage = 0.2                    #Pa   #The pressure at inlet of LPT is considered this
                                            #percentage of the HPT
T_list = [400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600]   #Boiler Temperature
eta_turb = .90                        #Turbine efficiency
eta_pump = .90                        #Pump efficiency
T_sat = 39+273.15                     #K      #Temperature of Condenser
P_sat = 7e3                           #Pa     #Saturation pressure at the Temperature of Condenser
P_regen = 0.15e6                      #Pa     #Pressure at Regenerator which is set
T_surr = 25+273.15                    #K      # Surrounding Temperature

#Cycle Optimisation
for i in T_list:
    for j in P_list:
        T_max = i+273.15               #K
        P_max = j                      #Pa
        # State 1
        P_1 = P_max
        T_1 = T_max
        h_1 = PropsSI('H', 'P', P_1, 'T', T_1, 'Water')
        s_1 = PropsSI('S', 'P', P_1, 'T', T_1, 'Water')
        #print('Properties of state 1: h_1 =', h_1 / 1000, 'kJ/kg and s_1 = ', s_1 / 1000, 'kJ/kg K')
        # State 2
        P_int = P_max * P_percentage
        P_2s = P_int
        s_2s = s_1
        h_2s = PropsSI('H', 'P', P_2s, 'S', s_2s, 'Water')
        # eta_turb = (h_1 -h_2)/(h_1-h_2s)
        h_2 = h_1 - (eta_turb * (h_1 - h_2s))
        P_2 = P_int
        T_2 = PropsSI('T', 'P', P_2, 'H', h_2, 'Water')
        s_2 = PropsSI('S', 'P', P_2, 'H', h_2, 'Water')
        #print('Properties of state 2: h_2 =', h_2 / 1000, 'kJ/kg and s_2 = ', s_2 / 1000, 'kj/kg K')
        # State 3
        P_3 = P_int
        T_3 = T_max
        h_3 = PropsSI('H', 'P', P_3, 'T', T_3, 'Water')
        s_3 = PropsSI('S', 'P', P_3, 'T', T_3, 'Water')
        #print('Properties of state 3: h_3 =', h_3 / 1000, 'kJ/kg and s_3 = ', s_3 / 1000, 'kj/kg K')
        # State 4
        P_4s = P_regen
        s_4s = s_3
        h_4s = PropsSI('H', 'P', P_4s, 'S', s_4s, 'Water')
        # eta_turb = (h_3 -h_4)/(h_3-h_4s)
        h_4 = h_3 - (eta_turb * (h_3 - h_4s))
        P_4 = P_regen
        T_4 = PropsSI('T', 'P', P_4, 'H', h_4, 'Water')
        s_4 = PropsSI('S', 'P', P_4, 'H', h_4, 'Water')
        #print('Properties of state 4: h_4 =', h_4 / 1000, 'kJ/kg and s_4 = ', s_4 / 1000, 'kj/kg K')
        # State 5
        P_5s = P_sat
        s_5s = s_3
        h_5s = PropsSI('H', 'P', P_5s, 'S', s_5s, 'Water')
        # eta_turb = (h_3 -h_5)/(h_3-h_5s)
        h_5 = h_3 - (eta_turb * (h_3 - h_5s))
        P_5 = P_sat
        T_5 = PropsSI('T', 'P', P_5, 'H', h_5, 'Water')
        s_5 = PropsSI('S', 'P', P_5, 'H', h_5, 'Water')
        #print('Properties of state 5: h_5 =', h_5 / 1000, 'kJ/kg and s_5 = ', s_5 / 1000, 'kj/kg K')
        # State 6
        P_6 = P_sat
        q_6 = 0  # Quality
        h_6 = PropsSI('H', 'P', P_6, 'Q', q_6, 'Water')
        s_6 = PropsSI('S', 'P', P_6, 'Q', q_6, 'Water')
        #print('Properties of state 6: h_6 =', h_6 / 1000, 'kJ/kg and s_6 = ', s_6 / 1000, 'kj/kg K')
        # State 7
        P_7s = P_regen
        s_7s = s_6
        h_7s = PropsSI('H', 'P', P_7s, 'S', s_7s, 'Water')
        # eta_pump = (h_7s -h_6)/(h_7-h_6)
        h_7 = h_6 + (h_7s - h_6) / eta_pump
        P_7 = P_regen
        T_7 = PropsSI('T', 'P', P_7, 'H', h_7, 'Water')
        s_7 = PropsSI('S', 'P', P_7, 'H', h_7, 'Water')
        #print('Properties of state 7: h_7 =', h_7 / 1000, 'kJ/kg and s_7 = ', s_7 / 1000, 'kj/kg K')
        # State 8
        P_8 = P_regen
        q_8 = 0  # Quality
        h_8 = PropsSI('H', 'P', P_8, 'Q', q_8, 'Water')
        s_8 = PropsSI('S', 'P', P_8, 'Q', q_8, 'Water')
        #print('Properties of state 8: h_8 =', h_8 / 1000, 'kJ/kg and s_8 = ', s_8 / 1000, 'kj/kg K')
        # State 9
        P_9s = P_max
        s_9s = s_8
        h_9s = PropsSI('H', 'P', P_9s, 'S', s_9s, 'Water')
        # eta_pump = (h_9s -h_8)/(h_9-h_8)
        h_9 = h_8 + (h_9s - h_8) / eta_pump
        P_9 = P_regen
        T_9 = PropsSI('T', 'P', P_9, 'H', h_9, 'Water')
        s_9 = PropsSI('S', 'P', P_9, 'H', h_9, 'Water')
        #print('Properties of state 9: h_9 =', h_9 / 1000, 'kJ/kg and s_9 = ', s_9 / 1000, 'kj/kg K')

        x = (h_8 - h_7) / (h_4 - h_7)
        #print('X = ', x)

        w_net = (h_1 - h_2) + (h_3 - x * h_4 - (1 - x) * h_5)
        #print('W = ', w_net / 1000)
        q_in = (h_1 - h_9) + (h_3 - h_2)
        #print('Q = ', q_in / 1000)
        eta = (w_net) / (q_in)
        #print('Efficiency = ', eta * 100, '%')
        print(i,j/1e6,eta)
