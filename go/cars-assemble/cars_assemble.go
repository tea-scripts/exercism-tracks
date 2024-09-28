package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	successRate /= 100
	return float64(productionRate) * successRate
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	carsPerMinute := float64(productionRate) / 60.0

	workingCarsPerMinute := carsPerMinute * (successRate / 100.0)

	return int(workingCarsPerMinute)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	discountedPrice := 95000
	unitPrice := 10000

	groupsOfCars := carsCount / 10
	inidividualCars := carsCount % 10

	totalCost := (groupsOfCars * discountedPrice) + (inidividualCars * unitPrice)

	return uint(totalCost)
}
