from manim import *

class X3DHVisualization(Scene):
    def construct(self):
        # Create Alice and Bob
        X3dh = Text("X3DH", font_size=35).shift(UP*2.5)
        alice = Text("Alice", font_size=30).shift(UP*2 + LEFT * 4)
        bob = Text("Bob", font_size=30).shift(UP*2 + RIGHT * 4)
        self.play(FadeIn(X3dh), FadeIn(alice), FadeIn(bob))
        self.wait(1)

        # Create Alice's Keys
        alice_keys = self.create_alice_keys(alice)
        self.play(*[FadeIn(key) for key in alice_keys])
        self.wait(1)

        # Create Bob's Keys
        bob_keys = self.create_bob_keys(bob)
        self.play(*[FadeIn(key) for key in bob_keys])
        self.wait(1)

        # Perform DH Computations
        self.perform_dh(alice_keys, bob_keys)

        SK = Text("SK = KDF(DH1 || DH2 || DH3 || DH4)", font_size=30).shift(DOWN*2.75)
        self.play(FadeIn(SK))
        self.wait(2)
        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])



    def create_alice_keys(self, alice):
        # Alice's Identity Key (IKa)
        ika_pub = self.create_key_box("IKa (Public)", alice, DOWN * 1)
        ika_priv = self.create_key_box("ika (Private)", ika_pub, DOWN * 0.8)

        # Alice's Ephemeral Key (EK)
        ek_pub = self.create_key_box("EKA (Public)", ika_priv, DOWN * 1.2)
        ek_priv = self.create_key_box("eka (Private)", ek_pub, DOWN * 0.8)

        return [ika_pub, ika_priv, ek_pub, ek_priv]

    def create_bob_keys(self, bob):
        # Bob's Identity Key (IKb)
        ikb_pub = self.create_key_box("IKb (Public)", bob, DOWN * 1)
        ikb_priv = self.create_key_box("ikb (Private)", ikb_pub, DOWN * 0.8)

        # Bob's Signed PreKey (SPKb)
        spkb_pub = self.create_key_box("SPKb (Public)", ikb_priv, DOWN * 1.2)
        spkb_priv = self.create_key_box("spkb (Private)", spkb_pub, DOWN * 0.8)

        # Bob's One-Time PreKey (OPKb)
        opkb_pub = self.create_key_box("OPKb (Public)", spkb_priv, DOWN * 1.2)
        opkb_priv = self.create_key_box("opkb (Private)", opkb_pub, DOWN * 0.8)

        return [ikb_pub, ikb_priv, spkb_pub, spkb_priv, opkb_pub, opkb_priv]

    def create_key_box(self, text, reference_mob, direction):
        box = Rectangle(height=0.5, width=3)
        label = Text(text, font_size=18)
        key_group = VGroup(box, label)
        key_group.next_to(reference_mob, direction, buff=0.2)
        return key_group

    def perform_dh(self, alice_keys, bob_keys):
        # DH1: Alice's ika (Private) -> Bob's SPKb (Public) 
        self.draw_arrow_and_label(alice_keys[1], bob_keys[2], "DH1: (ika → SPKb)")

        # DH2: Alice's eka (Private) -> Bob's IKb (Public)
        self.draw_arrow_and_label(alice_keys[3], bob_keys[0], "DH2: (eka → IKb)")

        # DH3: Alice's eka (Private) -> Bob's SPKb (Public)
        self.draw_arrow_and_label(alice_keys[3], bob_keys[2], "DH3: (eka → SPKb )")

        # DH4: Alice's eka (Private) -> Bob's OPKb (Public)
        self.draw_arrow_and_label(alice_keys[3], bob_keys[4], "DH4: (eka → OPKb)")

    def draw_arrow_and_label(self, start_key, end_key, label_text):
        start_box = start_key[0]
        end_box = end_key[0]

        # Draw the arrow
        arrow = Arrow(
            start=start_box.get_right(),
            end=end_box.get_left(),
            buff=0.1,
            stroke_width=2,
            color=YELLOW
        )
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Display the label below in larger font and cream color
        label = Text(label_text, font_size=30, color="#F5F5DC").next_to(arrow, DOWN, buff=0.2)
        self.play(FadeIn(label))
        self.wait(1)

        # Remove the arrow and label before drawing the next one
        self.play(FadeOut(arrow), FadeOut(label))
