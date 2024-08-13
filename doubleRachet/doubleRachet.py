from manim import *

class DoubleRachet(Scene):
    def construct(self):
        # Create Alice and Bob
        alice = Text("Alice").shift(LEFT * 3)
        bob = Text("Bob").shift(RIGHT * 3)
        self.play(Write(alice), Write(bob))