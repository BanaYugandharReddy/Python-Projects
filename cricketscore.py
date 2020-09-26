# before executing the code install the "pycricbuzz" package
# use "pip install pycricbuzz" or "pip3 install pycricbuzz"


from pycricbuzz import Cricbuzz
import json
c = Cricbuzz() # create a cricbuzz object
matches = c.matches()
for match in matches:
    print(match)
    print(c.livescore(match['id'])) # fetches the lievscore
    print(c.commentary(match['id'])) # fetch the commentary of the match
    print(c.scorecard(match['id'])) # fetch the scorecard of the match


