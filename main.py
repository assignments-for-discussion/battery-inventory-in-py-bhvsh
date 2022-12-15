
def count_batteries_by_usage(cycles):
  #Initializing variables for low, med and high counts
  lowcount=0
  medcount=0
  highcount=0
  
  for val in cycles:
    # Battery capacity won't be less than zero
    if val >= 0 and val < 310:
      lowcount+=1
    elif val >= 310 and val <= 929:
      medcount+=1
    # Upper bound was not implemented since it was not mentioned in the problem statement.
    elif val > 929:
      highcount+=1
    else:
      print(f"Invalid entry in cycle. Skipped {val}")
  
  return {
    "lowCount": lowcount,
    "mediumCount": medcount,
    "highCount": highcount
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)

  #Testing Boundary conditions
  counts = count_batteries_by_usage([-2, 0, 309, 310, 929, 930, 2000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 2)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
