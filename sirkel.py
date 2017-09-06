from ezgraphics import GraphicsWindow

vindu = GraphicsWindow(500, 500)
lerret = vindu.canvas()

lerret.setOutline("red")
sirkel = lerret.drawOval(50, 50, 400, 400)

vindu.wait()
