"""The main Pong game"""

from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (NumericProperty, ObjectProperty,
                             ReferenceListProperty)
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongBall(Widget):
    """Represent the ball widget in the game"""

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        Adds behaviour to the ball object in the game by
        changing its position.
        """
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    """
    Represents the main game on the canvas.
    """

    ball = ObjectProperty(None)

    def serve_ball(self):
        """
        Anytime the game is started or a player scores a point
        a ball serve is done to give random motion to the static ball.
        """
        print('veer self.ball.center: ', self.ball.center)
        print('veer self.center: ', self.center)
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        """
        Simply updates the ball position by moving it.
        """

        self.ball.move()

        # bounce of top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        # bounce of left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
