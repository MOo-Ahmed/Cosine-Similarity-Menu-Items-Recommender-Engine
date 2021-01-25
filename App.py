import Engine
import time

# starting time
start = time.time()

item = 'coffee'
n = 10
name = 'menu item'
engine = Engine.RecommendationEngine(item, n, name)
engine.run()

# end time
end = time.time()

# total time taken
print(f"Time =  {end - start} seconds")

