import pygame
import pygame_gui
import time
import threading

RED = (255, 255, 255)
BLACK = (0, 0, 0)
teal = (5,248,220)
Y = 500
X = 0
num = 10
number = float(0)
pygame.init()
score_font = pygame.font.SysFont("Times New Roman", 20)
pygame.display.set_caption('Experimental UI')
window_surface = pygame.display.set_mode((600, 600))
w = 2
image = pygame.image.load(r'cookie.webp')
window_surface.blit(image, (-670, -150))
pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, 600, 20))
background = pygame.Surface((600, 600))
qu = 1000000
s = 0
manager = pygame_gui.UIManager((600, 600))
q = 0
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 250), (150, 50)),text='Cookie clicker',manager=manager)
Grandma = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (150, 50)),text='Grandma',manager=manager)
mine = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 120), (150, 50)),text='Mines',manager=manager)
Bank = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 240), (150, 50)),text='Bank',manager=manager)
Wiztow = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 360), (150, 50)),text='Wizard Tower',manager=manager)
Quadrive = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 480), (150, 50)),text='Quantum Drive',manager=manager)
clock = pygame.time.Clock()
is_running = True
loop2 = 1
loop4 = 1
loop5 = 1
X2 = 600
g = 100
d = 10000
Y2 = 600
c = 100000
f= 10
mill = 1000000
value = score_font.render("Cookies: " + str(number), True, RED) 
value2 = score_font.render("Cookies " + str(f), True, teal) 
value3 = score_font.render("Cookies " + str(g), True, teal) 
value4 = score_font.render("Cookies " + str(d), True, teal)
value5 = score_font.render("Cookies " + str(c), True, teal)
value6 = score_font.render("Cookies " + str(mill), True, teal)

textRect = value.get_rect()
textRect2 = value2.get_rect()
textRect3 = value3.get_rect()
textRect4 = value4.get_rect()
textRect5 = value5.get_rect()
textRect6 = value6.get_rect()
background.blit(value, textRect)
background.blit(value2, textRect2)
background.blit(value3, textRect3)
background.blit(value4, textRect4)
background.blit(value5, textRect5)
background.blit(value6, textRect6)
textRect2.center = (X2 // 2, Y2 // 2) 

textRect3.center = (X2 // 2, Y2 // 2) 
textRect4.center = (X2 // 2, Y2 // 2) 
textRect5.center = (X2 // 2, Y2 // 2) 
textRect6.center = (X2 // 2, Y2 // 2) 

loop3 = 1
z = 0
def backgroundnum():
  global z
  global w
  global q
  global number
  global value
  while True:
    window_surface.blit(image, (-670, -150))
    pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, 600, 20))
    value = score_font.render("Cookies: " + str(number), True, RED)   
    value2 = score_font.render("Cookies: " + str(f), True, teal)
    value3 = score_font.render("Cookies: " + str(g * loop2), True, teal)
    value4 = score_font.render("Cookies: " + str(d* loop3), True, teal)   
    value5 = score_font.render("Cookies: " + str(c* loop4), True, teal)
    value6 = score_font.render("Cookies: " + str(mill* loop5), True, teal)
    window_surface.blit(value2, (0, 50))
    window_surface.blit(value3, (0, 170))
    window_surface.blit(value4, (0, 290))
    window_surface.blit(value5, (0, 410))
    window_surface.blit(value6, (0, 530))

    number = float(number)
    if z == 5:
        number += 1
    if w == 3:
        number += 10
    if q == 4:
      number += 100
    if s == 4:
      number+= 1000
    if mill == 3:
      number += 10000
    time.sleep(1)
#ellipse(surface, color, rect)
g = 100
d = 10000


loop = 1
while True:
    pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, 600, 20))
    window_surface.blit(value, (270, 0))

    for event in pygame.event.get():
       
        time_delta = clock.tick(10000)

        if event.type == pygame.QUIT:
          print("Click on the console and type\n")
          input1 = input("Are you sure you want to quit: \n")

          if input1 == "y" or input1 == "yes" or     input1 == "Yes" or input1 == "Y":
            print("Ok\n")
            quit(time.sleep(1))
  
          elif input1 ==  "no" or input1 == "N" or   input1 == "n" or input1 == "No":
            print("ok \n")
            continue
          else:
            print("Press a plausible key! \n" + "Click on X again to exit")
            continue

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
              number += 1
              value = score_font.render("Cookies: " + str(number), True, RED)
              pygame.draw.rect(window_surface, BLACK, pygame.Rect(0, 0, 600, 20))
              window_surface.blit(image, (-670, -150))

            

           
            if event.ui_element == Grandma:
    
              f = loop*num

              if number < f:
                print('Insufficient funds!')
              elif number >= f:
                z = 5
                loop += 1.25
                number = number - f
                print('Purchased')

                b = threading.Thread(name='backgroundnum', target=backgroundnum)
                b.start()

            if event.ui_element == mine:

              
              if number < loop2 * g :
                print('Insufficient funds!')

              elif number >= loop2* g:
 
                w = 3
                number = number - (g * loop2)
                loop2 += 1.25
    
                print('Purchased')

                b = threading.Thread(name='backgroundnum', target=backgroundnum)
                b.start()
                
            if event.ui_element == Bank:

              if number < loop3*d:
                print('Insufficient funds!')

              elif number >= loop3 *d :
                q = 4
                number = number - (d * loop3)              
                loop3 += 1.25
                print('Purchased')

                b = threading.Thread(name='backgroundnum', target=backgroundnum)
                b.start()
            if event.ui_element == Wiztow:
              
              if number < loop4*c:
                print('Insufficient funds!')
              elif number >= loop4*c:
                s = 4
                number = number - (c*loop4)                
                loop4 += 1.25
            
            if event.ui_element == Quadrive:
              if number < loop5 * qu:
                print("insufficient funds")
              elif number >= loop5 * qu:
                mill = 3
                number = number - (qu * loop5)

                print('Purchased')

                b = threading.Thread(name='backgroundnum', target=backgroundnum)
                b.start()
        manager.process_events(event)
    

    manager.update(time_delta)


    manager.draw_ui(window_surface)

    pygame.display.update()
