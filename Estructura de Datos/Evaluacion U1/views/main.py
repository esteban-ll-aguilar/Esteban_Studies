#DAO
'''
Patron de diseno DAO PIS

Dao adapter
* create
* list
* update (change, stafe)
* search

'''

import sys
from time import time
sys.path.append('../')
from controls.parqueDaoControl import ParqueDaoControl

#rqq = RetencionListDaoControl(size=25)
pdc = ParqueDaoControl()

try:
    pdc._parque._nombre = 'hoalaaaa'
    pdc._parque._direccion = 'av.Loja'
    pdc._parque._ubicacionGPS ='ddfsdfsdfsdfsdfsd'
    pdc.save
    
except Exception as e:
    print(e)
