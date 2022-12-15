
def count_batteries_by_usage(cycles):
  #Initializing variables for low, med and high counts
  lowcount=0
  medcount=0
  highcount=0
  
  for val in cycles:
    if val < 310:
      lowcount+=1
    elif val >= 310 and val <= 929:
      medcount+=1
    else:
      highcount+=1
  
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
  counts = count_batteries_by_usage([0, 309, 310, 929, 930])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 2)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
