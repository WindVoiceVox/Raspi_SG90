#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
import atexit

class sg90:
  '''
  Servo Motor SG90をRaspberry piから簡単に使えるようにするためのクラス。
  要RPiパッケージ。

  Class for easy-to-use Servo Motor SG90 with Raspberry pi.
  '''
  def __init__( self, pin, direction ):
    '''
    初期化する。
    pin : GPIOのピン番号。PWMが使えること。
    direction : 初期の向き。 -100(一番左) から 100(一番右)までの場所を整数値で指定する。

    Initialize class.
    pin       : GPIO pin number. The pin must be able to use PWM.
    direction : Initial servo direction. Integer between -100 to 100.
    '''
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( pin, GPIO.OUT )
    self.pin = int( pin )
    self.direction = int( direction )
    self.servo = GPIO.PWM( self.pin, 50 )
    self.servo.start(0.0)
    atexit.register( self.cleanup )

  def cleanup( self ):
    '''
    最後は正面に戻して終了する

    Cleanup class.
    '''
    self.servo.ChangeDutyCycle(self._henkan(0))
    time.sleep(0.3)
    self.servo.stop()
    GPIO.cleanup()

  def currentdirection( self ):
    '''
    現在のSG90の向きを返す。

    Return current servo direction.
    '''
    return self.direction

  def _henkan( self, value ):
    '''
    ChangeDutyCycleに渡すための値を計算する。
    -100から100のfloat値を入力して、2から12の値を返す。
    ChangeDutyCycleに渡す値は 0.0 <= dc <= 100.0
    ……のはずだが、なぜか2から12の間で動作している。
    '''
    return 0.05 * value + 7.0

  def setdirection( self, direction, speed ):
    '''
    SG90の向きを変える。
    direction : -100 - 100 の整数値
    speed     : 変化量

    Set SG90 direction.
    direction : New SG90 direction. Integer between -100 to 100.
    speed     : Move speed. Integer 1 to 50.
    '''
    for d in range( self.direction, direction, int(speed) ):
      self.servo.ChangeDutyCycle( self._henkan( d ) )
      self.direction = d
      time.sleep(0.1)
    self.servo.ChangeDutyCycle( self._henkan( direction ) )
    self.direction = direction

if __name__ == "__main__":
    pass
