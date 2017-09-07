"""
Dette programmet importerer GraphicsWndow, og bruker det til aa lage et vindu med et lerret,
tegne en roed sirkel og vente paa at brukeren lukker vinduet.
"""

from ezgraphics import GraphicsWindow

vindu = GraphicsWindow(500, 500)
lerret = vindu.canvas()

lerret.setOutline("red")
sirkel = lerret.drawOval(50, 50, 400, 400)

vindu.wait()
