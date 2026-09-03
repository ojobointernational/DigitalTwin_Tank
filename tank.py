import random
import time

water_level = 100  # full tank %

for i in range(20):
    usage = random.uniform(1, 50)
    water_level -= usage
    
    print(f"Water Level: {water_level:.2f}%")
    
    if water_level < 20:
        print("⚠️ Warning: Tank getting empty!")
    
    time.sleep(1)

    # edited and pushed from repo augustine
    # edited bypassrule
  # changes to branch
  