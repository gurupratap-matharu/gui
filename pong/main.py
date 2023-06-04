"""The main Pong game"""

from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    """Represents a ping pong bat or a paddle in our lingo."""

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        """
        Bounces of the ball when the ball touches the paddle.
        """

        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)  # reverse direction
            vel = bounced * 1.1  # give a slight boost
            ball.velocity = vel.x, vel.y + offset  # offset ???


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
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        """
        Anytime the game is started or a player scores a point
        a ball serve is done to give random motion to the static ball.
        """

        self.ball.center = self.center
        self.ball.velocity = vel

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

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            # its a touch for the left player ;D
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            # its a touch for the right player ;D
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
