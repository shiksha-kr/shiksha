#!/usr/bin/env python

from manimlib.imports import *
#from topics import functions


        
############################## Real stuff from here on ###########################         
class CircularMotion0(ThreeDScene):
    def construct(self):

        title    = TextMobject("Uniform Circular Motion:Centripetal Force", color=YELLOW)
        center   = SmallDot()
        circle   = Circle(radius=2.0,color=GRAY)
        tangent  = Line([2,0,0],[2,2,0])
        tangent1 = Line([2,0.5,0],[2,2.5,0])        
        string   = Line([0,0,0],[1.9,0,0])
        #ball     = Sphere(radius=0.1,fill_color=RED, checkerboard_colors=[RED, RED])
        ball     = Circle(arc_center=[2.0,0,0],radius=0.1)
        ball.set_fill(RED, opacity=1.0)        

        velocity  = Arrow([2.0,0.0,0.0],[2.0,1.0,0.0],color=GREEN)
        tension   = Arrow([2.0,0,0],[0,0,0],color=BLUE)
        
        txt1      = TextMobject("Top View")
        txt1.scale(0.7)
        
        self.move_camera(phi=0.8*np.pi/2, theta=-0.50*np.pi)        
        ball.move_to([2.0,0,0])
        self.add(center)
        self.add(circle)

        self.play(Rotating(string,radians=6.0*TAU,about_point=ORIGIN,run_time=18),
                  Rotating(ball,radians=6.0*TAU,about_point=ORIGIN,run_time=18),
                  Rotating(velocity,radians=6.0*TAU,about_point=ORIGIN,run_time=18),

        )
        # 00:00:18
        self.move_camera(phi=0, theta=-1*np.pi/2, run_time=4)
        
        title.move_to(title.get_center()+UP*3.5)
        self.add(title)

        txt1.move_to(txt1.get_center()+UP*2.5)        
        self.add(txt1)
        
        # 00:00:22
        self.play(Rotating(string,radians=14.0*TAU,about_point=ORIGIN,run_time=42),
                  Rotating(ball,radians=14.0*TAU,about_point=ORIGIN,run_time=42),
                  Rotating(velocity,radians=14.0*TAU,about_point=ORIGIN,run_time=42),
        )

        # 00:01:04
        self.play(Rotating(string,radians=2.0*TAU,about_point=ORIGIN,run_time=6),
                  Rotating(tension,radians=2.0*TAU,about_point=ORIGIN,run_time=6),
                  Rotating(ball,radians=2.0*TAU,about_point=ORIGIN,run_time=6),
                  Rotating(velocity,radians=2.0*TAU,about_point=ORIGIN,run_time=6),
        )        

        # 00:01:10
        self.play(FadeOut(circle),
                  FadeOut(center),
                  FadeOut(string),
                  FadeOut(tension),
                  FadeOut(ball),
                  FadeOut(velocity)
        )          


class CircularMotion1(Scene):
    def construct(self):
        center   = SmallDot()
        radius1  = DashedLine([0.0,0,0],[1.5,0,0])        
        radius2  = DashedLine([0.0,0,0],[1.5,0,0])
        circle   = Circle(radius=1.5,color=GRAY)
        ball     = Circle(arc_center=[1.5,0,0],radius=0.1)
        ball.set_fill(RED, opacity=1.0)        
        
        V        = [0.0,1.0,0.0]
        v1       = Vector(V, color=GREEN)
        v1_lab   = TexMobject("v1").scale(0.5)
        v1p      = Vector(V, color=GREEN)        
        v1.move_to([1.5,0.5,0.0])
        v2       = Vector(V, color=GREEN)
        v2_lab   = TexMobject("v2").scale(0.5)        
        v2p       = Vector(V, color=GREEN)
        v2p.rotate(angle=PI/4, about_point=ORIGIN)

        v2.move_to([1.5,0.5,0.0])        

        self.add(center, circle, radius1, radius2, v1)
        self.play(Rotating(radius2,radians=PI/4, about_point=ORIGIN),
                  Rotating(v2,radians=PI/4, about_point=ORIGIN),
                  Rotating(ball,radians=PI/4, about_point=ORIGIN),                  
                  run_time=2)
        
        v1_lab.next_to(v1,0.5*RIGHT,buff=SMALL_BUFF)
        self.add(v1_lab)

        v2_lab.next_to(v2,0.5*RIGHT,buff=SMALL_BUFF)
        self.add(v2_lab)        

        self.wait(18) #0:03
        self.remove(v1_lab,v2_lab)

        self.play(Transform(v1,v1p), run_time=3) #0:20
        v1_lab.next_to(v1,(0.25*RIGHT+0.1*UP),buff=SMALL_BUFF)
        self.add(v1_lab)        

        self.wait(2) #0:23
        
        self.play(Transform(v2,v2p), run_time=3) #0:25
        v2_lab.next_to(v2,0.25*LEFT,buff=SMALL_BUFF)
        self.add(v2_lab)
        
        dv      = Vector(v2.get_end()-v1.get_end())
        dv_lab   = TexMobject("\Delta v").scale(0.5)
        
        l1 = Line([dv.get_center()[0],dv.get_center()[1],0], [dv.get_center()[0],dv.get_center()[1]+1.0,0])
        self.play(MoveAlongPath(dv,l1),run_time=0.1) #0:28
        dv_lab.next_to(dv,0.3*UP,buff=SMALL_BUFF)
        self.add(dv_lab)
        
        #self.add(dv)
        self.wait(16)#0:28.1
        eqn0   = TexMobject("v1 = v(t); v2 = v(t+\Delta t)").scale(0.5)
        eqn1   = TexMobject("\Delta v = v2-v1").scale(0.5)
        eqn2   = TexMobject("Acceleration = \Delta v/\Delta t").scale(0.5)
        eqn3   = TexMobject("Force = m.(\Delta v/\Delta t)").scale(0.5)        
        eqn0.move_to(3.5*RIGHT+UP*1.5)
        eqn1.move_to(3.5*RIGHT+UP*0.75)
        eqn2.move_to(3.5*RIGHT)        
        eqn3.move_to(3.5*RIGHT+DOWN*0.75)
        self.add(eqn0, eqn1, eqn2, eqn3)
        self.wait(14.9) #0:44.1 ->0:59
        

class CircularMotion2(Scene):
   def construct(self):
       title    = TextMobject("Uniform Circular Motion: Centripetal Force",color=YELLOW)
       earth    = ImageMobject('assets/images/earth.png')
       moon     = ImageMobject('assets/images/moon.png')
       gravity  = Arrow([-2.0,0,0],[-0.75,0,0],color=BLUE)       
       title.move_to(title.get_center()+UP*3.5)

       self.add(title)
       self.add(earth)
       moon.scale(0.25)
       moon.move_to([2.5,0,0])
        
       self.play(Rotating(moon,radians=1.5*TAU,about_point=ORIGIN,run_time=15))


       self.play(Rotating(moon,radians=1.1*TAU,about_point=ORIGIN,run_time=11),
                 Rotating(gravity,radians=1.1*TAU,about_point=ORIGIN,run_time=11),
       )       


       self.play(FadeOut(gravity),
                 FadeOut(moon),
                 FadeOut(earth)
       )       

       
       
class CircularMotion3(Scene):
   def construct(self):
       title    = TextMobject("Uniform Circular Motion: Centrifugal Force",color=YELLOW)

       string   = Line([0,0,0],[1.9,0,0])
       ball     = Circle(arc_center=[2.0,0,0],radius=0.1)
       ball.set_fill(RED, opacity=1.0)        
       fly      =  ImageMobject('assets/images/fly.png')
       fly.scale(0.05)
       fly.move_to([2,0,0])
       velocity  = Arrow([2.0,0.0,0.0],[2.0,1.0,0.0],color=GREEN)

       #centripetal = Arrow([2,0,0],[1,0,0],color=BLUE)
       #centrifugal = Arrow([2,0,0],[3,0,0],color=BLUE)
       centripetal = Vector([-1,0,0],color=BLUE)
       centripetal.move_to([1.3,0,0])
       centrifugal = Vector([1,0,0],color=BLUE)                     
       centrifugal.move_to([2.7,0,0])
       
       # 0:0
       self.play(Rotating(string,radians=5.0*TAU,about_point=ORIGIN,run_time=15),
                 Rotating(ball,radians=5.0*TAU,about_point=ORIGIN,run_time=15),
                 Rotating(fly,radians=5.0*TAU,about_point=ORIGIN,run_time=15),                 
                 Rotating(velocity,radians=5.0*TAU,about_point=ORIGIN,run_time=15),
                 
       )
       self.wait(3) #0:18
       self.play(FadeOut(ball),
                 FadeOut(string),
                 FadeOut(fly),
                 FadeOut(velocity)
       )

       fly.scale(5)                 
       ball.scale(5)
       self.add(ball,fly)
       self.wait(9) #0:27
       self.add(centripetal)
       self.wait(16) #0:43       
       self.add(centrifugal)
       self.wait(12)       

       
       
class CircularMotion4(Scene):
    def construct(self):
       title  = TextMobject("Uniform Circular Motion: Balanced Forces",color=YELLOW)               
       arc   =  Arc(radius=3,start_angle=-PI/4,angle=PI/2)
       bus   = Dot(color=YELLOW)
       bus.move_to([3.0,0,0])
       #velocity = Arrow([3,0,0],[3,1,0],color=GREEN)
       centripetal = Arrow([3,0,0],[1,0,0],color=BLUE)
       centripetal_lab = TexMobject("Centripetal Force").scale(0.5)
       centrifugal = Arrow([3,0,0],[5,0,0],color=BLUE)
       centrifugal_lab = TexMobject("Centrifugal Force").scale(0.5)       
       title.move_to(title.get_center()+UP*3.5)

       self.add(title)       
       self.add(arc)
       self.add(bus)
       self.wait(5) #0:05
       self.add(centrifugal)
       self.wait(33) #0:38                    

       centripetal_lab.next_to(centripetal, 0.5*TOP, buff=SMALL_BUFF)
       self.add(centripetal, centripetal_lab)
       self.wait(5) #0:43

       centrifugal_lab.next_to(centrifugal, 0.5*TOP, buff=SMALL_BUFF)
       self.add(centrifugal, centrifugal_lab)
       self.wait(12) #0:55              

       
class CircularMotion5(Scene):
    def construct(self):
       title  = TextMobject("Uniform Circular Motion: Summary",color=YELLOW)
       title.move_to(title.get_center()+UP*3.5)
       self.add(title)
       vert = DashedLine(DOWN, UP).scale(3.0)
       self.add(vert)
       
       itxt  = TextMobject("Inertial Observer -- on the Ground")
       itxt.scale(0.5)
       itxt.move_to(itxt.get_center()+UP*2.5+LEFT*2.5)       
       ibus   = Dot(color=YELLOW)
       ibus.move_to([-1.0,0,0])

       iarc   =  Arc(radius=3,arc_center=[-4,0,0], start_angle=-PI/4,angle=PI/2)

       ivelocity = Arrow([-1,0,0],[-1,1,0],color=GREEN)
       icentripetal = Arrow([-1,0,0],[-3,0,0],color=BLUE)
       icentripetal_lab = TexMobject("Centripetal Force").scale(0.5)

       #00:05:23
       self.add(itxt,iarc,ibus,ivelocity)

       #self.add(velocity)
       self.wait(9) #0:09
       self.add(icentripetal)
       self.wait(4) #0:13       
       icentripetal_lab.next_to(icentripetal, 0.5*TOP, buff=SMALL_BUFF)
       self.add(icentripetal, icentripetal_lab)
       self.wait(11) #0:24
       
       #############
       ntxt  = TextMobject("Non-Inertial Observer -- on the Bus")
       ntxt.scale(0.5)
       ntxt.move_to(ntxt.get_center()+UP*2.5+RIGHT*2.5)       
       
       nbus   = Dot(color=YELLOW)
       nbus.move_to([3.0,0,0])
       narc   =  Arc(radius=3,start_angle=-PI/4,angle=PI/2)       

       ncentripetal = Arrow([3,0,0],[1,0,0],color=BLUE)
       ncentripetal_lab = TexMobject("Centripetal Force").scale(0.5)
       ncentrifugal = Arrow([3,0,0],[5,0,0],color=BLUE)
       ncentrifugal_lab = TexMobject("Centrifugal Force").scale(0.5)       

       self.add(ntxt,narc,nbus)
       self.wait(3) #0:27

       ncentripetal_lab.next_to(ncentripetal, 0.5*TOP, buff=SMALL_BUFF)
       self.add(ncentripetal, ncentripetal_lab)
       

       self.wait(12) #0:39              
       ncentrifugal_lab.next_to(ncentrifugal, 0.5*TOP, buff=SMALL_BUFF)
       self.add(ncentrifugal, ncentrifugal_lab)

       self.wait(4)
       
