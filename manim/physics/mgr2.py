#!/usr/bin/env python

from manimlib.imports import *
#from topics import functions


def boy_func(t):
    return np.array((2*np.cos((TAU/10)*t), 2*np.sin((TAU/10)*t), 0))

def girl_func(t):
    return np.array((2*np.cos((TAU/10)*t+PI), 2*np.sin((TAU/10)*t+PI), 0))

def pole_func(t):
    return np.array((3, 0, 0))

def ball_func(t):
    return np.array((3.0, 0.3*t, 0))




def pboy_func(t):
    return np.array((0, 0, 0))

def pgirl_func(t):
    return np.array((2*np.cos((TAU/10)*t+PI)-2*np.cos((TAU/10)*t), 2*np.sin((TAU/10)*t+PI)-2*np.sin((TAU/10)*t), 0))

def pcent_func(t):
    return np.array((0-2*np.cos((TAU/10)*t), 0-2*np.sin((TAU/10)*t), 0))

def ppole_func(t):
    return np.array((3-2*np.cos((TAU/10)*t), 0-2*np.sin((TAU/10)*t), 0))

def pball_func(t):
    return np.array((3-2*np.cos((TAU/10)*t), 0.3*t-2*np.sin((TAU/10)*t), 0))

                    

class MerryGoRound0(Scene):
   def construct(self):
       title    = TextMobject("Merry-go-round: camera fixed at center",color=YELLOW)       
       title.scale(0.7)
       title.move_to(UP*3.5)
       
       center   = SmallDot()
       
       mgr      = Circle(radius=2.5,color=GRAY)
       mgr.set_fill(color=GRAY, opacity=0.25)

       boy      = Circle(radius=0.25,color=BLUE)
       boy.set_fill(color=BLUE, opacity=1.0)

       girl     = Circle(radius=0.25,color=PURPLE)
       girl.set_fill(color=PURPLE, opacity=1.0)

       pole     = Square(side_length=0.25)
       pole.move_to([3.0,0,0])
       
       ball     = Circle(radius=0.1)
       ball.set_fill(RED, opacity=1.0)  
       ball.move_to([3.0,0,0])

       self.add(center, mgr)
       boy.move_to([2.0,0,0])
       girl.move_to([-2.0,0,0])

       self.add(boy,girl,ball,title)
       # non-prime frame                    
       self.remove(mgr)
       boy_path = ParametricFunction(boy_func,t_max=10,fill_opacity=0)
       girl_path = ParametricFunction(girl_func,t_max=10,fill_opacity=0)
       pole_path = ParametricFunction(pole_func,t_max=10,fill_opacity=0)              
       ball_path = ParametricFunction(ball_func,t_max=10,fill_opacity=0)       
       self.play(MoveAlongPath(boy,boy_path,run_time=10,rate_func=linear),
                 MoveAlongPath(girl,girl_path,run_time=10,rate_func=linear),
                 MoveAlongPath(pole,pole_path,run_time=10,rate_func=linear),                                  
                 MoveAlongPath(ball,ball_path,run_time=10,rate_func=linear)                 
       )
       self.wait(2)



class MerryGoRound1(Scene):
   def construct(self):
       title    = TextMobject("Merry-go-round: camera fixed above the boy",color=YELLOW)       
       title.scale(0.7)       
       title.move_to(UP*3.5)
       
       center   = SmallDot()
       
       mgr      = Circle(radius=2.5,color=GRAY)
       mgr.set_fill(color=GRAY, opacity=0.25)

       boy      = Circle(radius=0.25,color=BLUE)
       boy.set_fill(color=BLUE, opacity=1.0)

       girl     = Circle(radius=0.25,color=PURPLE)
       girl.set_fill(color=PURPLE, opacity=1.0)

       pole     = Square(side_length=0.25)
       pole.move_to([3.0,0,0])       
       
       ball     = Circle(radius=0.1)
       ball.set_fill(RED, opacity=1.0)  
       ball.move_to([3.0,0,0])
       

       self.add(center)
       boy.move_to([2.0,0,0])
       girl.move_to([-2.0,0,0])

       self.add(boy,girl,pole,ball,title)

       # prime frame
       pboy_path = ParametricFunction(pboy_func,t_max=10,fill_opacity=0)
       pgirl_path = ParametricFunction(pgirl_func,t_max=10,fill_opacity=0)
       pcent_path = ParametricFunction(pcent_func,t_max=10,fill_opacity=0)
       ppole_path = ParametricFunction(ppole_func,t_max=10,fill_opacity=0,color=WHITE)                     
       pball_path = ParametricFunction(pball_func,t_max=10,fill_opacity=0,color=RED)              
       self.play(MoveAlongPath(boy,pboy_path,run_time=10,rate_func=linear),
                 MoveAlongPath(girl,pgirl_path,run_time=10,rate_func=linear),
                 MoveAlongPath(center,pcent_path,run_time=10,rate_func=linear),
                 MoveAlongPath(pole,ppole_path,run_time=10,rate_func=linear),                                                   
                 MoveAlongPath(ball,pball_path,run_time=10,rate_func=linear),                                  
       )
       self.add(ppole_path)
       self.add(pball_path)              
       self.wait(0.1)


class MerryGoRound2(ThreeDScene):
   def construct(self):
       title    = TextMobject("Merry-go-round: camera rotating above the boy at the same rate",color=YELLOW)
       title.scale(0.7)
       title.move_to(UP*3.5)
       
       center   = SmallDot()
       
       mgr      = Circle(radius=2.5,color=GRAY)
       mgr.set_fill(color=GRAY, opacity=0.25)

       boy      = Circle(radius=0.25,color=BLUE)
       boy.set_fill(color=BLUE, opacity=1.0)

       girl     = Circle(radius=0.25,color=PURPLE)
       girl.set_fill(color=PURPLE, opacity=1.0)

       pole     = Square(side_length=0.25)
       pole.move_to([3.0,0,0])   
       
       ball     = Circle(radius=0.1)
       ball.set_fill(RED, opacity=1.0)  
       ball.move_to([3.0,0,0])

       
       self.add(center)
       boy.move_to([2.0,0,0])
       girl.move_to([-2.0,0,0])
       ball.move_to([3.0,0,0])

       self.add(boy,girl,ball)
       self.add_fixed_in_frame_mobjects(title)
       
       # prime frame
       pboy_path = ParametricFunction(pboy_func,t_max=10,fill_opacity=0)
       pgirl_path = ParametricFunction(pgirl_func,t_max=10,fill_opacity=0)
       pcent_path = ParametricFunction(pcent_func,t_max=10,fill_opacity=0)
       ppole_path = ParametricFunction(ppole_func,t_max=10,fill_opacity=0,color=WHITE)                            
       pball_path = ParametricFunction(pball_func,t_max=10,fill_opacity=0,color=RED)
       self.begin_ambient_camera_rotation(rate=0.63)
       self.play(MoveAlongPath(boy,pboy_path,run_time=10,rate_func=linear),
                 MoveAlongPath(girl,pgirl_path,run_time=10,rate_func=linear),
                 MoveAlongPath(center,pcent_path,run_time=10,rate_func=linear),
                 MoveAlongPath(pole,ppole_path,run_time=10,rate_func=linear),                                                   
                 MoveAlongPath(ball,pball_path,run_time=10,rate_func=linear),                                  
       )
       #self.add(ppole_path)
       #self.add(pball_path)       
       self.wait(0.1)

       
