from manim import *

config.disable_caching = True

class Video(Scene):
    def construct(self):
        self.add_sound("bgm.mp3", gain=-40)
        self.add_sound("대본1.wav", time_offset=0)
        title_main = Text("JeongHoon Theory", font_size=48)
        title_main.set_color(BLUE_B)
        self.play(Write(title_main))
        self.wait()
        self.play(title_main.animate.to_edge(UP, buff=1))

        eq1 = MathTex(r"\frac{1}{0} = \infty", font_size=60)
        eq1.to_edge(UP, buff=2.5)  # 화면 위쪽에 붙이기

        eq2 = MathTex(r" \frac{0}{0}=\mathbb{R}", font_size=60)
        eq2.next_to(eq1, DOWN, buff=0.5)  # eq1 아래에 0.5 거리로 배치

        self.play(Write(eq1), Write(eq2))
        self.wait(4)
        self.play(Unwrite(eq1), Unwrite(eq2))
        self.wait()
        
        eq3 = MathTex(r"-\infty=\frac{-1}{0}=\frac{1}{\frac{-0}{1}}=\frac{1}{0}=\infty", font_size=60)
        eq3.to_edge(UP, buff=2.5)

        eq3Description = Text("Wheel Theory", font_size=60)
        eq3Description.next_to(eq3, DOWN, buff=0.5)

        self.add_sound("대본2.wav", time_offset=0)
        self.play(Write(eq3))
        self.wait(2)
        self.play(Write(eq3Description))
        self.wait(2)
        self.play(Unwrite(eq3), Unwrite(eq3Description))
        self.wait()

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_numbers": True}
        ).scale(0.6)
        self.play(Create(axes))

        m_tracker = ValueTracker(1)

        line1 = always_redraw(
            lambda: axes.plot(lambda x: m_tracker.get_value() * x, x_range=[-3, 3], color=BLUE)
        )
        line2 = always_redraw(
            lambda: axes.plot(lambda x: -m_tracker.get_value() * x, x_range=[-3, 3], color=RED)
        )
        self.play(Create(line1), Create(line2))

        # 오른쪽 아래 기울기 표시 텍스트
        slope_text = always_redraw(
            lambda: Text(
                f"Slope: {m_tracker.get_value():.2f}",
                font_size=24,
                color=YELLOW
            ).to_corner(DOWN + RIGHT).shift(LEFT * 0.5 + UP * 0.5)
        )
        self.add(slope_text)

        self.wait()
        self.play(m_tracker.animate.set_value(500), run_time=4)
        self.wait()

        self.add_sound("대본3.m4a")
        self.play(Uncreate(axes), Uncreate(line1), Uncreate(line2), Uncreate(slope_text))
        self.wait()

        val = ValueTracker(0)

        def overflow_number():
            x = val.get_value()
            if x > 32767:
                return -32767 + (x-32768)
            else:
                return x

            # 10 단위로 숫자 반올림

        def overflow_latex():
            num = overflow_number()
            if num < 0:
                return r"-" + str(abs(int(num)))
            else:
                return str(int(num))


        number_text = always_redraw(
            lambda: MathTex(overflow_latex(), font_size=72)
                .move_to(ORIGIN)
        )
        self.add(number_text)

        # 0 -> 150까지 숫자 증가 애니메이션
        self.play(val.animate.set_value(32768), run_time=5)
        self.wait(2)
        self.play(Unwrite(number_text))
        self.wait()

        self.add_sound("대본4.m4a")
        infinity = MathTex(r"\infty+\infty=0", font_size=60)
        infinity.to_edge(UP, buff=2.5)

        infinityDsc1 = Text("Jeonghoon’s Infinite Theorem", font_size=30)
        infinityDsc1.next_to(infinity, DOWN, buff=0.5)
        infinityDsc2 = Text("Unmanipulable expression", font_size=30)
        infinityDsc2.next_to(infinityDsc1, DOWN, buff=0.5)

        self.play(Write(infinity))
        self.wait(1.5)
        self.play(Write(infinityDsc1))
        self.wait(3)
        self.play(Write(infinityDsc2))
        self.wait(2)
        self.play(Unwrite(infinity), Unwrite(infinityDsc1), Unwrite(infinityDsc2))
        self.wait()

        self.add_sound("대본5.wav")
        eq22 = MathTex(r" \frac{0}{0}=\mathbb{R}", font_size=60)
        eq22.move_to(ORIGIN)

        self.play(Write(eq22))
        self.wait(2)
        self.play(Unwrite(eq22))
        self.wait()

        proof1 = MathTex(r"x=\frac{0}{0}", font_size=60)
        proof1.move_to(ORIGIN)

        proof2 = MathTex(r"0x=0", font_size=60)

        proofDsc = Text("Identity Equation", font_size=30)
        proofDsc.next_to(proof1, DOWN, buff=0.5)

        self.play(Write(proof1))
        self.wait(2)
        self.play(Transform(proof1, proof2))
        self.wait()
        self.play(Write(proofDsc))
        self.wait(2)
        self.play(Unwrite(proof1), Unwrite(proofDsc))
        self.wait()

        func1 = MathTex(r"x = k", font_size=60)
        func2 = MathTex(r"0y=x-k", font_size=60)
        func3 = MathTex(r"y=\frac{1}{0}x-\frac{k}{0}", font_size=60)
        self.play(Write(func1))
        self.wait()
        self.play(Transform(func1, func2))
        self.wait()
        self.play(Transform(func1, func3))
        self.wait(2)

        # Step 2: 수식을 아래로 이동
        self.add_sound("대본6.wav")
        self.play(func1.animate.to_edge(DOWN))
        self.wait(0.5)

        # Step 3: 좌표축 생성
        axes2 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=4,
    
            x_axis_config={
                "include_numbers": False,  # x축 숫자 제거
            },
            y_axis_config={
                "include_ticks": False,
                "include_tip": False,
                "include_numbers": False,
                "stroke_opacity": 0,       # y축 자체를 투명하게 (= 없애기)
            }
        )
        self.play(Create(axes2))

        # Step 4: x = 2 수직선 그리기
        line = Line(
            start=axes2.c2p(0, -3),  # 아래쪽 y
            end=axes2.c2p(0, 3),     # 위쪽 y
            color=BLUE
        )
        self.play(Create(line))
        self.wait(2)
        self.play(Uncreate(axes2), Uncreate(line), Uncreate(func1), Uncreate(title_main))
        self.wait()

        self.add_sound("대본7.m4a")
        title_two = Text("Ramanujan Sum", font_size=48)
        title_two.set_color(BLUE_B)
        self.play(Write(title_two))
        self.wait()
        self.play(title_two.animate.to_edge(UP, buff=1))
        
        terms = ["1", "+ 2", "+ 3", "+ 4", "+ 5", "+ 6", "+ 7", "+ 8", "+ 9", "+ 10", "+ \\cdots"]
        expressions = []

        first_term = MathTex(terms[0])
        self.play(Write(first_term), run_time=0.2)  # 첫 항 등장 애니메이션 시간
        expressions.append(first_term)

        group = VGroup(first_term)

        for i in range(1, len(terms)):
            new_term = MathTex(terms[i])
            new_term.next_to(expressions[-1], RIGHT, buff=0)
            expressions.append(new_term)
            group.add(new_term)

            self.play(
                FadeIn(new_term, run_time=0.2),  # 새 항 등장 애니메이션 시간
                group.animate.shift(LEFT * new_term.width * 0.5), run_time=0.2  # 수식 전체 밀림 애니메이션 시간
            )

        equal_tex = MathTex("= -\\frac{1}{12}")
        equal_tex.next_to(expressions[-1], RIGHT, buff=0.1)
        group.add(equal_tex)

        self.play(
            FadeIn(equal_tex, run_time=0.2),  # 등호 및 결과 등장 애니메이션 시간
            group.animate.shift(LEFT * equal_tex.width * 0.5), run_time=0.2  # 수식 전체 밀림 애니메이션 시간
        )

        self.wait(2)

        self.play(FadeOut(group), run_time=1.0)  # 라마누잔 수식 및 라벨 제거 애니메이션 시간
        self.wait()

        self.add_sound("대본8.m4a")
        infDef = MathTex(r"\infty=N+k \ (0\leq k\leq 1)", font_size=60)
        self.play(Write(infDef))
        self.wait(3)
        self.play(Unwrite(infDef))
        self.wait()

        summation = MathTex(r"\left\{\begin{matrix}\, \\ \,\end{matrix}\right.\sum_{k=1}^{n}k\left.\begin{matrix}\, \\ \,\end{matrix}\right\}^{2}=\sum_{k=1}^{n}k^3", font_size=60)
        self.play(Write(summation))
        self.wait()

        summation2 = MathTex(r"\begin{Bmatrix}\zeta (-1)\end{Bmatrix}^{2}=\zeta (-3)", font_size=60)
        self.play(Transform(summation, summation2))
        self.wait(2.5)

        summation3 = MathTex(r"\left ( -\frac{1}{12} \right )^{2}\neq \frac{1}{120}", font_size=60)
        self.play(Transform(summation, summation3))
        self.wait(3)

        self.add_sound("대본9.wav")
        self.play(Unwrite(summation))
        self.wait()

        overflow = MathTex(r"128=-128",font_size=60)
        self.play(FadeIn(overflow))
        self.wait()

        self.play(overflow.animate.to_edge(DOWN))
        self.wait(1)

        value = MathTex(r"130", font_size=60)
        self.play(Write(value))
        self.wait(3)

        value2 = MathTex(r"65", font_size=60)
        self.play(Transform(value, value2))
        self.wait()

        value22 = MathTex(r"130", font_size=60)
        self.play(Transform(value, value22))
        self.wait()

        value3 = MathTex(r"-126", font_size=60)
        self.play(Transform(value, value3))
        self.wait()

        value4 = MathTex(r"-63", font_size=60)
        self.play(Transform(value, value4))
        self.wait(9)

        self.play(Unwrite(value), Unwrite(overflow))
        self.wait()

        self.add_sound("대본10.wav")
        rasummation = MathTex(r"f(1)+f(2)+f(3)+\cdots =-\frac{f(0)}{2}+i\int_{0}^{\infty}\frac{f(it)-f(-it)}{e^{2\pi t}-1}dt", font_size=48)
        self.play(Write(rasummation))
        self.wait()

        rasummationDsc = Text("Ramanujan Summation", font_size=30)
        rasummationDsc.next_to(rasummation, DOWN, buff=0.5)
        self.play(Write(rasummationDsc))
        self.wait()

        self.play(Unwrite(rasummation), Unwrite(rasummationDsc))
        self.wait()
        
        self.add_sound("대본11.wav")
        funcDef = MathTex(r"f(x)=x^{2n}", font_size=60)
        self.play(Write(funcDef))
        self.wait(2)

        funcDef2 = MathTex(r"1^{2n}+2^{2n}+3^{2n}+\cdots =0", font_size=60)
        self.play(Transform(funcDef, funcDef2))
        self.wait(2)

        funcDef3 = MathTex(r"1+1+1+\cdots =0", font_size=60)
        self.play(Transform(funcDef, funcDef3))
        self.wait(2)

        self.play(Unwrite(funcDef))
        self.wait()

        self.add_sound("대본12.m4a")
        zero = MathTex(r"1+x+x^{2}+x^{3}+\cdots =\frac{1}{1-x}", font_size=60)
        self.play(Write(zero))
        self.wait()

        zero2 = MathTex(r"1+1+1+1+\cdots =\frac{1}{0}", font_size=60)
        self.play(Transform(zero, zero2))
        self.wait()

        self.play(Unwrite(zero))
        self.wait()

        zero3 = MathTex(r"\infty + \infty = 0", font_size=60)
        self.play(Write(zero3))
        self.wait(2)

        zero4 = MathTex(r"\frac{1}{0}=0", font_size=60)
        self.play(Transform(zero3, zero4))
        self.wait(4)

        self.play(Unwrite(zero3), Unwrite(title_two))
        self.wait()

        self.add_sound("대본13.m4a")
        title_three = Text("JeongHoon Triangle", font_size=48)
        title_three.set_color(BLUE_B)
        self.play(Write(title_three))
        self.wait()
        self.play(title_three.animate.to_edge(UP, buff=1))

        jt = MathTex(r" J(x, k)=1^{k}+2^{k}+3^{k}+\cdots +\left \lfloor x\right \rfloor ^{k} \ (R_{max}=x)", font_size=60)
        self.play(Write(jt))
        self.wait(2)

        self.play(Unwrite(jt))
        self.wait()

        def f(x):
            x = round(x, 3)
            if x <= 0:
                return None  # 자연수 x만 처리
            natural = int(x)
            summation = natural * (natural + 1) / 2
            maxNum = int(summation / x)
            if maxNum % 2 == 0:
                summation -= maxNum * x
            else:
                summation -= (maxNum + 1) * x
            return summation
        
        self.add_sound("대본14.m4a")
        axes3 = Axes(
            x_range=[0, 20, 1],
            y_range=[-10, 10, 2],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True},
        )
        self.play(Create(axes3), run_time=2)

        # 점들과 라벨을 담을 VGroup
        dots = VGroup()
        labels = VGroup()

        for x in range(1, 21):  # x는 자연수만
            y = f(x)
            if y is None:
                continue

            dot_color = YELLOW if y == 0 else BLUE
            dot = Dot(point=axes3.c2p(x, y), color=dot_color, radius=0.08)
            dots.add(dot)

            if y == 0:
                label = MathTex(f"({x}, 0)", font_size=24).next_to(dot, UP, buff=0.2)
                labels.add(label)

        self.play(LaggedStartMap(FadeIn, dots, shift=UP, lag_ratio=0.05))
        self.wait(2)
        self.play(LaggedStartMap(Write, labels, lag_ratio=0.1))
        self.wait()
        self.play(Uncreate(axes3), Uncreate(dots), Uncreate(labels))

        axes4 = Axes(
            x_range=[0, 10000, 2000],
            y_range=[-10000, 10000, 5000],
            x_length=10,
            y_length=5,  # y축 길이 원래대로
            axis_config={"include_numbers": True, "font_size": 20},
        )
        axes4.move_to(ORIGIN + DOWN * 0.5)

        points = []
        for x in range(1, 10001):
            fx = f(x)
            points.append(axes4.coords_to_point(x, fx))

        graph_line = VMobject(color=BLUE)
        graph_line.set_points_as_corners(points)

        self.play(Create(axes4), run_time=1.0)  # 좌표축 및 제목 등장 애니메이션 시간
        
        graph_line.set_z_index(-1)  # 그래프를 x축 위에 그리지 말고 뒤로 보내기
        
        self.play(Create(graph_line), run_time=3.0)  # 그래프 그리기 애니메이션 시간

        self.wait(2)
        self.play(Uncreate(graph_line), Uncreate(axes4))
        self.wait()

        self.add_sound("대본15.m4a")
        axes5 = Axes(
            x_range=[10.5, 13.5, 0.5],
            y_range=[-7, 8, 2],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True}
        )
        axes5.move_to(ORIGIN + DOWN * 0.5)

        for label in axes5.x_axis.numbers:
            if abs(label.get_value() - 10.5) < 1e-4:
                label.set_opacity(0)  # 또는 self.remove(label)
        
        self.play(Create(axes5))

        xs = np.linspace(11, 13, 600)  # 점 간격 조절

        dots = VGroup()
        for x in xs:
            y = f(x)
            if y is None:
                continue
            color = BLUE
            dot = Dot(point=axes5.c2p(x, y), radius=0.01, color=color)
            dots.add(dot)


        self.play(LaggedStartMap(FadeIn, dots, shift=UP, lag_ratio=0.01), run_time=3)

        dot_12 = Dot(point=axes5.c2p(12, 0), radius=0.1, color=BLUE)
        self.play(FadeIn(dot_12))
        self.play(dot_12.animate.set_color(RED).scale(1.2))

        # 점대칭 시각화 (대칭 선, 설명 추가)
        symmetry_text = Text("Point symmetry", font_size=24, color=RED)
        symmetry_text.next_to(dot_12, UP)

        self.play(FadeIn(symmetry_text))

        self.wait()
        
        self.add_sound("대본16.wav")
        self.play(Uncreate(dots), Uncreate(axes5), Uncreate(symmetry_text), Uncreate(dot_12))
        self.wait()

        jt2 = MathTex(r"J(x, 1)=-\frac{1}{12}", font_size=60)
        jtDsc = MathTex(r"x=?", font_size=60)
        jtDsc.next_to(jt2, DOWN, buff=0.5)

        self.play(Write(jt2))
        self.wait()
        self.play(Write(jtDsc))
        self.wait(1.5)

        self.play(Unwrite(jt2), Unwrite(jtDsc))
        self.wait()

        init = MathTex(r"n=\left \lfloor x\right \rfloor, S_{n}=\frac{n(n+1)}{2},m=\left \lfloor \frac{S_{n}}{x}\right \rfloor", font_size=60)
        self.play(Write(init))
        self.wait(2)

        self.play(Unwrite(init))
        self.wait()

        self.add_sound("대본17.wav")
        eqSolve = MathTex(r"J(x,1)=\begin{Bmatrix}S_{n}-mx &  m\ \text{is even}\\S_{n}-(m+1)x & m\ \text{is odd} \\\end{Bmatrix}", font_size=60)
        self.play(Write(eqSolve))
        self.wait(2)
        self.play(Unwrite(eqSolve))
        self.wait()
        
        self.add_sound("대본18.wav")
        jt3 = MathTex(r"J(x, 1)=-\frac{1}{12}", font_size=60)
        self.play(Write(jt3))
        self.wait()
        eqSolve2 = MathTex(r"x=\begin{Bmatrix}\frac{12S_{n}+1}{12m} &  m\ \text{is even}\\ & \\\frac{12S_{n}+1}{12(m+1)} & m\ \text{is odd} \\\end{Bmatrix}", font_size=60)
        self.play(Transform(jt3, eqSolve2))
        self.wait()
        eqSolve3 = MathTex(r"n=4k+3, \ m=\frac{n-1}{2}=2k+1\ (k=0,1,2,\cdots)", font_size=60)
        self.play(Transform(jt3, eqSolve3))
        self.wait(3)
        eqSolve4 = MathTex(r"x=n+\frac{1}{6(n+1)} \ (k=0,1,2,\cdots) \ (n=4k+3)", font_size=60)
        self.play(Transform(jt3, eqSolve4))
        self.wait(2)
        eqSolveDsc = Text("The largest natural number is odd.", font_size=48)
        eqSolveDsc.next_to(jt3, DOWN, buff=0.5)
        self.play(Write(eqSolveDsc))
        self.wait(2)
        self.play(Unwrite(eqSolveDsc), Unwrite(jt3))
        self.wait()

        # 처음 수식
        k_values = list(range(1, 11))

        self.add_sound("대본19.m4a")
        # 첫 수식
        current_eq = MathTex(r"J(x,\ 1)\ =\ \zeta(-1)", font_size=60)
        self.play(Write(current_eq))
        self.wait()

        # k=2부터 10까지 순서대로 Transform
        for k in k_values[1:]:
            next_eq = MathTex(rf"J(x,\ {k})\ =\ \zeta(-{k})", font_size=60)
            self.play(Transform(current_eq, next_eq))
            self.wait(0.1)

        # 마지막 수식 잠깐 유지 후 사라지기
        self.wait()

        self.add_sound("대본20.m4a")
        guess = MathTex(r"J(x,\ k)\ =\ \zeta(-k)", font_size=60)
        self.play(Transform(current_eq, guess))
        self.wait(4)
        guessDsc = Text("JeongHoon–Ramanujan Conjecture", font_size=48)
        guessDsc.next_to(current_eq, DOWN, buff=0.5)
        self.play(Write(guessDsc))
        self.wait(4)
