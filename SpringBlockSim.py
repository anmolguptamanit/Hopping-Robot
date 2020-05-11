from Box2D.examples.framework import (Framework, main)
from Box2D import *
from Box2D import (b2EdgeShape, b2FixtureDef, b2PolygonShape, b2Random)


class Spring(Framework):
    name = "Spring"
    description = "A test for springs"

    def __init__(self):
        super(Spring, self).__init__()

        ground = self.world.CreateStaticBody(
            position=(0, 0),
            shapes=[b2EdgeShape(vertices=[(-50, 0), (50, 0)])],
        )

        self.bodyA = self.world.CreateDynamicBody(
            position=(0, 10),
            fixtures=b2FixtureDef(
                shape=b2PolygonShape(box=(1, 1)), density=1.0)
        )

        self.bodyB = self.world.CreateDynamicBody(
            position=(0, 5),
            fixtures=b2FixtureDef(
                shape=b2CircleShape(radius = 0.5), density=1.0, restitution=0)
        )

        dfn = b2DistanceJointDef(
            frequencyHz=2.5,
            dampingRatio=0,
            bodyA=self.bodyA,
            bodyB=self.bodyB,
            anchorA=(0, 10),
            anchorB=(0, 5),
            collideConnected=True
        )

        self.world.CreateJoint(dfn)

    def Step(self, settings):
        super(Spring, self).Step(settings)


if __name__ == "__main__":
    main(Spring)
