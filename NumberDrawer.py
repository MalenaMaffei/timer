import curses
NUMBERS =
[
     [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1], #/* 0 */
     [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1], #/* 1 */
     [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1], #/* 2 */
     [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1], #/* 3 */
     [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1], #/* 4 */
     [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1], #/* 5 */
     [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1], #/* 6 */
     [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1], #/* 7 */
     [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1], #/* 8 */
     [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1], #/* 9 */
]


class NumberDrawer:

     def __init__(self, window):
          self.window = window

     def drawNumber(stdscr, number, x, y):
          # aca tengo que agarrar el numero y dibujarlo
          sy = y
          for i in range(0, 30):
               if sy == y + 6:
                    sy = y
                    x+=1

               self.stdscr.bkgdset(COLOR_PAIR(NUMBERS[number][i/2]))
               stdscr.addch(x, sy, ' ')
               sy+=1

          sstdscr.refresh()
