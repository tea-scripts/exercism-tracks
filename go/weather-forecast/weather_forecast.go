// Package weather provides an application to get a forcast
// for a provided city.
package weather

// CurrentCondition stores the weather condition of a city.
var CurrentCondition string

// CurrentLocation stores and returns the location of a city.
var CurrentLocation string

// Forecast returns a string of city's currrent location 
// and current weather condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
