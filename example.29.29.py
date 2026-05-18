from turtle import*
color('blue')
for i in range(1, 100, 2):
  up()
  goto(i*2, 0)
  down()
  circle(i)
done()