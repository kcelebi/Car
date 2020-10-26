# Car

This is a project dedicated to providing a solution to traffic, in the context of a max-flow problem. The first part of this project, located in folder V1 is a simulation of traffic in a small, isolated city system. The second part, located in folder V2, uses data from the first to create an algorithm that adds n new roads to a system to alleviate traffic as much as possible.

# V1

This folder includes a program that simulates the movement of cars through 6 grids of two-way city roads. Cars follow random paths that are consistent with lawful driving. This includes waiting at stoplights for other cars with right-of-way and turning only onto certain roads. A graphic of the map has been implemented using nodes and edges to visualize the traffic, and can be run with road3.py . The color of the roads indicate the density, with red meaning heavy traffic and green meaning light to no traffic. In the terminal output with that Python file you will be able to see multiple lists that contain car ID's. Each list corresponds to a street. This is mostly for debugging purposes, but it acts as another visualization for the traffic density on each road. The labels of the arrays (RA, LE, etc.) refer to the label of the road, and which side. RA refers to road A on the right side, LJ refers to road J on the left side.

# V2
(V2 code retracted, new changes being implemented, stick around to see them soon)
