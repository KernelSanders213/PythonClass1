import time
import tracemalloc

def compare_performance(func):
  # Start tracking memory
  tracemalloc.start()

  # Start timer
  start_time = time.perf_counter()

  # Run function
  result = func()

  # Stop timer
  end_time = time.perf_counter()

  # Get memory usage
  current, peak = tracemalloc.get_traced_memory()
  tracemalloc.stop()

  execution_time = end_time - start_time
  print(f"Function: {func.__name__}")
  print(f"Execution Time: {execution_time:.6f} seconds")
  print(f"Peak Memory Usage: {peak / 1024 / 1024:.4f} MB")
  print("-" * 30)