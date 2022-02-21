import math
import CoolProp
import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI , get_global_param_string

#Input Data

T_max = 590 + 273.15                    # K
P_max = 15e6                            # Pa
P_percentage = 0.2                      #Pa   #The pressure at inlet of LPT is considered this
                                              #percentage of the HPT
eta_turb = .90                          #Turbine efficiency
eta_pump = .90                          #Pump efficiency
T_sat = 39+273.15                       #K      #Temperature of Condenser
P_sat = 7e3                             #Pa     #Saturation pressure at the Temperature of Condenser
P_regen = 0.15e6                        #Pa     #Pressure at Regenerator which is set
T_surr = 25+273.15                      #K      # Sourrounding Temperature
m_water = 1
    #Flue gas property
Cp_gas = 1.1058                         #Initial State of flue gas as reference state
T_gas_in = 1500+273.15
T_gas_out = 400+273.15
P_gas_out = 101e3
P_gas_in = 102e3
h_gas_in = 0
s_gas_in = 0
k = 1.35
    #Cooling water
P_cold_in = 101e3
T_cold_in = 25 +273.15
T_cold_out = 39 +273.15
P_cold_out = 101e3
#Cycle Analysis with optimized parameter

# State 1
P_1 = P_max
T_1 = T_max
h_1 = PropsSI('H', 'P', P_1, 'T', T_1, 'Water')
s_1 = PropsSI('S', 'P', P_1, 'T', T_1, 'Water')
print('Properties of state 1: h_1 =', h_1 / 1000, 'kJ/kg , s_1 = ', s_1 / 1000, 'kJ/kg K and T_1 = ',T_1-273.15,'C')
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
print('Properties of state 2: h_2 =', h_2 / 1000, 'kJ/kg , s_2 = ', s_2 / 1000, 'kj/kg K and T_2 = ',T_2-273.15,'C')
# State 3
P_3 = P_int
T_3 = T_max
h_3 = PropsSI('H', 'P', P_3, 'T', T_3, 'Water')
s_3 = PropsSI('S', 'P', P_3, 'T', T_3, 'Water')
print('Properties of state 3: h_3 =', h_3 / 1000, 'kJ/kg, s_3 = ', s_3 / 1000, 'kj/kg K and T_3 = ',T_3-273.15,'C')
# State 4
P_4s = P_regen
s_4s = s_3
h_4s = PropsSI('H', 'P', P_4s, 'S', s_4s, 'Water')
# eta_turb = (h_3 -h_4)/(h_3-h_4s)
h_4 = h_3 - (eta_turb * (h_3 - h_4s))
P_4 = P_regen
T_4 = PropsSI('T', 'P', P_4, 'H', h_4, 'Water')
s_4 = PropsSI('S', 'P', P_4, 'H', h_4, 'Water')
print('Properties of state 4: h_4 =', h_4 / 1000, 'kJ/kg , s_4 = ', s_4 / 1000, 'kj/kg K and T_4 = ',T_4-273.15,'C')
# State 5
P_5s = P_sat
s_5s = s_3
h_5s = PropsSI('H', 'P', P_5s, 'S', s_5s, 'Water')
# eta_turb = (h_3 -h_5)/(h_3-h_5s)
h_5 = h_3 - (eta_turb * (h_3 - h_5s))
P_5 = P_sat
T_5 = PropsSI('T', 'P', P_5, 'H', h_5, 'Water')
s_5 = PropsSI('S', 'P', P_5, 'H', h_5, 'Water')
print('Properties of state 5: h_5 =', h_5 / 1000, 'kJ/kg , s_5 = ', s_5 / 1000, 'kj/kg K and T_5 = ',T_5-273.15,'C')
# State 6
P_6 = P_sat
q_6 = 0  # Quality
h_6 = PropsSI('H', 'P', P_6, 'Q', q_6, 'Water')
s_6 = PropsSI('S', 'P', P_6, 'Q', q_6, 'Water')
T_6 = PropsSI('T', 'P', P_6, 'Q', q_6, 'Water')
print('Properties of state 6: h_6 =', h_6 / 1000, 'kJ/kg ,s_6 = ', s_6 / 1000, 'kj/kg K and T_6 = ',T_6-273.15,'C')
# State 7
P_7s = P_regen
s_7s = s_6
h_7s = PropsSI('H', 'P', P_7s, 'S', s_7s, 'Water')
# eta_pump = (h_7s -h_6)/(h_7-h_6)
h_7 = h_6 + (h_7s - h_6) / eta_pump
P_7 = P_regen
T_7 = PropsSI('T', 'P', P_7, 'H', h_7, 'Water')
s_7 = PropsSI('S', 'P', P_7, 'H', h_7, 'Water')
print('Properties of state 7: h_7 =', h_7 / 1000, 'kJ/kg, s_7 = ', s_7 / 1000, 'kj/kg K and T_7 = ',T_7-273.15,'C')
# State 8
P_8 = P_regen
q_8 = 0  # Quality
h_8 = PropsSI('H', 'P', P_8, 'Q', q_8, 'Water')
s_8 = PropsSI('S', 'P', P_8, 'Q', q_8, 'Water')
T_8 = PropsSI('T', 'P', P_8, 'Q', q_8, 'Water')

