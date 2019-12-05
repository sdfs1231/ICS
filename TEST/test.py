import re

from asciimatics.effects import Julia, Clock,Cog,Print
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
import sys
form_data = {
    "TA": ["Hello world!", "How are you?"],
    "TB": "alphabet",
    "TC": "123",
    "TD": "a@b.com",
    "Things": 2,
    "CA": False,
    "CB": True,
    "CC": False,
}
global InsertNum,QueryNum,FlightlistNum,BlankNum,ExistNum

class AnimationFrame(Frame):
    def __init__(self, screen, x, y):
        super(AnimationFrame, self).__init__(screen, width=screen.width//2,height=screen.height//2,
                                         name="Clock",can_scroll=False,
                                         x=x, y=y)
        self.set_theme("bright")
        #effects=[]add effect one by one
        self.add_effect(Cog(self._canvas, 0, 0, self._canvas.width//4),
                 )
        self.add_effect(Cog(self._canvas, self._canvas.width, self._canvas.height, self._canvas.width // 4,
            direction=-1))
        self.set_theme("bright")
        self.fix()


class Sum_Frame(Frame):
    def __init__(self,screen,x,y):
        super(Sum_Frame,self).__init__(screen,width=screen.width//2,height=screen.height//2,name="test",
                                       title="Summary",
                                       x=x,y=y,
                                       can_scroll=True
                                       )
        self.InsertNum = 0
        self.QueryNum = 0
        self.FlightlistNum = 0
        self.BlankNum = 0
        self.ExistNum = 0
        self._last_frame = 0
        self._sort = 5
        self._reverse = True
        self.set_theme('bright')
        layout=Layout([30,1])
        self.add_layout(layout)

        layout.add_widget(
            Text(label="InsertNum: %d"%self.InsertNum,),0)
        layout.add_widget(
            Text(label="QueryNum: %d"%self.QueryNum,), 0)
        layout.add_widget(
            Text(label="BlankNum: %d"%self.BlankNum,), 0)
        layout.add_widget(
            Text(label="ExistNum: %d"%self.ExistNum,),0)
        layout.add_widget(
            Text(label="FlightNum: %d"%self.FlightlistNum,), 0)
        self.fix()

    def _update(self, frame_no):
        if frame_no - self._last_frame >= self.frame_update_count or self._last_frame == 0:
            self._last_frame = frame_no
            self.InsertNum += 1
            self.QueryNum += 1
            self.FlightlistNum += 1
            self.BlankNum += 1
            self.ExistNum += 1
        super(Sum_Frame,self)._update(frame_no)

    @property
    def frame_update_count(self):
        # Refresh once every 2 seconds by default.
        return 20



class Warning_Frame(Frame):
    def __init__(self,screen,x,y):
        super(Warning_Frame,self).__init__(screen,width=screen.width,height=screen.height//2,name='logtextbox',
                                           x=x,
                                           y=y)
        self.set_theme("bright")
        layout=Layout([1,18])
        self.add_layout(layout)
        layout.add_widget(TextBox(height=1,),1)
        layout.add_widget(
            Text(label="Warning:",
                 name="TC",
                 validator="^[0-9]*$"), 1)
        self.fix()
        #layout.add_widget(Divider(height=1),1)


def demo(screen, scene):
    scenes = []
    effects = [
        Sum_Frame(screen, screen.width//2, 0),

        AnimationFrame(screen,0,0),
        Warning_Frame(screen,0,screen.height//2),

    ]
    scenes.append(Scene(effects, -1))
    AnimationFrame._update(AnimationFrame(screen,0,0),0)

    screen.play(scenes, stop_on_resize=True, start_scene=scene)

last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
