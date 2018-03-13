# !/usr/bin/env python
# -*- coding: utf-8 -*-

class ConversionNotPossible(Exception):
	pass

def celsiusToKelvin(cels):
	return round(cels + 273.15, 2)

def celsiusToFahrenheit(cels):
	return round(cels * 9/5.0 + 32, 2)

def fahrenheitToCelsius(fahr):
	return round((fahr-32)*5/9.0, 2)

def fahrenheitToKelvin(fahr):
	return round((fahr+459.67)*5/9.0, 2)

def kelvinToCelsius(kelvin):
	return round(kelvin - 273.15, 2)

def kelvinToFahrenheit(kelvin):
	return round(kelvin*9/5.0 - 459.67, 2)

def yardToMeter(yard):
	return round(yard*0.9144, 2)

def yardToMile(yard):
	return round(yard/1760.0, 2)

def meterToYard(meter):
	return round(meter/0.9144, 2)

def meterToMile(meter):
	return round(meter/1609.34, 2)

def mileToMeter(mile):
	return round(mile*1609.344, 2)

def mileToYard(mile):
	return round(mile*1760.0, 2)

convFromTo = {
	'Fahrenheit': {'Kelvin': fahrenheitToKelvin, 'Celsius': fahrenheitToCelsius},
	'Kelvin': {'Fahrenheit': kelvinToFahrenheit, 'Celsius': kelvinToCelsius},
	'Celsius': {'Kelvin': celsiusToKelvin, 'Fahrenheit': celsiusToFahrenheit},
	'Meter': {'Yard': meterToYard, 'Mile': meterToMile},
	'Yard': {'Meter': yardToMeter, 'Mile': yardToMile},
	'Mile': {'Yard': mileToYard, 'Meter': mileToMeter},
}

def convert(fromUnit, toUnit, value):
	if fromUnit == toUnit:
		return float(value)
	if not toUnit in convFromTo[fromUnit]:
		raise ConversionNotPossible, 'cannot convert from %s to %s' %(fromUnit, toUnit)
	converter = convFromTo[fromUnit][toUnit]
	return converter(value)