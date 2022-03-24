## Project: 3D Motion Planning
![Quad Image](./misc/enroute.png)

---

## [Rubric](https://review.udacity.com/#!/rubrics/1534/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Writeup / README

### Explain the Starter Code

#### 1. Explain the functionality of what's provided in `motion_planning.py` and `planning_utils.py`
These scripts contain a basic planning implementation that includes:
* Create a grid with 0 and 1 where 1's are obstacles.
* Implement A* Algorithm with given start and goal points.
* Prune the found path using Bresenham algorithm.

Created path is sent as waypoints.

### Implementing Your Path Planning Algorithm

#### 1. Set your global home position
lat0 and lon0 are extracted from the csv file with Regex as floating point values and used in the self.set_home_position() method to set global home.

#### 2. Set your current local position
Local position is set using the global_to_local() method.

#### 3. Set grid start position from local position
Start position is the current position. To convert, it's offset by north_offset and east_offset.

#### 4. Set grid goal position from geodetic coords
Goal positions are chosen to be either down the road or around the corner to speed up the search and check if the whole thing works.

#### 5. Modify A* to include diagonal motion (or replace A* altogether)
In planning_utils() to the A* implementation is updated to include diagonal motions on the grid that have a cost of sqrt(2).

#### 6. Cull waypoints
Bresenham module is used to trim unneeded waypoints from path


### Execute the flight
#### 1. Does it work?
It works!

### Double check that you've met specifications for each of the [rubric](https://review.udacity.com/#!/rubrics/1534/view) points.
  
# Extra Challenges: Real World Planning

For an extra challenge, consider implementing some of the techniques described in the "Real World Planning" lesson. You could try implementing a vehicle model to take dynamic constraints into account, or implement a replanning method to invoke if you get off course or encounter unexpected obstacles.


