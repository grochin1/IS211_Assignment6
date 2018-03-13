# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import conversions as conv
import conversions_refactored as convref

class TestConversions(unittest.TestCase):
    knownValuesCKF = (
        (0, 273.15, 32.00),
        (100, 373.15, 212.00),
        (300, 573.15, 572.00),
        (-100, 173.15, -148.00),
        (-273.15, 0.00, -459.67)
    )

    def testConvertCelsiusToKelvin(self):
        for celsius, kelvin, fahr in self.knownValuesCKF:
            print 'checking convertCelsiusToKelvin', celsius
            result = conv.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def testConvertCelsiusToFahrenheit(self):
        for celsius, _, fahr in self.knownValuesCKF:
            print 'checking convertCelsiusToFahrenheit', celsius
            result = conv.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahr, result)

    def testConvertFahrenheitToCelsius(self):
        for celsius, kelvin, fahr in self.knownValuesCKF:
            print 'checking convertFahrenheitToCelsius', fahr
            result = conv.convertFahrenheitToCelsius(fahr)
            self.assertEqual(celsius, result)

    def testConvertFahrenheitToKelvin(self):
        for celsius, kelvin, fahr in self.knownValuesCKF:
            print 'checking convertFahrenheitToKelvin', fahr
            result = conv.convertFahrenheitToKelvin(fahr)
            self.assertEqual(kelvin, result)

    def testConvertKelvinToCelsius(self):
        for celsius, kelvin, fahr in self.knownValuesCKF:
            print 'checking convertKelvinToCelsius', kelvin
            result = conv.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)

    def testConvertKelvinToFahrenheit(self):
        for celsius, kelvin, fahr in self.knownValuesCKF:
            print 'checking convertKelvinToFahrenheit', kelvin
            result = conv.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahr, result)

class TestConversionsRefactored(unittest.TestCase):
    unitTemp = ['Celsius', 'Kelvin', 'Fahrenheit']
    unitDistance = ['Meter', 'Yard', 'Mile']
    incompatible = [(u1,u2) for u1 in unitTemp for u2 in unitDistance] + [(u2,u1) for u1 in unitTemp for u2 in unitDistance]
    knownValues = (
        {'Celsius':0, 'Kelvin':273.15, 'Fahrenheit':32.00},
        {'Celsius':100, 'Kelvin':373.15, 'Fahrenheit':212.00},
        {'Celsius':300, 'Kelvin':573.15, 'Fahrenheit':572.00},
        {'Celsius':-100, 'Kelvin':173.15, 'Fahrenheit':-148.00},
        {'Celsius':-273.15, 'Kelvin':0.00, 'Fahrenheit':-459.67},
        {'Meter':949.51, 'Yard':1038.4, 'Mile':0.59},
        {'Meter':1609.34, 'Yard':1760.00, 'Mile':1.00},
        {'Meter':5005.06, 'Yard':5473.6, 'Mile':3.11},
        {'Meter':997.79, 'Yard':1091.2, 'Mile':0.62},
        {'Meter':9994.03, 'Yard':10929.6, 'Mile':6.21},
    )

    def testConvert(self):
        """ test conversion between compatible units, including a unit to itself """
        for inst in self.knownValues:
            for unitFrom, v1 in inst.iteritems():
                for unitTo, v2 in inst.iteritems():
                    print 'checking convert(%s, %s, %f) = %f' %(unitFrom, unitTo, v1, v2)
                    result = convref.convert(unitFrom, unitTo, v1)
                    self.assertEqual(v2, result)

    def testIncompatible(self):
        """ test conversion between incompatible units raises ConversionNotPossible exception """
        for unitFrom, unitTo in self.incompatible:
            print 'checking convert from %s to %s is incompatible' %(unitFrom, unitTo)
            self.assertRaises(convref.ConversionNotPossible, convref.convert, unitFrom, unitTo, 12345)

if __name__ == '__main__':
    unittest.main()