print('Properties of state 8: h_8 =', h_8 / 1000, 'kJ/kg, s_8 = ', s_8 / 1000, 'kj/kg K and T_8 = ',T_8-273.15,'C')
# State 9
P_9s = P_max
s_9s = s_8
h_9s = PropsSI('H', 'P', P_9s, 'S', s_9s, 'Water')
# eta_pump = (h_9s -h_8)/(h_9-h_8)
h_9 = h_8 + (h_9s - h_8) / eta_pump
P_9 = P_regen
T_9 = PropsSI('T', 'P', P_9, 'H', h_9, 'Water')
s_9 = PropsSI('S', 'P', P_9, 'H', h_9, 'Water')
print('Properties of state 9: h_9 =', h_9 / 1000, 'kJ/kg, s_9 = ', s_9 / 1000, 'kj/kg K and T_9 = ',T_9-273.15,'C','\n')

x = (h_8 - h_7) / (h_4 - h_7)
print('Mass fraction feeding regenerator X = ', x,'\n')

w_hpt = (h_1 - h_2)
print('HPT Specific Work w = ', w_hpt / 1000,'kJ/kg')
w_lpt = (h_3 - x * h_4 - (1 - x) * h_5)
print('LPT Specific Work w = ', w_lpt / 1000,'kJ/kg')
w_net = w_hpt + w_lpt
print('Turbine Specific Work w = ', w_net / 1000,'kJ/kg\n')

q_regen = h_8 - h_7
print('Specific Heat transfer in regenerator = ', q_regen / 1000,'kJ/kg')

q_in = (h_1 - h_9) + (h_3 - h_2)
print('Specific Heat input from boiler = ', q_in / 1000,'kJ/kg')

q_out = (1-x) * (h_5-h_6)
print('Specific Heat outgoing from condenser = ', q_out / 1000,'kJ/kg')

w_pumpI = (1-x) * (h_6-h_7)
print('PUMP I Specific Work input = ', w_pumpI / 1000,'kJ/kg')

w_pumpII = (h_8-h_9)
print('PUMP II Specific Work input = ', w_pumpII / 1000,'kJ/kg')

eta = (w_net) / (q_in)
print('1st law Efficiency = ', eta * 100, '%\n')

E_hpt_avail = (h_1-h_2)-T_surr*(s_1-s_2)
print('E_hpt_avail = ', E_hpt_avail/1000, 'kJ/kg')
E_hpt_dest = -T_surr*(s_1-s_2)
print('E_hpt_dest = ', E_hpt_dest/1000, 'kJ/kg')

E_lpt_avail = (h_3-x*h_4-(1-x)*h_5)-T_surr*((s_3-x*s_4-(1-x)*s_5))
print('E_lpt_avail = ', E_lpt_avail/1000, 'kJ/kg')
E_lpt_dest = -T_surr*((s_3-x*s_4-(1-x)*s_5))
print('E_lpt_dest = ', E_lpt_dest/1000, 'kJ/kg')

