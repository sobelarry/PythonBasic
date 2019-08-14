height_in = [70, 84, 75, 72, 72, 70, 76, 72]

# Import the numpy package as np
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out type of np_height
print(type(np_height_in))

# Convert np_height_in to m: np_height_m, by multiply np_height_in with 0.0254
np_height_m = np_height_in * 0.0254

# Create the short array, show true if np_height_m < 1.8
short = np_height_m < 1.8

# Print out Short
print(short)

# Print out np_height_m of all baseball players whose np_height_m is below 1.8
print(np_height_m[np_height_m<1.8])

``` 2d Numpy Array ```
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the 3th row of np_baseball
print(np_baseball[2,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 4th player
print(np_baseball[3,0])

``` Statistics ```
# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean, median, standard deviation and correlation of np_height_in
print(np.mean(np_height_in))
print(np.median(np_height_in))
print(np.std(np_height_in))
print(np.corrcoef(np_height_in))


positions = ['GK', 'M', 'A', 'D', 'GK', 'M', 'A', 'GK']
heights = [191, 184, 185, 180, 200, 179, 188, 199]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']
