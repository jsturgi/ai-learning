# Day 1.5 11/4/2025

# Roadmap Version 1.3

## What I learned today:
- I learned how to write a dockerfile and a docker-compose.yaml file.  I also configured a custom container image from scratch! I've just pulled existing images in the past.
- I got a refresher on vectors, their properties, and their operations.  Its been a few years since I've used anything Linear Algebra related so it was a good refresher.
- I implemented a vector class in the jupyter notebook.  Unfortunately, my original plan was generated with full implementation and I saw it as I was reading the task.  I've since updated my learning agent's rules and updated all my daily plans so this won't happen again.

## What I built Today
- Vector class from scratch**
- a dev container based on python 3.11 with datascience. libraries installed (pandas, matplot, numpy, scikit, etc)
- a dockerfile and docker-compose file
- a callable graph function using matplotlib

## Implementation Details
- used magic methods in my vector class
- used list comprehension** in my dot product and vector addition solutions.

## Challenges I Faced
- Initally, the roadmap was generated using a virtual environment.  I decided it wasn't worth the hassle and considering that most professionals use containers, it would be a good time to start getting familiar with docker. 
- As mentioned previously, the vector solution was generated with the daily roadmaps. I tried to come up with my own solution but after seeing the list comprehension solution, it was difficult to come up with a solution that wasn't just expanding the list comprehension into multiple lines so I just accepted it for today and fixed the issue moving forward.
- There were multiple rules and refactors I needed to run to get to my current version (1.3). The rules I added were - no implementation provided ever (empty functions with docstrings is okay), academic sources. must be referenced if learning a mathematical/theory topic (ie the vector lecture I watched today), and this wasn't a problem with the initial version, but I added an extra practice file for each week.

## Insights
-  The way vector multiplication was described in the MIT lecture made sense - its always been something that has confused me.  
- There was a vector mindmap in the vector section from the ml math textbook that helped me remember how the different aspects of linear algebra are connected.
- It's been so long since I've used a list comprehension that it didn't come to mind until I saw it and realized what it was.  