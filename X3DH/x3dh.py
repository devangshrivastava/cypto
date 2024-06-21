from manim import *

class TripleDeffieHellman(Scene):
    def construct(self):
        # Create Alice and Bob
        alice = Text("Alice").shift(LEFT * 3)
        bob = Text("Bob").shift(RIGHT * 3)
        self.play(Write(alice), Write(bob))

        # Show Alice's keys
        alice_keys = self.create_keys("Alice", alice)
        self.play(Write(alice_keys))
        self.wait(2)

        # Show Bob's keys
        bob_keys = self.create_keys("Bob", bob)
        self.play(Write(bob_keys))
        self.wait(2)

        # Shift Alice and her keys
        self.play(alice.animate.shift(UP * 2 + LEFT * 1), alice_keys.animate.shift(UP * 2 + LEFT * 1))
        
        # Shift Bob and his keys
        self.play(bob.animate.shift(UP * 2 + RIGHT * 1), bob_keys.animate.shift(UP * 2 + RIGHT * 1))
        self.wait(2)

        # Create an arrow from Alice's IKa to Bob's EPK
        ika_public_box = alice_keys[1][0][0]  # Rectangle around "IKa (public)"
        epk_private_box = bob_keys[1][3][0]    # Rectangle around "EPK (public)"

        ika_private_box = alice_keys[1][1][0]  # Rectangle around "IKa (public)"
        epk_public_box = bob_keys[1][2][0]    # Rectangle around "EPK (public)"

        # self.draw_arrow_between_boxes_rl(ika_public_box, epk_private_box)
        # self.draw_arrow_between_boxes_lr(epk_public_box, ika_private_box)
        self.DH(ika_public_box, ika_private_box, epk_public_box, epk_private_box)

        self.wait(2)
    
    def create_keys(self, owner_name, owner_text):
        key_labels = [
            f"IK{owner_name[0].lower()} (public)",
            f"ik{owner_name[0].lower()} (private)",
            "EPK (public)",
            "epk (private)"
        ]
        
        keys = VGroup()
        for i, label in enumerate(key_labels):
            key_box = Rectangle(height=0.5, width=2.5)
            key_text = Text(label, font_size=18).move_to(key_box.get_center())
            key_group = VGroup(key_box, key_text)
            key_group.next_to(owner_text, DOWN, buff=1 + i * 0.6)
            keys.add(key_group)
        
        title_text = Text(f"{owner_name}'s Keys", font_size=24).next_to(keys, UP, buff=0.5)
        
        return VGroup(title_text, keys)

    def draw_arrow_between_boxes_rl(self, start_box, end_box, stroke_width=2):
        arrow = Arrow(start=start_box.get_right(), end=end_box.get_left(), buff=0.1, stroke_width=stroke_width)
        self.play(Create(arrow))

    def draw_arrow_between_boxes_lr(self, start_box, end_box, stroke_width=2):
        arrow = Arrow(start=start_box.get_left(), end=end_box.get_right(), buff=0.1, stroke_width=stroke_width)
        self.play(Create(arrow))

    def DH(self, key1_pub, key1_priv, key2_pub, key2_priv, stroke_width=2):
        arrow1 = Arrow(start=key1_pub.get_right(), end=key2_priv.get_left(), buff=0.1, stroke_width=stroke_width)
        arrow2 = Arrow(start=key2_pub.get_left(), end=key1_priv.get_right(), buff=0.1, stroke_width=stroke_width)
        self.play(Create(arrow1))
        self.wait(1)
        self.play(Create(arrow2))
        self.wait(1)

        diffie_hellman_text_1 = Text("Diffie-Hellman (EPK(public), IKa(private))", font_size=24).shift(DOWN * 2.5)
        diffie_hellman_text_2 = Text("Diffie-Hellman (EPK(private), IKa(public))", font_size=24).next_to(diffie_hellman_text_1, DOWN, buff=0.2) 
        self.play(Write(diffie_hellman_text_1))
        self.play(Write(diffie_hellman_text_2))
        self.wait(2)

        self.play(FadeOut(arrow1, arrow2, diffie_hellman_text_1, diffie_hellman_text_2))