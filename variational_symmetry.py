from manim import *
from numpy import cos, sin, exp


class VarTransform(Scene):
    def construct(self):
        # AXES AND LABELS
        ax = Axes(
            x_range = [-3, 4], y_range= [-2, 5, 1], 
            axis_config = {'tip_shape': StealthTip, 
                           "tip_height": 0.1,
                           "tip_width": 0.1,
                           "tick_size": 0.04}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="u")
        transf_labels = ax.get_axis_labels(x_label="\Tilde{x}", y_label="\Tilde{u}")

        line = Line(ax.coords_to_point(-0.4,0), ax.coords_to_point(3.5,0))
        line.stroke_width = 9
        omega_text = MathTex("\Omega").move_to(ax.coords_to_point(1.5,-0.5))
        movement_path = Line(ax.coords_to_point(1.5,0), ax.coords_to_point(-1.03,0))
        omega_hat_text = MathTex("\Tilde{\Omega}").move_to(ax.coords_to_point(-1.03,-0.5))

        # FUNCTIONS
        def u(x):
            return x + 0.5*x*cos(x) + 1
        
        def eta(x):
            return u(x) - 1.3*x*exp(-1/(x-0.35)**2)*exp(-1/(x-2.85)**2) if 0.35<x<2.85 else u(x)
        
        def u_hat(x):
            return -x + 0.9*sin(x) + 1
        
        def eta_hat(x):
            return u_hat(x) - 2.9*x*exp(-1/(x+1.81)**2)*exp(-1/(x-0.57)**2) if -1.81<x<0.57 else u_hat(x)
        
        # GRAPHS
        u_graph0 = ax.plot(u, x_range=[-0.4, 3.5] , color=BLUE)
        graph_text0 = ax.get_graph_label(u_graph0, label = r"u=f(x)", x_val=3, direction=UP * 2)
        u_graph1 = ax.plot(u_hat, x_range=[-3.0,0.9], color=RED)
        graph_text1 = ax.get_graph_label(u_graph1, label = r"\Tilde{u} = \Tilde{f}(\Tilde{x})", x_val=-1.5,
                                          direction=DOWN * 2)

        eta_graph0 = ax.plot(eta, x_range=[0.9,2.3] , color=DARK_BLUE)
        d_eta_graph0 = DashedVMobject(eta_graph0, num_dashes=10)
        graph_text2 = ax.get_graph_label(eta_graph0, label=r'u(x)+\varepsilon \eta(x)', x_val=2.2,
                                          direction=DOWN * 2.1)
        eta_graph1 = ax.plot(eta_hat, x_range=[-1.81,0.57] , color=MAROON)
        d_eta_graph1 = DashedVMobject(eta_graph1, num_dashes=10)
        graph_text3 = ax.get_graph_label(eta_graph1, label=r'\Tilde{u}(\Tilde{x}) + \Tilde{\eta}(\Tilde{x}, \varepsilon)', 
                                         x_val=-0.9, direction=UP * 1.5)
        
        # TEXT
        display_text0 = Tex("Perturbing the function $u$").to_edge(UR)
        display_text0.font_size=30
        display_text1 = Tex("and applying the transformation $g$").next_to(display_text0, DOWN * 1/2)
        display_text1.font_size=30
        
        # GROUPINGS 
        texts = VGroup(display_text0, display_text1)
        graph0 = VGroup(u_graph0, d_eta_graph0, labels, graph_text0, graph_text2)
        graph1 = VGroup(u_graph1, d_eta_graph1, transf_labels, graph_text1, graph_text3)
        

        self.add(ax, line, labels, graph_text0, u_graph0, omega_text)
        self.wait(duration=1)
        self.play(FadeIn(texts[0]))
        self.wait(duration=1)
        self.play(Create(d_eta_graph0), Write(graph_text2), run_time=1.2)
        self.play(FadeIn(texts[1]))
        self.wait(duration=2)
        self.play(ReplacementTransform(graph0, graph1), MoveAlongPath(line, movement_path),
                  ReplacementTransform(omega_text, omega_hat_text), run_time=3)
        self.wait()