#!/usr/bin/env python3

import time

import RPi.GPIO as GPIO
import requests #api module

from waveshare.epaper import EPaper
from waveshare.epaper import Handshake
from waveshare.epaper import RefreshAndUpdate
from waveshare.epaper import SetPallet
from waveshare.epaper import DisplayText
from waveshare.epaper import SetCurrentDisplayRotation
from waveshare.epaper import SetEnFontSize
from waveshare.epaper import ClearScreen


from yrApi.yr_data import air_temperature
air_temperature = str(air_temperature())

from yrApi.yr_data import wind_speed
wind_speed = str(wind_speed())


from yrApi.yr_data import wind_direction
wind_direction = wind_direction()

from yrApi.yr_data import precipitation_1_hour
precipitation_1_hour = str(precipitation_1_hour())

from yrApi.yr_data import summary_1_hour
summary_1_hour = summary_1_hour()

from yrApi.yr_data import updated_time
updated_time = updated_time()





if __name__ == '__main__':
    with EPaper() as paper:

        paper.send(Handshake())
        time.sleep(2)
        paper.send(SetPallet(SetPallet.BLACK, SetPallet.WHITE))
        paper.send(SetCurrentDisplayRotation(SetCurrentDisplayRotation.FLIP))
        paper.send(SetEnFontSize(SetEnFontSize.SIXTYFOUR))
        paper.read_responses(timeout=10)

        paper.send(DisplayText(100, 10, "Yr varsel for Remmen".encode("gb2312")))
        
        paper.send(DisplayText(20, 100, air_temperature.encode("gb2312") + "     grader  C".encode("gb2312")))
        
        paper.send(DisplayText(20, 200, wind_speed.encode("gb2312") + "     m/s".encode("gb2312") + "     Fra  ".encode("gb2312") + wind_direction.encode("gb2312")))
        
        
        paper.send(DisplayText(20, 400, "Om  1  time:     ".encode("gb2312") + summary_1_hour.encode("gb2312")))
        
        paper.send(DisplayText(20, 500, "Nedbor     ".encode("gb2312") + precipitation_1_hour.encode("gb2312") +"  mm".encode("gb2312") ))
        
        
        paper.send(SetEnFontSize(SetEnFontSize.THIRTYTWO))
        paper.read_responses(timeout=10)
        
        paper.send(DisplayText(385, 560, "Oppdatert ".encode("gb2312") + updated_time.encode("gb2312")))
        #700, 550




        paper.send(RefreshAndUpdate())
        paper.read_responses()
