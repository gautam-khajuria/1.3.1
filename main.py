import turtle as trtl

# 0.1.0

pen = trtl.Turtle()
pen.penup()
wn = trtl.Screen()
wn.setup(height=320, width=800)
# pen.shape('hot-air-balloon-21225(2).png')

background_image = "bkgrnd.gif"
wn.addshape(background_image)
wn.tracer(0)
camera_dx = 3
camera_x = 0



  


# Scrolling background
if __name__ == '__main__':
  while True:
    camera_x += camera_dx
    camera_x %= 800
      
    pen.goto(camera_x-800, 0)
    pen.shape(background_image)
    pen.stamp()
      
    pen.goto(camera_x, 0)
    pen.shape(background_image)
    pen.stamp()

    wn.update()

    pen.clear()
