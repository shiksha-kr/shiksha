import sys
sys.path.append("C:\manim\manim-master\manim")

from manimlib.imports import *


#############################################################
# parametric function
#############################################################
def lissajous_curve_func(t):
    return np.array((np.sin(2 * t), np.sin(3 * t), 0))


class ParamFunc(Scene):

    def construct(self):
        func = ParametricFunction(lissajous_curve_func, t_max=TAU, fill_opacity=0.5)
        dot = Dot()
        self.add(dot)
        self.add(func)
        self.wait(3)
        self.remove(dot)
        self.wait(1)


#############################################################
# Grouping Mobjects
#############################################################
class MobjGroup(Scene):

    def construct(self):
        body     = Rectangle(height=1.5,width=1.0)
        head     = Polygon([-0.5, 0.75, 0], [0.5, 0.75, 0], [0, 1.25, 0], color=GRAY)
        trail1   = Line([0.0,-0.75,0.0],[0.0,-0.95,0.0],color=RED)
        trail2   = Line([0.25,-0.75,0.0],[0.30,-0.85,0.0],color=RED)
        trail3   = Line([-0.25,-0.75,0.0],[-0.30,-0.85,0.0],color=RED)                
        head.set_fill(GRAY, opacity=1.0)
        rocket   = Group(body,head,trail1,trail2,trail3)

        path     = Line([0,0,0],[0,2,0])
        self.play(MoveAlongPath(rocket,path,run_time=5))





#############################################################
# Update Functions
#############################################################        
class MovingLabel(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT*5,buff=SMALL_BUFF)
        path     = Line([0,0,0],[0,2,0])
        
        self.add(dot,text)

        def update_text(obj):
            obj.next_to(dot,RIGHT*5,buff=SMALL_BUFF)

        # Only works in play
        self.play((MoveAlongPath(dot,path,run_time=5)),
                  #Rotating(text,radians=TAU,about_point=text.get_center(),run_time=5),
                  UpdateFromFunc(text,update_text)
            )

        self.wait()


#############################################################
# DrawTrail
#############################################################        
class DrawTrail(Scene):
    def construct(self):
        dot    = Dot(color=RED)
        path   = Line(ORIGIN, UP)
        trace  = Line(ORIGIN, ORIGIN, color=YELLOW)
        
        def trace_update(mob):
            trace =    mob
            new_trace = Line(ORIGIN,dot.get_center(),color=YELLOW)
            trace.become(new_trace)

        trace.add_updater(trace_update)
        self.add(dot,trace)

        self.play(MoveAlongPath(dot,path,run_time=5))

        self.wait()        


#############################################################
# DrawTrail2
#############################################################        
class DrawTrail2(Scene):
    def construct(self):
        dot    = Dot(color=RED)
        path   = Arc(radius=3,start_angle=0,angle=PI/4)
        trace  = Arc(radius=3,start_angle=0,angle=0)
        
        def trace_update(mob):
            trace = mob
            theta = np.arctan(dot.get_center()[1]/dot.get_center()[0])
            new_trace = Arc(radius=3,start_angle=0,angle=theta, color=YELLOW)
            trace.become(new_trace)

        trace.add_updater(trace_update)
        self.add(dot,trace)

        self.play(MoveAlongPath(dot,path,run_time=5))

        self.wait()        


#############################################################
# DrawTrail3
#############################################################        
def nifpath_func(t):
    return np.array((0.05*t, -0.5*0.00375*t*t, 0))

class Idx:
    i = 0

class DrawTrail3(Scene):
    def construct(self):
        dot    = Dot(color=RED)
        path   = ParametricFunction(nifpath_func, t_max=20, fill_opacity=0)
        trace  = ParametricFunction(nifpath_func, t_max=0.1, fill_opacity=0, color=YELLOW)

        idx = Idx()

        def trace_update(mob):
            trace = mob
            new_trace = ParametricFunction(nifpath_func, t_max=1, fill_opacity=0, color=GREEN)
            new_trace.points = []
            #trace.copy(new_trace) 
            np.append(new_trace.points,path.points[0:idx.i])
            idx.i=idx.i+1
            trace.become(new_trace)

        trace.add_updater(trace_update)
        self.add(dot,trace)

        self.play(MoveAlongPath(dot,path,run_time=5))

        self.wait()        
        
        
        

#############################################################
# TriangleScene
#############################################################                
class TriangleScene(Scene):
    def construct(self):
        circle = Circle(radius=3)
        base_line = Line(ORIGIN,RIGHT*3,color=ORANGE)
        side_1 = Line(ORIGIN,RIGHT*3,color=BLUE)
        side_2 = Line(RIGHT*3,RIGHT*3,color=PURPLE)
        sides = VGroup(side_1,side_2)
        
        def triangle_update(mob):
            side_1,side_2 = mob
            new_side_1 = Line(ORIGIN,circle.points[-1],color=BLUE)
            new_side_2 = Line(RIGHT*3,circle.points[-1],color=PURPLE)
            side_1.become(new_side_1)
            side_2.become(new_side_2)

        sides.add_updater(triangle_update)
        self.add(base_line,sides)
        self.play(ShowCreation(circle,run_time=3))

        self.wait()        

        
        
#############################################################
# Moving Camera
#############################################################                
class Jnk(MovingCameraScene):    
    def construct(self):        
        cube = Cube()
        cube.move_to([2,0,0])
        self.add(cube)
        self.wait(2)
        self.camera_frame.save_state()

        self.play(
            # Move the camera to the object
            self.camera_frame.move_to,cube,
            Rotating(cube,radians=1.0*TAU,about_point=ORIGIN,run_time=10),
        )
        self.wait(2)
        
        # Restore the state saved
        self.play(Restore(self.camera_frame))        
        self.wait(2)

class BlackScreen(Scene):    
    def construct(self):        
        self.wait(210)        
