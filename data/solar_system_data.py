from src.physics import Body


sun = Body(mass=1.989e30, x=0, y=0, vx=0, vy=0, name="Sun", color='yellow')

mercury = Body(mass=0.330e24, x=0, y=0, vx=0, vy=0, name="Mercury", color='gray')

venus = Body(mass=4.867e24, x=0, y=0, vx=0, vy=0, name="Venus", color='orange')

earth = Body(mass=5.972e24, x=0, y=0, vx=0, vy=0, name="Earth", color='blue')

mars = Body(mass=0.64171e24, x=0, y=0, vx=0, vy=0, name="Mars", color='red')


bodies = [sun, mercury, venus, earth, mars]