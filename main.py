def count_batteries_by_health(present_capacities):
    rated_capacity = 120
    health_counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    for present_capacity in present_capacities:
        soh = 100 * present_capacity / rated_capacity

        if soh >= 83:
            health_counts["healthy"] += 1
        elif 63 <= soh < 83:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1

    return health_counts  
      
def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2), f"Expected 2 healthy, got {counts['healthy']}"
    assert(counts["exchange"] == 3), f"Expected 3 exchange, got {counts['exchange']}"
    assert(counts["failed"] == 1), f"Expected 1 failed, got {counts['failed']}"
    assert(count_batteries_by_health([120]) == {"healthy": 1, "exchange": 0, "failed": 0})
    assert(count_batteries_by_health([60]) == {"healthy": 0, "exchange": 0, "failed": 1})
    assert(count_batteries_by_health([80, 81]) == {"healthy": 0, "exchange": 2, "failed": 0})

    print("Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()
