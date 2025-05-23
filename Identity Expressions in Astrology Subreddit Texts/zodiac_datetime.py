# zodiac_datetime.py

from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import FixedLocator, FixedFormatter

class ZodiacFormatter:
    """
    Formatter for x-axis ticks based on planeary ingress timestamps
    """
    
    def __init__(self, planet='Sun'):
        
        self.planet = planet
        
        z_labels = [
            'Aqu', 'Pis', 'Ari',
            'Tau', 'Gem', 'Can',
            'Leo', 'Vir', 'Lib',
            'Sco', 'Sag', 'Cap'
        ]
        
        z_ingress = {
            'Sun'    : 'Aqu', 'Moon'   : 'Cap',
            'Mercury': 'Aqu', 'Venus'  : 'Cap', 
            'Mars'   : 'Tau', 'Jupiter': 'Pis',
        }
        
        
        match planet:
            case 'Sun':
                self.ingresses = [
                    datetime(2021, 1,19,20,39), datetime(2021, 2,18,10,43),
                    datetime(2021, 3,20, 9,37), datetime(2021, 4,19,20,33),
                    datetime(2021, 5,20,19,37), datetime(2021, 6,21, 3,32),
                    datetime(2021, 7,22,14,26), datetime(2021, 8,22,21,34),
                    datetime(2021, 9,22,19,21), datetime(2021,10,23, 4,51),
                    datetime(2021,11,22, 2,33), datetime(2021,12,21,15,59)
                ]
                
            case 'Moon':
                self.ingresses = [
                    datetime(2021, 1,13, 5, 0), datetime(2021, 1,28,19,16),
                    datetime(2021, 2,11,19, 5), datetime(2021, 2,27, 8,17),
                    datetime(2021, 3,13,10,21), datetime(2021, 3,28,18,48),
                    datetime(2021, 4,12, 2,31), datetime(2021, 4,27, 3,31),
                    datetime(2021, 5,11,19, 0), datetime(2021, 5,26,11,14),
                    datetime(2021, 6,10,10,53), datetime(2021, 6,24,18,40),
                    datetime(2021, 7,10, 1,17), datetime(2021, 7,24, 2,36),
                    datetime(2021, 8, 8,13,50), datetime(2021, 8,22,12, 2),
                    datetime(2021, 9, 7, 0,52), datetime(2021, 9,20,23,55),
                    datetime(2021,10, 6,11, 5), datetime(2021,10,20,14,57),
                    datetime(2021,11, 4,21,15), datetime(2021,11,19, 8,57),
                    datetime(2021,12, 4, 7,43), datetime(2021,12,19, 4,35)
                ]
                
            case 'Mercury':
                self.ingresses = [
                    datetime(2021, 1, 8,12, 0), datetime(2021, 3,15,22,27), 
                    datetime(2021, 4, 4, 3,42), datetime(2021, 4,19,10,30), 
                    datetime(2021, 5, 4, 2,49), datetime(2021, 7,11,20,36), 
                    datetime(2021, 7,28, 1,12), datetime(2021, 8,11,21,57),
                    datetime(2021, 8,30, 5,10), datetime(2021,11, 5,22,35), 
                    datetime(2021,11,24,15,37), datetime(2021,12,13,17,52)
                ]
            
            case 'Venus':
                self.ingresses = [
                    datetime(2021, 1, 8,15,41), datetime(2021, 2, 1,14, 6),
                    datetime(2021, 2,25,13,12), datetime(2021, 3,21,14,17), 
                    datetime(2021, 4,14,18,22), datetime(2021, 5, 9, 2, 2),
                    datetime(2021, 6, 2,13,19), datetime(2021, 6,27, 4,27), 
                    datetime(2021, 7,22, 0,37), datetime(2021, 8,16, 4,27), 
                    datetime(2021, 9,10,20,39), datetime(2021,10, 7,11,21),
                    datetime(2021,11, 5,22,44)
                ]
                
            case 'Mars':
                self.ingresses = [
                    datetime(2021, 1, 6,22,27), datetime(2021, 3, 4, 3,30),
                    datetime(2021, 4,23,11,49), datetime(2021, 6,11,13,34),
                    datetime(2021, 7,29,20,33), datetime(2021, 9,15, 0,14),
                    datetime(2021,10,30,14,21), datetime(2021,12,13, 9,53)
                ]
            
            case 'Jupiter':
                self.ingresses = [
                    datetime(2021, 5,13,22,36)
                ]
                
            case 'Saturn':
                raise ValueError(f'No ingresses found for {planet}')
                
            case 'Uranus':
                raise ValueError(f'No ingresses found for {planet}')
                
            case 'Neptune':
                raise ValueError(f'No ingresses found for {planet}')
                
            case 'Pluto':
                raise ValueError(f'No ingresses found for {planet}')
                
            case _:
                raise ValueError(f'Unsupported category: {planet}')
             
        sign_init = z_ingress.get(self.planet)
        idx = z_labels.index(sign_init)
        self.labels = [z_labels[(idx+i)%12] for i in range(len(self.ingresses))]
    
    def get_tick_positions(self):
        return mdates.date2num(self.ingresses)

    def get_tick_labels(self):
        return self.labels

def set_zodiac_locator(ax, planet='Sun'):
    formatter = ZodiacFormatter(planet=planet)
    tick_positions = formatter.get_tick_positions()
    ax.xaxis.set_major_locator(FixedLocator(tick_positions))


def set_zodiac_formatter(ax, planet='Sun'):
    formatter = ZodiacFormatter(planet=planet)
    tick_labels = formatter.get_tick_labels()
    ax.xaxis.set_major_formatter(FixedFormatter(tick_labels))