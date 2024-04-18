from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import *



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # Set up the GeoMipTerrain
        terrain = GeoMipTerrain("myDynamicTerrain")
        terrain.setHeightfield("heightmap.png")

        # Set terrain properties
        terrain.setBlockSize(32)
        terrain.setNear(40)
        terrain.setFar(100)
        terrain.setFocalPoint(base.camera)
        
        # Store the root NodePath for convenience
        root = terrain.getRoot()
        root.reparentTo(render)
        root.setSz(100)

        # Generate it.
        terrain.generate()

        # Add a task to keep updating the terrain
        def updateTask(task):
            terrain.update()
            return task.cont
        taskMgr.add(updateTask, "update")
        plight = PointLight('plight')
        plight.setColor((0.2, 0.2, 0.2, 1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(10, 20, 0)
        render.setLight(plnp)


    
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        self.camera.setPos(self.pandaActor.get_pos())
        self.camera.setHpr(self.pandaActor.get_hpr()*-1)
        return Task.cont



app = MyApp()

app.run()