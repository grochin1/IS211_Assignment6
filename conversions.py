# !/usr/bin/env python
# -*- coding: utf-8 -*-

def convertCelsiusToKelvin(cels):
	return round(cels + 273.15, 2)

def convertCelsiusToFahrenheit(cels):
	return round(cels * 9/5.0 + 32, 2)

def convertFahrenheitToCelsius(fahr):
	return round((fahr-32)*5/9.0, 2)

def convertFahrenheitToKelvin(fahr):
	return round((fahr+459.67)*5/9.0, 2)

def convertKelvinToCelsius(kelvin):
	return round(kelvin - 273.15, 2)

def convertKelvinToFahrenheit(kelvin):
	return round( kelvin*9/5.0 - 459.67, 2)