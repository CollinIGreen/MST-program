import timeit
import random
import line_profiler

from openpyxl import workbook, load_workbook

class Graph:
   def __init__(self):
       pass
   def read(self, v): #graph.read([])
       self.data = v
       self.size = len(v)
       CurVP = []
       self.VL = []
       EDP = []
       for i in range(0, self.size):
           CurVP = self.data[i]
           VP = []
           for j in range(0, self.size):
               if CurVP[j] != 0:
                   EDP = [CurVP[j], i, j]
                   VP.append(EDP)
           self.VL.append(VP)
   #@profile
   def IDdata(self):
       Rint = random.randint(0, self.size-1)
       edges = []
       T = [self.VL[Rint]]
       L = []
       length = 0
       for i in T[0]:
           L.append(i)
       L.sort()
       while len(T) != len(self.VL):
           edge = L[0]
           length = length + edge[0]
           edges.append(edge)
           T.append(self.VL[edge[2]])
           Lap = []
           for i in self.VL[edge[2]]:
               Lap.append(i)

           for line in L:
               DelL = []
               for line2 in Lap:
                   if line2[2] == line[1] and line2[1] == line[2]:
                       DelL.append(line2)
               for i in DelL:
                   Lap.remove(i)
           for i in L:
               DelL = []
               for x in self.VL[edge[2]]:
                   if x[1] == i[2] and x[2] == i[1]:
                       DelL.append(i)
               for i in DelL:
                   L.remove(i)
           Lap.sort()
           L = L+Lap
       print("minimum spanning tree is: ", length, " long")
wb = load_workbook(filename='graph.xlsx')
sh = wb.active
g = Graph()
num = 0
GRPH = []
for row in sh.rows:
   RW = []
   for cell in row:
       RW.append(cell.value)
   GRPH.append(RW)
g.read(GRPH)
#g.IDdata()
print(timeit.timeit(g.IDdata, number=1))
