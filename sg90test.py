#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import raspi_sg90

# GPIO 12番を使用 (PWM 0)
s = raspi_sg90.sg90( 12, 0 )

while True:
  print "Turn left ..."
  s.setdirection( 100, 10 )
  time.sleep(0.5)
  print "Turn right ..."
  s.setdirection( -100, -10 )
  time.sleep(0.5)
