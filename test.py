from step2stl import read_step, write_stl

input = 'models/planes.stp'
output = 'models/planes.stl'

shape = read_step(input)
write_stl(shape, output)