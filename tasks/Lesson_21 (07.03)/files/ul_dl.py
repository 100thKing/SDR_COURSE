import numpy as np

U_bs = 7500 # м/с
U_ue = 2500 # м/c
F_dl = 15e9 # Гц
F_ul = 10e9 # Гц

coord_bs = np.array([0, 0, 5e5]) # м
coord_ue = np.array([0, 0, 1e4]) # м

dis_bu = np.array(coord_bs - coord_ue)
print('dis_bu',dis_bu)

U_ue_rx = U_ue*dis_bu[2] / (np.sum(dis_bu**2) ** 0.5)
U_bs_rx = U_bs*dis_bu[2] / (np.sum(dis_bu**2) ** 0.5)
print('V_ue_rx',U_ue_rx)
print('V_bs_rx',U_bs_rx)

dl_ue = F_dl * (1+(U_ue_rx + U_bs_rx) / 3e8)
ul_ue = F_ul * (1-(U_ue_rx + U_bs_rx) / 3e8)
print(f'F_dl_ue = {round (dl_ue,1): }') # ГЦ
print(f'F_ul_ue = {round (ul_ue,1): }') # Гц
