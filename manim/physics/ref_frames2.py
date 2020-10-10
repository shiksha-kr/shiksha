#!/usr/bin/env python

from manimlib.imports import *

def rocket_func1(t):
    return np.array((0, -3.0+0.25*t, 0))

def ball_func(t):
    return np.array((-0.5+0.05*t, -3.0+0.25*t, 0))

def rocket_func2(t):
    return np.array((0, -3.0+0.25*t+0.5*0.00375*t*t, 0))

def nifpath_func(t):
    return np.array((0.05*t, -0.5*0.00375*t*t, 0)) 

def update_vry(vry):
    vry.scale(1.002) # how to make ths 0.5*a*t^2?
    vry.move_to([2.5,1.5,0.0])
    return(vry)

class FramesIntro(Scene):
   def construct(self):
       txt0 = TextMobject("Frames of Reference",color=YELLOW)
       txt0.move_to(txt0.get_center()+UP*2.5)              
       self.add(txt0)
       self.wait(3)

       txt1 = TextMobject("Inertial Frame of Reference: Zero or Constant Velocity")       
       txt1.scale(0.7)
       txt1.move_to(txt1.get_center()+UP*1.0)       
       self.add(txt1)
       self.wait(3)
       
       txt2 = TextMobject("Non-Inertial Frame of Reference: Accelerating")       
       txt2.scale(0.7)
       txt2.move_to(txt2.get_center()+UP*0.0)       
       self.add(txt2)                     
       self.wait(28)


class ReferenceFrames(Scene):

    def construct(self):
        txt0 = TextMobject("Frames of Reference",color=YELLOW)
        txt0.move_to(txt0.get_center()+UP*3.75)
        txt1 = TextMobject("Inertial Frame of Reference: Zero or Constant Velocity")
        txt1.scale(0.7)
        txt1.move_to(txt1.get_center()+UP*1.0)
        txt2 = TextMobject("Non-Inertial Frame of Reference: Accelerating")       
        txt2.scale(0.7)
        txt2.move_to(txt2.get_center()+UP*0.0)       
        
        body     = Rectangle(height=1.5,width=1.0)
        head     = Polygon([-0.5, 0.75, 0], [0.5, 0.75, 0], [0, 1.25, 0], color=GRAY)
        trail1   = Line([0.0,-0.75,0.0],[0.0,-0.95,0.0],color=RED)
        trail2   = Line([0.25,-0.75,0.0],[0.30,-0.85,0.0],color=RED)
        trail3   = Line([-0.25,-0.75,0.0],[-0.30,-0.85,0.0],color=RED)
        
        head.set_fill(GRAY, opacity=1.0)
        line_d   = DashedLine(body.get_center()+LEFT*0.5, body.get_center()+RIGHT*0.5)        
        rocket   = Group(body,head,line_d,trail1,trail2,trail3)

        self.add(txt0)
        self.wait(10)
        self.add(txt1)
        self.wait(8)        
        self.add(txt2)
        self.wait(16)
        self.remove(txt0,txt1,txt2)

        
        vry      = Vector([0.0,1.0,0.0], color=BLUE)
        vry.move_to([2.5,1.5,0.0])
        vry_lab  = TextMobject("Vy(rocket)") 
        vry_lab.scale(0.5)
        vry_lab.next_to(vry,LEFT,buff=SMALL_BUFF)

        vbx      = Vector([0.5,0.0,0.0], color=BLUE)
        vbx.move_to([4.25,1.0,0.0])
        vbx_lab  = TextMobject("Vx(ball)") 
        vbx_lab.scale(0.5)
        vbx_lab.next_to(vbx,RIGHT,buff=SMALL_BUFF)        

        vby      = Vector([0.0,1.0,0.0], color=BLUE)
        vby.move_to([4.0,1.5,0.0])
        vby_lab  = TextMobject("Vy(ball)") 
        vby_lab.scale(0.5)
        vby_lab.next_to(vby,LEFT,buff=SMALL_BUFF)                

        
        START_Y  = rocket.get_center()+[0,-2.5,0]
        END_Y    = rocket.get_center()+[0,2.5,0]

        # Just the rocket motion
        path     = ParametricFunction(rocket_func1, t_max=10,fill_opacity=0)
        self.add(vry,vry_lab)        
        self.play(MoveAlongPath(rocket,path,run_time=10,rate_func=linear))
        self.play(FadeOut(rocket),
                  FadeOut(vry),
                  FadeOut(vry_lab),
        )

        # Inertial
        txt0 = TextMobject("Inertial Frame of Reference",color=YELLOW)
        txt0.move_to(txt0.get_center()+UP*3.75)        
        self.add(txt0)
        rocket.move_to(START_Y)
        path     = ParametricFunction(rocket_func1, t_max=20,fill_opacity=0)        
        ball = Dot(color=RED)
        ball_path = ParametricFunction(ball_func, t_max=20, fill_opacity=0)
        ball.move_to(START_Y+[0.5,0,0])

        self.add(vbx,vbx_lab, vby,vby_lab, vry,vry_lab)
        self.play(MoveAlongPath(rocket,path,run_time=20,rate_func=linear),
                  MoveAlongPath(ball,ball_path,run_time=20,rate_func=linear),
        )
        self.wait(23)
        
        if_path = Line(rocket.get_center()+LEFT*0.5, rocket.get_center()+RIGHT*0.5, color=YELLOW)
        self.add(if_path)        
        self.wait(11)
        self.remove(txt0)
        self.remove(if_path)                
        self.remove(vbx,vbx_lab, vby,vby_lab, vry,vry_lab)
        
        # Non-Intertial
        txt0 = TextMobject("Non-Inertial Frame of Reference",color=YELLOW)
        txt0.move_to(txt0.get_center()+UP*3.75)        
        self.add(txt0)
        
        self.add(vbx,vbx_lab, vby,vby_lab, vry,vry_lab)        
        rocket.move_to(START_Y)
        ball.move_to(START_Y+[0.5,0,0])
        path     = ParametricFunction(rocket_func2, t_max=20,fill_opacity=0)                  

        self.add(vry, vbx, vby)
        self.play(MoveAlongPath(rocket,path,run_time=20,rate_func=linear),
                  MoveAlongPath(ball,ball_path,run_time=20,rate_func=linear),                  
                  UpdateFromFunc(vry,update_vry)
        )       
        self.wait(23)
        nif_path = ParametricFunction(nifpath_func, t_max=20, fill_opacity=0, color=YELLOW)
        nif_path.move_to(nif_path.get_center()+rocket.get_center()+LEFT*0.5)        
        self.add(nif_path)        
        self.wait(27)
        
        fma_eqn = TexMobject("\Sigma F = ma") 
        self.add(fma_eqn)
        fma_eqn.move_to(RIGHT*3+DOWN*2)
        self.wait(38)        

        
class Jnk(Scene):

    def construct(self):

        dot = Dot()
        
        vry      = Vector([0.0,0.5,0.0], color=YELLOW)


        
        self.add(vry, dot)
        self.wait(3)

        vry.move_to([2.0,1.0,0.0])
        dot.move_to([2.0,1.0,0.0])
        self.add(vry, dot)
        self.wait(3)
        
        vby      = Vector([0.0,0.5,0.0], color=YELLOW)
        vby.move_to([2.0,-0.75,0.0])

        vbx      = Vector([0.5,0.0,0.0], color=YELLOW)
        vbx.move_to([2.25,-1.0,0.0])     

        dot.move_to(vbx.get_center())
        
        self.add(vbx, vby, vry, dot)

        self.wait(3)

