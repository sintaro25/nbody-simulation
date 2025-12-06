from src.physics import Body


sun = Body(mass=1.989e30, x=0, y=0, vx=0, vy=0, name="Sun", color='yellow')

mercury = Body(mass=0.330e24, x=58e9, y=0, vx=0, vy=47360, name="Mercury", color='gray')

venus = Body(mass=4.867e24, x=108e9, y=0, vx=0, vy=35020, name="Venus", color='orange')

earth = Body(mass=5.972e24, x=149e9, y=0, vx=0, vy=29780, name="Earth", color='blue')

mars = Body(mass=0.64171e24, x=228e9, y=0, vx=0, vy=24070, name="Mars", color='red')

jupiter = Body(1.89813e27, x=778e9, y=0, vx=0, vy=13100, name="Jupiter", color='#e3dccb')


bodies = [sun, mercury, venus, earth, mars, jupiter]