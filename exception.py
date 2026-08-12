try:
    raise TypeError("error")
    pass
except TypeError as e:
    print(f"Cleaning up type error: {e}")
    raise  # Re-raises the caught BaseException safely
except:
    print(f"Cleaning up resources after error")
    raise  # Re-raises the caught BaseException safely
