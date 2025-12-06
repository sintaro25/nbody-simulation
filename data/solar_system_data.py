from src.physics import Body

sun = Body(1.989e30, 0, 0, 0, 0, "Sun", "yellow")
mercury = Body(3.30e23, 57.9e9, 0, 0, 47.36e3, "Mercury", "gray")
venus   = Body(4.87e24,108.2e9, 0, 0, 35.02e3, "Venus",  "orange")
earth   = Body(5.97e24,149.6e9, 0, 0, 29.78e3, "Earth",  "blue")
mars    = Body(6.42e23,227.9e9, 0, 0, 24.07e3, "Mars",   "red")
jupiter = Body(1.898e27,778.5e9,0, 0, 13.07e3, "Jupiter","brown")
saturn  = Body(5.683e26,1.433e12,0,0, 9.68e3, "Saturn", "gold")
uranus  = Body(8.681e25,2.872e12,0,0, 6.80e3, "Uranus", "lightblue")
neptune = Body(1.024e26,4.495e12,0,0, 5.43e3, "Neptune","darkblue")

bodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