E_regen_avail =  -T_surr*(x*s_4-(1-x)*s_7-s_8)+(1-x)*((h_8-h_7)-T_surr*(s_8-s_7))
print('E_regen_avail = ', E_regen_avail/1000, 'kJ/kg')
E_regen_dest =  -T_surr*(x*s_4-(1-x)*s_7-s_8)#+(1-x)*((h_8-h_7)-T_surr*(s_8-s_7))
print('E_regen_dest = ', E_regen_dest/1000, 'kJ/kg')

h_cold_in = PropsSI('H', 'P', P_cold_in, 'T', T_cold_in, 'Water')
print('h cold_in = ',h_cold_in/1000)
h_cold_out = PropsSI('H', 'P', P_cold_out, 'T', T_cold_out, 'Water')
print('h cold_out = ',h_cold_out/1000)
s_cold_in = PropsSI('S', 'P', P_cold_in, 'T', T_cold_in, 'Water')
print('s cold_in = ',s_cold_in/1000)
s_cold_out = PropsSI('S', 'P', P_cold_out, 'T', T_cold_out, 'Water')
print('s cold_out = ',s_cold_out/1000)
m_cold = q_out/(h_cold_out- h_cold_in)
print('Cold water mass flow rate, m_cold = ', m_cold/1000, 'kg/s')
E_cond_avail = m_cold*((h_cold_out-h_cold_in)-T_surr*(s_cold_out-s_cold_in))
print('E_cond_available = ', E_cond_avail/1000, 'kJ/kg')
E_cond_dest =  -T_surr*((1-x)*(s_5-s_6)+m_cold*(s_cold_in-s_cold_out))
print('E_cond_destruction = ', E_cond_dest/1000, 'kJ/kg')

m_gas = q_in/(Cp_gas*(T_gas_in-T_gas_out))
a = math.log(T_gas_out/T_gas_in)
b = math.log(P_gas_out/P_gas_in)
s_gas_out = Cp_gas*(a - (((k-1)/k) *b))
print('s =',s_gas_out)
h_gas_out = Cp_gas*(T_gas_out-T_gas_in)
print('h =',h_gas_out)
print('Flue gas mass flow rate, m_gas = ', m_gas/1000, 'kg/s')
E_boiler_avail = m_gas*((h_gas_in-h_gas_out)-T_surr*(s_gas_in-s_gas_out))
print('E_boiler_available = ', E_boiler_avail/1000, 'kJ/kg')
E_boiler_dest = -T_surr*((s_9-s_1)+(s_2-s_3)+m_gas*(s_gas_in-s_gas_out))
print('E_boiler_destruction = ', E_boiler_dest/1000, 'kJ/kg')


E_pumpI_avail = (1-x)*((h_6-h_7)-T_surr*(s_6-s_7))
print('E_pumpI_available = ', E_pumpI_avail/1000, 'kJ/kg')
E_pumpI_dest = -(1-x)*(T_surr*(s_6-s_7))
print('E_pumpI_dest = ', E_pumpI_dest/1000, 'kJ/kg')
E_pumpII = ((h_8-h_9)-T_surr*(s_8-s_9))
print('E_pumpII_available = ', E_pumpII/1000, 'kJ/kg')
E_pumpII_dest = (-T_surr*(s_8-s_9))
print('E_pumpII_dest = ', E_pumpII_dest/1000, 'kJ/kg')
#a_gas_in = h_gas_in - T_surr * s_gas_in
#print('a_gas_in = ', a_gas_in/1000, 'kJ/kg')
#a_gas_out = Cp_gas*((T_gas_out-T_gas_in)-T_surr*a - ((k-1)/k) *b) #a_gas out = h_gas_out - T_sutt*s_gas_out
#print('a_gas_out = ', a_gas_out, 'kJ/kg')
#RED = m_gas*(a_gas_in-a_gas_out)
#print('Rate of exergy decrease of the system',RED/1000,'KW')

eta_II= w_net/E_boiler_avail
print('2nd law Efficiency = ', eta_II * 100, '%')

