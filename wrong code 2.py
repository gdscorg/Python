#!/usr/bin/env python
# coding: utf-8

# In[2]:


# wrong code 2
#you need to create two objects of the Vehicle class object that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.
class Vehicle:
    color = "white"

    def __init__(max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties():
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)


vehicle1 = Vehicle(200, 50000)
vehicle1.seating_capacity(5)
vehicle1.display_properties

vehicle2 = Vehicle(180, 75000)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()


# In[ ]:




