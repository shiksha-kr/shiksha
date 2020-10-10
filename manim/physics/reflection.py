#!/usr/bin/env python

from manimlib.imports import *

def MeasureArrow(sp, ep, txt):

    mp =[]
    for (s, e) in zip(sp, ep):
        mp.append((s+e)/2)
    
    la = Line(mp,sp,color=GREEN)
    la.add_tip(tip_length=0.1)
    
    ra = Line(mp,ep,color=GREEN)
    ra.add_tip(tip_length=0.1)
    
    ma = Group(la,ra)

    lab   = TexMobject(txt,buff=SMALL_BUFF).scale(0.5)
    lab.next_to(mp,0.1*UP)
    
    return(Group(ma,lab))

def parabola_func1(t):
    return np.array((t, np.sqrt(4*1.0*t), 0))

def parabola_func2(t):
    return np.array((t, -1*np.sqrt(4*1.0*t), 0)) 


class Spoon(Scene): # ANIM 0, ANIM 5
    def construct(self):
        spoon    = ImageMobject('D:/play/shiksha_env/photos/spoon.jpg')
        spoon.scale(2)
        self.add(spoon)
        #self.wait(40)
        self.wait(29)
        
class PlaneMirror(Scene): # ANIM 1

    def construct(self):

        mirror = Line([0.0,-2.0,0.0],[0.0,2.0,0.0],color=GRAY)

        src    = SmallDot(color=YELLOW)
        src.move_to([2.5,-1.5,0.0])
        axis   = DashedLine([0,0,0], [2.5,0,0])
        angle  = math.asin(1.25/2.5) # should be 1.5/2.5 but for better arc drawing made it 1.25/2.5
        
        iray   = Line([2.5,-1.5,0.0],[0.0,0.0,0.0],color=RED)
        iray.add_tip(tip_length=0.1)
        iarc   = Arc(radius=0.4, start_angle=-1*angle, angle=angle)
        iarc_lab   = TexMobject("\\theta",buff=SMALL_BUFF).scale(0.5)
        iarc_lab.next_to(iarc, RIGHT)

        rray   = Line([0.0,0.0,0.0],[2.5,1.5,0.0],color=RED)
        rray.add_tip(tip_length=0.1)        
        rarc   = Arc(radius=0.4, start_angle=0, angle=angle)
        rarc_lab   = TexMobject("\\theta",buff=SMALL_BUFF).scale(0.5)
        rarc_lab.next_to(rarc, RIGHT)        

        # wall and Ball
        wall = Line([3.0,-2.0,0.0],[3.0,2.0,0.0],color=GRAY)
        ball = Dot(color=RED).move_to([3.0,-2.0,0.0])
        l1 = Line([4.0,-2.0,0.0], [3.0,0.0,0.0])
        l2 = Line([3.0,0.0,0.0],[4.0,2.0,0.0])

        # Depth
        depth = MeasureArrow([0.0,-1.5,0.0],[2.5,-1.5,0.0],"d")

        # point src
        vsrc    = SmallDot(color=YELLOW)
        vsrc.move_to([-2.5,-1.5,0.0])        
        vray   = DashedLine([0.0,0.0,0.0],[-2.5,-1.5,0.0],color=RED)
        vdepth = MeasureArrow([0.0,-1.5,0.0],[-2.5,-1.5,0.0],"d")        

        # Submarine Periscope
        periscope    = ImageMobject('D:/play/shiksha_env/photos/submarine_periscope.jpg').scale(2)
        attribution1 = TextMobject('Courtesy: https://www.archives.gov/research/military/ww2/photos/images/thumbnails/ww2-58-l.jpg').scale(0.2)
        attribution1.move_to(2*DOWN)

        kscope       = ImageMobject('D:/play/shiksha_env/photos/640px-Kaleidoscope_2.jpg')
        attribution2 = TextMobject('Courtesy: https://commons.wikimedia.org/wiki/User:Hide-sp').scale(0.2)
        attribution2.move_to(2*DOWN)        
        
        # actual animation
        self.add(mirror, src)        
        self.wait(3)
        
        self.add(iray)        
        self.wait(11)
        self.add(iarc, iarc_lab)  #0:14

        self.wait(3)
        self.add(rray, rarc, rarc_lab) #0:17

        self.wait(2) 
        self.add(axis) #0:19                
        self.wait(11)                

        self.add(wall) #0:30
        self.play(MoveAlongPath(ball,l1),run_time=3.0, rate_func=linear)
        self.play(MoveAlongPath(ball,l2),run_time=3.0, rate_func=linear)                                      
        self.wait(1)
        self.remove(wall, ball) #0:37
        self.wait(4)
        
        self.add(depth)  #0:41
        self.wait(5)

        self.add(vsrc, vray, vdepth)  #0:46
        self.wait(5)                                

        self.remove(axis, iray, iarc, iarc_lab, rray, rarc, rarc_lab, depth, vsrc, vray, vdepth, mirror, src) #0:51
        self.add(periscope, attribution1)
        self.wait(5)
        self.remove(periscope, attribution1)        
        self.add(kscope,attribution2)
        self.wait(8)
        

        
class ConcaveMirrorOld(GraphScene):

    def construct(self):
        parab_u = ParametricFunction(parabola_func1, t_max=0.3,fill_opacity=0, color=GRAY)
        parab_l = ParametricFunction(parabola_func2, t_max=0.3,fill_opacity=0, color=GRAY)        
        axis    = DashedLine([0,0,0], [2.5,0,0])
        fp      = SmallDot(color=YELLOW).move_to([0.5,0,0])
        fp_lab  = TexMobject("F",buff=SMALL_BUFF).scale(0.5)
        fp_lab.move_to([0.5,-0.1,0])
        
        circle = Circle(radius=1.0).move_to([1.0,0,0])
        
        self.play(ShowCreation(parab_u),
                  ShowCreation(parab_l),
        )
        self.wait(3)
        self.add(axis, fp, fp_lab)
        self.wait(3)

        iray   = Line([2.0,0.5,0.0],[0.125,0.5,0.0],color=RED)
        self.add(iray)
        rray   = Line([0.125,0.5,0.0],[0.5,0,0],color=RED)
        self.add(rray)
        

        
        #self.add(circle)
        self.wait(3)        



class ConcaveMirror0(Scene): # ANIM 2

    def construct(self):
        parab_u = ParametricFunction(parabola_func1, t_max=0.35,fill_opacity=0, color=GRAY)
        parab_l = ParametricFunction(parabola_func2, t_max=0.35,fill_opacity=0, color=GRAY)        
        axis    = DashedLine([0,0,0], [2.5,0,0])
        fp      = SmallDot(color=YELLOW).move_to([1.0,0,0])
        fp_lab  = TexMobject("F",buff=SMALL_BUFF).scale(0.5)
        fp_lab.move_to([1.0,-0.1,0])
        
        self.play(ShowCreation(parab_u),
                  ShowCreation(parab_l),
        )
        self.wait(3)
        self.add(axis, fp, fp_lab)
        #self.play(FocusOn(fp,color=YELLOW))
        
        self.wait(7) #0:10

        # forward ray traces
        iray   = Line([2.0,1.0,0.0],[0.25,1.0,0.0],color=RED)
        iray.add_tip(tip_length=0.1)
        self.add(iray)
        self.wait(1)                                
        tgnt = Line([0.0,0.5,0],[0.5,1.5,0]) # eqn: y=2x+0.5
        self.add(tgnt)
        self.wait(1)
        nrml = Line([0.25,1.0,0],[1.0,0.625,0]) # eqn: y=-0.5x+1.125
        self.add(nrml)
        self.wait(3) #0:15        
        rray   = Line([0.25,1.0,0.0],[1.0,0,0],color=RED)
        rray.add_tip(tip_length=0.1)
        #self.add(rray)
        self.play(ShowCreation(rray), Flash(fp,color=YELLOW))
        self.wait(1)                

        angle      = math.atan(-0.5)      # slope of normal is used in calc
        iarc       = Arc(radius=0.3, start_angle=0, angle=angle).move_arc_center_to([0.25,1.0,0])
        iarc_lab   = TexMobject("\\theta_i",buff=SMALL_BUFF).scale(0.5)
        iarc_lab.next_to(iarc, RIGHT)
        rarc       = Arc(radius=0.3, start_angle=angle, angle=angle).move_arc_center_to([0.25,1.0,0])
        rarc_lab   = TexMobject("\\theta_r",buff=SMALL_BUFF).scale(0.5)
        rarc_lab.next_to(rarc, DOWN)
        self.add(iarc,iarc_lab, rarc, rarc_lab)
        self.wait(1) #0:17        

        # reverse ray traces
        self.remove(iray, rray, tgnt, nrml, iarc, iarc_lab, rarc, rarc_lab)
        self.wait(1) #0:18
        iray1   = Line([1.0,0,0],[0.25,1.0,0.0],color=RED)
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(2)                                

        self.add(tgnt,nrml)
        self.wait(3) #0:23
        
        rray1   = Line([0.25,1.0,0.0],[2.0,1.0,0.0],color=RED)
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(9) #0:32
        
        iarc       = Arc(radius=0.3, start_angle=angle, angle=angle).move_arc_center_to([0.25,1.0,0])
        iarc_lab.next_to(iarc, DOWN)
        rarc       = Arc(radius=0.3, start_angle=0, angle=angle).move_arc_center_to([0.25,1.0,0])
        rarc_lab.next_to(rarc, RIGHT)
        self.add(iarc,iarc_lab, rarc, rarc_lab)        
        self.wait(7) #0:39                

        # circular arc
        self.remove(tgnt,nrml,iray,rray,iarc,iarc_lab,rarc,rarc_lab)        
        circle = Circle(radius=2.0, color=GREEN).move_to([2.0,0,0])
        center = SmallDot(color=YELLOW).move_to([2,0,0])
        self.add(center,circle) #0:40
        self.wait(3)

        #self.remove(parab_u,parab_l)
        #carc = Arc(radius=2.0, arc_center=[2.0,0,0], start_angle=3*PI/4, angle=PI/2, color=RED)
        carc = Arc(radius=2.0, arc_center=[2.0,0,0], start_angle=143*DEGREES, angle=74*DEGREES, color=GRAY)
        self.add(carc)
        self.wait(3) #0:46
        self.remove(circle)
        self.wait(1)
        self.remove(parab_u,parab_l) #0:47
        self.wait(8)        


class ConcaveMirror1(Scene): # ANIM 3

    def construct(self):
        
        carc = Arc(radius=2.0, arc_center=[2.0,0,0], start_angle=143*DEGREES, angle=74*DEGREES, color=GRAY)
        cp      = SmallDot(color=YELLOW).move_to([2,0,0])
        cp_lab  = TexMobject("C",buff=SMALL_BUFF).scale(0.5)
        cp_lab.move_to([2.0,-0.2,0])                
        axis    = DashedLine([0,0,0], [2.5,0,0])
        fp      = SmallDot(color=YELLOW).move_to([1.0,0,0])
        fp_lab  = TexMobject("F",buff=SMALL_BUFF).scale(0.5)
        fp_lab.move_to([1.0,-0.2,0])        

        headlight        = ImageMobject('D:/play/shiksha_env/photos/car_headlight.jpg').scale(2)
        headlight_attrib = TextMobject('Courtesy: https://nohat.cc/f/vintage-car-close-up-free-public-domain-photo-560200/comrawpixel560200-201907170208.html').scale(0.2)
        headlight.move_to(LEFT*2)
        headlight_attrib.move_to(2.5*DOWN+2*LEFT)

        telescope        = ImageMobject('D:/play/shiksha_env/photos/cel_telescope.jpg').scale(1.5)
        #telescope_attrib = TextMobject('Courtesy: https://en.wikipedia.org/wiki/Vainu_Bappu_Observatory#/media/File:93-inch_telescope_seen_from_the_40-inch_telescope_at_Vainu_Bappu_Observatory.JPG').scale(0.2)
        telescope_attrib = TextMobject('Courtesy: Prateek Karandikar').scale(0.2)
        telescope.move_to(RIGHT*2)
        telescope_attrib.move_to(2.5*DOWN+2*RIGHT)
        
        self.add(carc, axis, cp, fp, cp_lab, fp_lab)
        self.wait(2)

        # Generic Placement of obj(between C and F)
        obj = Line([1.5,0,0], [1.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) 
        self.wait(14)

        iray1   = Line([1.5,0.6,0.0],[0.1,0.6,0.0],color=RED)
        iray1.add_tip(tip_length=0.1)
        self.add(iray1) #0:16
        self.wait(1)                  

        rray1   = Line([0.1,0.6,0.0],[2.5,-1.0,0],color=RED)
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(9)           

        iray2   = Line([1.5,0.6,0.0],[0.22,-0.95,0.0],color=BLUE)
        iray2.add_tip(tip_length=0.1)
        self.add(iray2) #0:26
        self.wait(1)

        rray2   = Line([0.22,-0.95,0.0], [2.45,-0.95,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        self.wait(1)                                  

        #img = Line([5/3,0,0], [5/3, -0.4, 0], color=PURPLE).add_tip(tip_length=0.1)
        img = Line([2.45,0,0], [2.45, -0.95, 0], color=PURPLE).add_tip(tip_length=0.12)
        self.add(img) 
        self.wait(23)        

        self.remove(obj, iray1, rray1, iray2, rray2, img)

        
        # beyond C
        obj = Line([2.5,0,0], [2.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) #0:51
        self.wait(2)

        iray1   = Line([2.5,0.6,0.0],[0.1,0.6,0.0],color=RED)
        iray1.add_tip(tip_length=0.1)
        self.add(iray1) 
        self.wait(1)                  

        rray1   = Line([0.1,0.6,0.0],[2.5,-1.0,0],color=RED)
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(1)           


        iray2   = Line([2.5,0.6,0.0],[0.05,-0.4,0.0],color=BLUE)
        iray2.add_tip(tip_length=0.1)
        self.add(iray2) 
        self.wait(1)

        rray2   = Line([0.05,-0.4,0.0], [2.5,-0.4,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        self.wait(1)                                  

        #img = Line([5/3,0,0], [5/3, -0.4, 0], color=PURPLE).add_tip(tip_length=0.1)
        img = Line([1.6,0,0], [1.6, -0.4, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(img)
        self.wait(1)        


        # between C and F
        self.remove(obj, iray1, rray1, iray2, rray2, img)
        obj = Line([1.5,0,0], [1.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) #0:58
        self.wait(2)

        iray1   = Line([1.5,0.6,0.0],[0.1,0.6,0.0],color=RED)
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(1)                  

        rray1   = Line([0.1,0.6,0.0],[2.5,-1.0,0],color=RED)
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(2)           


        iray2   = Line([1.5,0.6,0.0],[0.22,-0.95,0.0],color=BLUE)
        iray2.add_tip(tip_length=0.1)
        self.add(iray2)
        self.wait(1)

        rray2   = Line([0.22,-0.95,0.0], [2.45,-0.95,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        self.wait(1)                                  

        #img = Line([5/3,0,0], [5/3, -0.4, 0], color=PURPLE).add_tip(tip_length=0.1)
        img = Line([2.45,0,0], [2.45, -0.95, 0], color=PURPLE).add_tip(tip_length=0.12)
        self.add(img) 
        self.wait(1)        


        # between F and O
        self.remove(axis, obj, iray1, rray1, iray2, rray2, img)
        axis    = DashedLine([-2.5,0,0], [2.5,0,0])
        obj = Line([0.5,0,0], [0.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(axis, obj) #1:06
        self.wait(2)

        iray1   = Line([0.5,0.6,0.0],[0.1,0.6,0.0],color=RED) # parallel eqn: y=0.6
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(1)                  

        rray1   = Line([0.1,0.6,0.0],[2.5,-1.0,0],color=RED) # eqn: y=-0.661x + 0.661
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(3)           


        iray2   = Line([1.0,0,0.0], [0.228,0.927,0.0], color=BLUE) # eqn y = -1.2x+1.2
        iray2.add_tip(tip_length=0.1)
        self.add(iray2)
        self.wait(1)

        rray2   = Line([0.228,0.927,0.0], [2,0.927,0.0],color=BLUE)  # parallel eqn: y=0.927
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        self.wait(1)                                  

        # extend rays behind mirror with dashed lines
        rray1d   = DashedLine([0.092,0.6,0.0],[-1.5,1.652,0],color=RED)
        self.add(rray1d)
        self.wait(1)

        rray2d   = DashedLine([0.268,0.927,0.0],[-2,0.927,0],color=BLUE)
        self.add(rray2d)
        self.wait(1)                   
        
        img = Line([-0.403,0,0], [-0.403, 0.927, 0], color=PURPLE).add_tip(tip_length=0.12)
        self.add(img) #1:16

        self.wait(19)
        self.remove(axis, carc, cp, cp_lab, fp, fp_lab, obj, iray1, rray1, iray2, rray2, rray1d, rray2d, img)        
        self.add(headlight, headlight_attrib) # 1:35
        
        self.wait(11)                
        self.add(telescope, telescope_attrib) # 1:46

        self.wait(11)        
        #1:57
        
class ConvexMirror(Scene): # ANIM 4

    def construct(self):
        
        #carc = Arc(radius=2.0, arc_center=[-2.0,0,0], start_angle=143*DEGREES, angle=74*DEGREES, color=GRAY)
        carc = Arc(radius=2.0, arc_center=[-2.0,0,0], start_angle=-37*DEGREES, angle=74*DEGREES, color=GRAY)
        axis    = DashedLine([-2.5,0,0], [2.5,0,0])

        cp      = SmallDot(color=YELLOW).move_to([-2,0,0])
        cp_lab  = TexMobject("C",buff=SMALL_BUFF).scale(0.5)
        cp_lab.move_to([-2.0,-0.2,0])                

        fp      = SmallDot(color=YELLOW).move_to([-1.0,0,0])
        fp_lab  = TexMobject("F",buff=SMALL_BUFF).scale(0.5)
        fp_lab.move_to([-1.0,-0.2,0])        

        cpp      = SmallDot(color=YELLOW).move_to([2,0,0])
        cpp_lab  = TexMobject("C'",buff=SMALL_BUFF).scale(0.5)
        cpp_lab.move_to([2.0,-0.2,0])                

        fpp      = SmallDot(color=YELLOW).move_to([1.0,0,0])
        fpp_lab  = TexMobject("F'",buff=SMALL_BUFF).scale(0.5)
        fpp_lab.move_to([1.0,-0.2,0])        

        
        self.add(carc, axis, cp, fp, cp_lab, fp_lab, cpp, fpp, cpp_lab, fpp_lab)
        self.wait(9)

        # beyond C'
        obj = Line([2.5,0,0], [2.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) #0:09
        self.wait(1)

        iray1   = Line([2.5,0.6,0.0],[-0.092,0.6,0.0],color=RED)
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(1)                  

        rray1   = Line([-0.092,0.6,0.0],[2.0,1.983,0],color=RED)
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        #self.wait(1)
        rray1d   = DashedLine([-0.092,0.6,0.0],[-1.0,0,0],color=RED)
        #rray1.add_tip(tip_length=0.1)
        self.add(rray1d)
        self.wait(1)    
        

        iray2   = Line([2.5,0.6,0.0],[-0.007,0.17,0.0],color=BLUE)
        iray2.add_tip(tip_length=0.1)
        self.add(iray2)
        self.wait(1)                  

        rray2   = Line([-0.007,0.17,0.0],[3.0,0.17,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        #self.wait(1)
        rray2d   = DashedLine([-0.007,0.17,0.0],[-2.5,0.17,0.0],color=BLUE)
        #rray2d.add_tip(tip_length=0.1)
        self.add(rray2d)
        self.wait(1)            
        
        img = Line([-0.743,0,0], [-0.743, 0.17, 0], color=PURPLE).add_tip(tip_length=0.05)
        self.add(img)
        self.wait(4)  


        # between C' and F'
        self.remove(obj, iray1, rray1, rray1d, iray2, rray2, rray2d, img)        #0:18
        self.wait(2)
        obj = Line([1.5,0,0], [1.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) #0:20
        self.wait(1)

        iray1   = Line([1.5,0.6,0.0],[-0.092,0.6,0.0],color=RED) # parallel y=0.6
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(1)                  

        rray1   = Line([-0.092,0.6,0.0],[2.0,1.983,0],color=RED) # eqn: y=0.661x+0.661
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        #self.wait(1)
        rray1d   = DashedLine([-0.092,0.6,0.0],[-1.0,0,0],color=RED)
        #rray1.add_tip(tip_length=0.1)
        self.add(rray1d)
        self.wait(1)    
        

        iray2   = Line([1.5,0.6,0.0],[-0.014,0.237,0.0],color=BLUE) # eqn: y=0.24x+0.24
        iray2.add_tip(tip_length=0.1)
        self.add(iray2)
        self.wait(1)                  

        rray2   = Line([-0.014,0.237,0.0],[2.5,0.237,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        #self.wait(1)
        rray2d   = DashedLine([-0.014,0.237,0.0],[-2.5,0.237,0.0],color=BLUE)
        #rray2d.add_tip(tip_length=0.1)
        self.add(rray2d)
        self.wait(1)            
        
        img = Line([-0.641,0,0], [-0.642, 0.237, 0], color=PURPLE).add_tip(tip_length=0.08)
        self.add(img)
        self.wait(3)  


        # between F' and the Mirror
        self.remove(obj, iray1, rray1, rray1d, iray2, rray2, rray2d, img)        #0:28
        self.wait(2)        
        obj = Line([0.5,0,0], [0.5, 0.6, 0], color=PURPLE).add_tip(tip_length=0.1)
        self.add(obj) #0:30
        self.wait(1)

        iray1   = Line([0.5,0.6,0.0],[-0.092,0.6,0.0],color=RED) # parallel y=0.6
        iray1.add_tip(tip_length=0.1)
        self.add(iray1)
        self.wait(1)                  

        rray1   = Line([-0.092,0.6,0.0],[2.0,1.983,0],color=RED) # eqn: y=0.661x+0.661
        rray1.add_tip(tip_length=0.1)
        self.add(rray1)
        self.wait(1)
        rray1d   = DashedLine([-0.092,0.6,0.0],[-1.0,0,0],color=RED)
        #rray1.add_tip(tip_length=0.1)
        self.add(rray1d)
        self.wait(1)    
        

        iray2   = Line([0.5,0.6,0.0],[-0.037,0.386,0.0],color=BLUE) # eqn: y=0.4x+0.4
        iray2.add_tip(tip_length=0.1)
        self.add(iray2)
        self.wait(1)                  

        rray2   = Line([-0.037,0.386,0.0],[2.5,0.386,0.0],color=BLUE)
        rray2.add_tip(tip_length=0.1)
        self.add(rray2)
        self.wait(1)
        rray2d   = DashedLine([-0.037,0.386,0.0],[-2.5,0.386,0.0],color=BLUE)
        #rray2d.add_tip(tip_length=0.1)
        self.add(rray2d)
        self.wait(1)            
        
        img = Line([-0.416,0,0], [-0.416, 0.386, 0], color=PURPLE).add_tip(tip_length=0.08)
        self.add(img)
        self.wait(8)  
        #0:44
        

class Summary(Scene): # ANIM 6

    def construct(self):

        lor         =  TextMobject("+ Mirrors Reflect According to the Law of Reflection",buff=SMALL_BUFF, color=YELLOW).move_to(2.1*UP)
        lor_d       =  TextMobject("+ Mirrors Reflect According to the Law of Reflection",buff=SMALL_BUFF).move_to(2.1*UP)        
        
        eq_angle    =  TextMobject("+ Reflected Angle = Incident Angle",buff=SMALL_BUFF, color=YELLOW).move_to(1.4*UP)
        eq_angle_d  =  TextMobject("+ Reflected Angle = Incident Angle",buff=SMALL_BUFF).move_to(1.4*UP)        

        mirr_type   =  TextMobject("+ Common Mirror Types: Plane, Concave and Convex",buff=SMALL_BUFF, color=YELLOW).move_to(0.7*UP)
        mirr_type_d =  TextMobject("+ Common Mirror Types: Plane, Concave and Convex",buff=SMALL_BUFF).move_to(0.7*UP)        
        
        img_type    =  TextMobject("+ Plane and Convex Mirrors: Virtual Images",buff=SMALL_BUFF, color=YELLOW)
        img_type_d  =  TextMobject("+ Plane and Convex Mirrors: Virtual Images",buff=SMALL_BUFF)        

        img_type1   =  TextMobject("+ Concave Mirrors: - Real Images if Object is beyond focal point",buff=SMALL_BUFF, color=YELLOW).move_to(0.7*DOWN)
        img_type1_d =  TextMobject("+ Concave Mirrors: - Real Images if Object is beyond focal point",buff=SMALL_BUFF).move_to(0.7*DOWN)        

        img_type2   =  TextMobject("                   - Virtual Image if Object is between mirror and focal point",buff=SMALL_BUFF, color=YELLOW).move_to(1.4*DOWN)
        img_type2_d =  TextMobject("                   - Virtual Image if Object is between mirror and focal point",buff=SMALL_BUFF).move_to(1.4*DOWN)        

        ray_diag   =  TextMobject("+ Image Formation is analyzed using Ray Diagrams",buff=SMALL_BUFF, color=YELLOW).move_to(2.1*DOWN)
        ray_diag_d =  TextMobject("+ Image Formation is analyzed using Ray Diagrams",buff=SMALL_BUFF).move_to(2.1*DOWN)        

        lor.scale(0.75)
        lor_d.scale(0.75)        

        mirr_type.scale(0.75)
        mirr_type_d.scale(0.75)

        eq_angle.scale(0.75)
        eq_angle_d.scale(0.75)                
        
        img_type.scale(0.75)
        img_type_d.scale(0.75)

        img_type1.scale(0.75)
        img_type1_d.scale(0.75)                                

        img_type2.scale(0.75)
        img_type2_d.scale(0.75)

        ray_diag.scale(0.75)
        ray_diag_d.scale(0.75)                                

        self.wait(2)        
        self.play(Write(lor)) # 0:02
        self.wait(3)

        self.play(ReplacementTransform(lor, lor_d), # 0:07
                  Write(eq_angle))
        self.wait(1)

        self.play(ReplacementTransform(eq_angle, eq_angle_d), # 0:10
                                    Write(mirr_type))
        self.wait(13)

        self.play(ReplacementTransform(mirr_type, mirr_type_d), #0:26 
                  Write(img_type))
        self.wait(2)


        self.play(ReplacementTransform(img_type, img_type_d), #0:30
                  Write(img_type1))
        self.wait(2)

        self.play(ReplacementTransform(img_type1, img_type1_d), #0:33
                  Write(img_type2))
        self.wait(2)

        self.play(ReplacementTransform(img_type2, img_type2_d), #0:38
                  Write(ray_diag))
        self.wait(2)                                        
        self.play(ReplacementTransform(ray_diag, ray_diag_d))# 0:41
        self.wait(1)                                        
        #0:43





















        
