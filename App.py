import Engine
import time

start = time.time()

item = 'grilled chicken pizza'
n = 5
name = 'menu item'
engine = Engine.RecommendationEngine(item, n, name)
engine.run()

end = time.time()

# total time taken
print(f"Time =  {end - start} seconds")

