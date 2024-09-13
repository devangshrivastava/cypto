from manim import *

class DoubleRatchetAnimation(Scene):

    def KDF(self):
        input_box = RoundedRectangle(corner_radius=0.2, width=1.5, height=0.75, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        input_text = Text("Input", font_size=24).move_to(input_box.get_center())
        input_group = VGroup(input_box, input_text).to_edge(LEFT)

        # Create the KDF box and label
        kdf_box = RoundedRectangle(corner_radius=0.2, width=1.5, height=1, color=GREY, fill_color=GREY, fill_opacity=1)
        kdf_text = Text("KDF", font_size=24).move_to(kdf_box.get_center())
        kdf_group = VGroup(kdf_box, kdf_text).next_to(input_group, RIGHT, buff=2)

        # Create the KDF key input with filled color and black text inside
        kdf_key_input_box = RoundedRectangle(corner_radius=0.2, width=1.5, height=0.75, color=RED, fill_color=RED, fill_opacity=1)
        kdf_key_input_text = Text("KDF key", font_size=24, color=BLACK).move_to(kdf_key_input_box.get_center())
        kdf_key_input_group = VGroup(kdf_key_input_box, kdf_key_input_text).move_to(kdf_group.get_top() + UP * 1.5)

        # Create the KDF key output with filled color and black text inside
        kdf_key_output_box = RoundedRectangle(corner_radius=0.2, width=1.5, height=0.75, color=RED, fill_color=RED, fill_opacity=1)
        kdf_key_output_text = Text("KDF key", font_size=24, color=BLACK).move_to(kdf_key_output_box.get_center())
        kdf_key_output_group = VGroup(kdf_key_output_box, kdf_key_output_text).next_to(kdf_group, DOWN, buff=1)

        # Create the Output key with filled color and black text inside
        output_key_box = RoundedRectangle(corner_radius=0.2, width=2, height=0.75, color=RED, fill_color=RED, fill_opacity=1)
        output_key_text = Text("Output key", font_size=24, color=BLACK).move_to(output_key_box.get_center())
        output_key_group = VGroup(output_key_box, output_key_text).next_to(kdf_group.get_bottom(), RIGHT + DOWN*0.08, buff=2)

        # Create arrows
        input_to_kdf_arrow = Arrow(input_group.get_right(), kdf_group.get_left(), buff=0.1)
        kdf_key_in_to_kdf_arrow = Arrow(kdf_key_input_group.get_bottom(), kdf_group.get_top(), buff=0.1)
        
        # Arrow from KDF box downwards
        kdf_to_down_arrow = Arrow(kdf_group.get_bottom(), kdf_group.get_bottom() + DOWN, buff=0.1, stroke_width=5)

        # Split arrow into two arrows pointing to output key and KDF key output
        split_point = kdf_group.get_bottom() + DOWN * 0.5 - RIGHT * 0.25
        down_to_output_key_arrow = Arrow(split_point + RIGHT*0.15, output_key_group.get_left(), stroke_width=5, buff=0.1)


        dot1 = Dot(color=GRAY, radius = 0.1).move_to(kdf_to_down_arrow.get_start())
        path1 = VMobject()
        path1.set_points_as_corners([kdf_to_down_arrow.get_start(), split_point + RIGHT * 0.25])

        dot2_1 = Dot(color=GRAY, radius = 0.1).move_to(split_point+ RIGHT * 0.25)
        path2_1 = VMobject()
        path2_1.set_points_as_corners([split_point+ RIGHT * 0.25, kdf_to_down_arrow.get_end()])

        dot2_2 = Dot(color=GRAY, radius = 0.1).move_to(split_point+ RIGHT * 0.25)
        path2_2 = VMobject()
        path2_2.set_points_as_corners([split_point+ RIGHT * 0.25, down_to_output_key_arrow.get_end()])



        # Create additional shapes
        a1 = Line(start=kdf_key_output_box.get_left(), end=kdf_key_output_box.get_left() + LEFT * 4, color=BLUE, stroke_width=4)
        a2 = Arrow(start=kdf_key_input_box.get_left() + LEFT * 4, end=kdf_key_input_box.get_left(), buff=0.01 , color=BLUE, stroke_width=3.8)
        a3 = Line(start=a1.get_end(), end=a2.get_start(), color=BLUE, stroke_width=3.8)
        
        
        dot3 = Dot(color=RED, radius = 0.1).move_to(a1.get_start())
        path3 = VMobject()
        path3.set_points_as_corners([a1.get_start(), a1.get_end(), a2.get_start(), a2.get_end()])


        # Grouping everything together
        everything = VGroup(input_group, kdf_group, kdf_key_input_group, kdf_key_output_group, output_key_group,
                            input_to_kdf_arrow, kdf_key_in_to_kdf_arrow, kdf_to_down_arrow, down_to_output_key_arrow,
                            a1, a2, a3, dot1, dot2_1, dot2_2, dot3, path1, path2_1, path2_2, path3)

        # Positioning
        everything.move_to(ORIGIN).shift(DOWN*1.5)

        # Resize everything to half
        everything.scale(0.75)
        # Animations
        self.play(FadeIn(input_group), FadeIn(kdf_group), FadeIn(kdf_key_input_group))
        self.play(GrowArrow(input_to_kdf_arrow), GrowArrow(kdf_key_in_to_kdf_arrow))
        self.play(GrowArrow(kdf_to_down_arrow))
        self.play(GrowArrow(down_to_output_key_arrow))
        self.play(FadeIn(kdf_key_output_group), FadeIn(output_key_group))
        
        self.play(Create(dot1))
        self.play(MoveAlongPath(dot1, path1, rate_func=linear), run_time=2)  # Adjust run_time as needed
        self.play(FadeOut(dot1))
        self.play(Create(dot2_1), Create(dot2_2))
        self.play(
            MoveAlongPath(dot2_1, path2_1, rate_func=linear, run_time=2),
            MoveAlongPath(dot2_2, path2_2, rate_func=linear, run_time=2)
        )# Adjust run_time as needed
        self.play(FadeOut(dot2_2, dot2_1))
        self.play(Create(a1))
        self.play(Create(a3))
        self.play(GrowArrow(a2))
        self.play(Create(dot3))
        self.play(MoveAlongPath(dot3, path3, rate_func=linear), run_time=8)  # Adjust run_time as needed
        self.wait(2)

    def aliceBobComm(self):
        alice = RoundedRectangle(corner_radius=0.2, width=3, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        alice_text = Text("Alice", font_size=48).move_to(alice.get_center())
        alice_group = VGroup(alice, alice_text).to_edge(LEFT, buff=1).shift(RIGHT)

        bob = RoundedRectangle(corner_radius=0.2, width=3, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        bob_text = Text("Bob", font_size=48).move_to(bob.get_center())
        bob_group = VGroup(bob, bob_text).to_edge(RIGHT, buff=1).shift(LEFT)

        # Message text below Alice
        msg_text_alice = Text("msg m", font_size=40, color=WHITE).next_to(alice_group, 1.25*DOWN, buff=0.2)
        enc_text_alice = Text("sent: Enc(m,k)", font_size=40, color=WHITE).next_to(msg_text_alice, DOWN, buff=0.2)

        # Message text below Bob
        enc_text_bob = Text("rec: Enc(m,k)", font_size=40, color=WHITE).next_to(bob_group, 1.25*DOWN, buff=0.2)
        dec_text_bob = Text("Dec(Enc(m,k), k)", font_size=40, color=WHITE).next_to(enc_text_bob, DOWN, buff=0.2)
        msg_text_bob = Text("msg m", font_size=40, color=WHITE).next_to(dec_text_bob, DOWN, buff=0.2)
        
        # Arrow line and dot
        a1 = Line(start=alice.get_right(), end=bob.get_left(), color=BLUE, stroke_width=4)
        dot = Dot(color=RED, radius=0.1).move_to(a1.get_start())
        path1 = VMobject()
        path1.set_points_as_corners([a1.get_start(), a1.get_end()])
        path2 = VMobject()
        path2.set_points_as_corners([a1.get_end(), a1.get_start()])

        # Group everything together
        everything = VGroup(alice_group, bob_group, msg_text_alice, enc_text_alice, a1, dot, path1, enc_text_bob, dec_text_bob, msg_text_bob, path2)
        everything.move_to(ORIGIN)

        # Animations
        self.play(FadeIn(alice_group), FadeIn(bob_group))
        self.play(Create(a1))
        self.play(FadeIn(msg_text_alice))
        self.play(FadeIn(enc_text_alice))
        self.wait(1)
        self.play(Create(dot))
        self.play(MoveAlongPath(dot, path1, rate_func=linear), run_time=3)

        self.play(FadeIn(enc_text_bob))
        self.play(FadeIn(dec_text_bob))
        self.play(FadeIn(msg_text_bob))
        self.wait(1)
        self.play(MoveAlongPath(dot, path2, rate_func=linear), run_time=4)
        self.wait(2)

        # Shift everything up
        self.play(everything.animate.shift(UP*2))

        # Resize everything to half
        self.play(everything.animate.scale(0.5))

        # Replay the same animation with the resized objects
        self.play(Create(dot))
        self.play(MoveAlongPath(dot, path1, rate_func=linear), run_time=3)

        self.play(FadeIn(enc_text_bob))
        self.play(FadeIn(dec_text_bob))
        self.play(FadeIn(msg_text_bob))
        self.wait(1)
        self.play(MoveAlongPath(dot, path2, rate_func=linear), run_time=4)
        self.wait(2)


    def Rachet(self):

        shared_secret_key = RoundedRectangle(corner_radius=0.2, width=6, height=1.25, color=GRAY, fill_color=GRAY, fill_opacity=1)
        shared_secret_key_text = Text("Shared Secret Key", font_size=48).move_to(shared_secret_key.get_center())
        shared_secret_key_group = VGroup(shared_secret_key, shared_secret_key_text).to_edge(UP, buff=1).shift(DOWN*0.5)

        l1 = Line(start=shared_secret_key_group.get_bottom(), end=ORIGIN,stroke_width=3)

        alice = RoundedRectangle(corner_radius=0.2, width=3, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        alice_text = Text("Alice", font_size=48).move_to(alice.get_center())
        alice_group = VGroup(alice, alice_text).to_edge(LEFT, buff=1).shift(RIGHT)

        bob = RoundedRectangle(corner_radius=0.2, width=4, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        bob_text = Text("Bob", font_size=48).move_to(bob.get_center())
        bob_group = VGroup(bob, bob_text).to_edge(RIGHT, buff=1) 

        root_rachet_alice = RoundedRectangle(corner_radius=0.2, width=4, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        root_rachet_alice_text = Text("root rachet", font_size=48).move_to(root_rachet_alice.get_center())
        root_rachet_alice_group = VGroup(root_rachet_alice, root_rachet_alice_text).next_to(alice, DOWN, buff=0.5)

        # Root Rachet Bob
        root_rachet_bob = RoundedRectangle(corner_radius=0.2, width=4, height=1.25, color=ORANGE, fill_color=ORANGE, fill_opacity=1)
        root_rachet_bob_text = Text("root rachet", font_size=48).move_to(root_rachet_bob.get_center())
        root_rachet_bob_group = VGroup(root_rachet_bob, root_rachet_bob_text).next_to(bob, DOWN, buff=0.5)




        a1 = Arrow(ORIGIN, alice.get_right(), buff=0,stroke_width=3)
        a2 = Arrow(ORIGIN, bob.get_left(), buff=0,stroke_width=3)

        a3 = Arrow(alice.get_bottom(), root_rachet_alice.get_top() , buff=0,stroke_width=3)
        a4 = Arrow(bob.get_bottom(), root_rachet_bob.get_top(), buff=0,stroke_width=3)



        everything = VGroup(alice_group, bob_group, a1,a2, shared_secret_key_group,l1, a3,a4,root_rachet_alice_group,root_rachet_bob_group)
        everything.move_to(ORIGIN+UP)

        self.play(FadeIn(shared_secret_key_group))
        self.play(FadeIn(l1))
        self.play(GrowArrow(a1), GrowArrow(a2))
        self.play(FadeIn(alice_group), FadeIn(bob_group))
        self.play(GrowArrow(a3), GrowArrow(a4))
        self.play(FadeIn(root_rachet_alice_group), FadeIn(root_rachet_bob_group))
        
        self.wait(2)

    def construct(self):
        # Create the input box and label
        # self.KDF()
        # self.aliceBobComm()
        # self.KDF()
        self.Rachet()
        pass
        
    
