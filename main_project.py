import pygame

print('Крестики нолики')
circle1 = False
circle2 = False
circle3 = False
circle4 = False
circle5 = False
circle6 = False
circle7 = False
circle8 = False
circle9 = False
b = 0
repeat_move1 = False
repeat_move2 = False
repeat_move3 = False
repeat_move4 = False
repeat_move5 = False
repeat_move6 = False
repeat_move7 = False
repeat_move8 = False
repeat_move9 = False
cross1 = False
cross2 = False
cross3 = False
cross4 = False
cross5 = False
cross6 = False
cross7 = False
cross8 = False
cross9 = False
x_win = False
o_win = False
win = False
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крестики-нолики')
    size = w, h = 800, 800
    screen = pygame.display.set_mode(size)
    step1 = False
    step2 = False
    step3 = False
    step4 = False
    step5 = False
    step6 = False
    step7 = False
    step8 = False
    step9 = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                x_pos = pos[0]
                y_pos = pos[1]
                step1 = True
                step2 = True
                step3 = True
                step4 = True
                step5 = True
                step6 = True
                step7 = True
                step8 = True
                step9 = True
                if 0 < x_pos < w // 3 and 0 < y_pos < h // 3:
                    if not repeat_move1:
                        b += 1
                        print(b)
                        repeat_move1 = True
                if w // 3 < x_pos < w // 3 * 2 and 0 < y_pos < h // 3:
                    if not repeat_move2:
                        b += 1
                        print(b)
                        repeat_move2 = True
                if w // 3 * 2 < x_pos < w and 0 < y_pos < h // 3:
                    if not repeat_move3:
                        b += 1
                        print(b)
                        repeat_move3 = True
                if 0 < x_pos < w // 3 and h // 3 < y_pos < h // 3 * 2:
                    if not repeat_move4:
                        b += 1
                        print(b)
                        repeat_move4 = True
                if w // 3 < x_pos < w // 3 * 2 and h // 3 < y_pos < h // 3 * 2:
                    if not repeat_move5:
                        b += 1
                        print(b)
                        repeat_move5 = True
                if w // 3 * 2 < x_pos < w and h // 3 < y_pos < h // 3 * 2:
                    if not repeat_move6:
                        b += 1
                        print(b)
                        repeat_move6 = True
                if 0 < x_pos < w // 3 and h // 3 * 2 < y_pos < h:
                    if not repeat_move7:
                        b += 1
                        print(b)
                        repeat_move7 = True
                if w // 3 < x_pos < w // 3 * 2 and h // 3 * 2 < y_pos < h:
                    if not repeat_move8:
                        b += 1
                        print(b)
                        repeat_move8 = True
                if w // 3 * 2 < x_pos < w and h // 3 * 2 < y_pos < h:
                    if not repeat_move9:
                        b += 1
                        print(b)
                        repeat_move9 = True
        screen.fill('blue4')
        pygame.draw.line(screen, (255, 255, 255), (w // 3, 0), (w // 3, h), width=3)
        pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2, 0), (w // 3 * 2, h), width=3)
        pygame.draw.line(screen, (255, 255, 255), (0, h // 3), (w, h // 3), width=3)
        pygame.draw.line(screen, (255, 255, 255), (0, h // 3 * 2), (w, h // 3 * 2), width=3)
        if step1 or step2 or step3 or step4 or step5 or step6 or step7 or step8 or step9:
            if 0 < x_pos < w // 3 and 0 < y_pos < h // 3 and b % 2 == 0 and not win and not cross1 or circle1:
                circle1 = True
                pygame.draw.circle(screen, pygame.Color('white'), (w // 3 // 2, h // 3 // 2), 100,
                                   3)
            if w // 3 < x_pos < w // 3 * 2 and 0 < y_pos < h // 3 and b % 2 == 0 and not win and not cross2 or circle2:
                circle2 = True
                pygame.draw.circle(screen, pygame.Color('white'),
                                   (w // 3 * 2 - w // 3 // 2, h // 3 // 2), 100, 3)
            if w // 3 * 2 < x_pos < w and 0 < y_pos < h // 3 and b % 2 == 0 and not win and not cross3 or circle3:
                circle3 = True
                pygame.draw.circle(screen, pygame.Color('white'), (w - w // 3 // 2, h // 3 // 2),
                                   100, 3)
            if 0 < x_pos < w // 3 and h // 3 < y_pos < h // 3 * 2 and b % 2 == 0 and not win and not cross4 or circle4:
                circle4 = True
                pygame.draw.circle(screen, pygame.Color('white'),
                                   (w // 3 // 2, h // 3 * 2 - h // 3 // 2), 100, 3)
            if w // 3 < x_pos < w // 3 * 2 and h // 3 < y_pos < h // 3 * 2 and b % 2 == 0 and not win and not cross5 or \
                    circle5:
                circle5 = True
                pygame.draw.circle(screen, pygame.Color('white'),
                                   (w // 3 * 2 - w // 3 // 2, h // 3 * 2 - h // 3 // 2), 100, 3)
            if w // 3 * 2 < x_pos < w and h // 3 < y_pos < h // 3 * 2 and b % 2 == 0 and not win and not cross6 \
                    or circle6:
                circle6 = True
                pygame.draw.circle(screen,
                                   pygame.Color('white'),
                                   (w - w // 3 // 2, h // 3 * 2 - h // 3 // 2), 100, 3)
            if 0 < x_pos < w // 3 and h // 3 * 2 < y_pos < h and b % 2 == 0 and not win and not cross7 or circle7:
                circle7 = True
                pygame.draw.circle(screen, pygame.Color('white'), (w // 3 // 2, h - h // 3 // 2),
                                   100, 3)
            if w // 3 < x_pos < w // 3 * 2 and h // 3 * 2 < y_pos < h and b % 2 == 0 and not win and not cross8 \
                    or circle8:
                circle8 = True
                pygame.draw.circle(screen, pygame.Color('white'),
                                   (w // 3 * 2 - w // 3 // 2, h - h // 3 // 2), 100, 3)
            if w // 3 * 2 < x_pos < w and h // 3 * 2 < y_pos < h and b % 2 == 0 and not win and not cross9 or circle9:
                circle9 = True
                pygame.draw.circle(screen, pygame.Color('white'),
                                   (w - w // 3 // 2, h - h // 3 // 2), 100, 3)
            if 0 < x_pos < w // 3 and 0 < y_pos < h // 3 and b % 2 != 0 and not win and not circle1 or cross1:
                cross1 = True
                pygame.draw.line(screen, (255, 255, 255), (50, 50), (w // 3 - 50, h // 3 - 50),
                                 width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 - 50, 50), (50, h // 3 - 50),
                                 width=5)
            if w // 3 < x_pos < w // 3 * 2 and 0 < y_pos < h // 3 and b % 2 != 0 and not win and not circle2 or cross2:
                cross2 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 + 50, 50),
                                 (w // 3 * 2 - 50, h // 3 - 50), width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 - 50, 50),
                                 (w // 3 + 50, h // 3 - 50), width=5)
            if w // 3 * 2 < x_pos < w and 0 < y_pos < h // 3 and b % 2 != 0 and not win and not circle3 or cross3:
                cross3 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 + 50, 50),
                                 (w - 50, h // 3 - 50), width=5)
                pygame.draw.line(screen, (255, 255, 255), (w - 50, 50),
                                 (w // 3 * 2 + 50, h // 3 - 50), width=5)
            if 0 < x_pos < w // 3 and h // 3 < y_pos < h // 3 * 2 and b % 2 != 0 and not win and not circle4 or cross4:
                cross4 = True
                pygame.draw.line(screen, (255, 255, 255), (50, h // 3 + 50),
                                 (w // 3 - 50, h // 3 * 2 - 50), width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 - 50, h // 3 + 50),
                                 (50, h // 3 * 2 - 50), width=5)
            if w // 3 < x_pos < w // 3 * 2 and h // 3 < y_pos < h // 3 * 2 and b % 2 != 0 and not win and not circle5 \
                    or cross5:
                cross5 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 + 50, h // 3 + 50),
                                 (w // 3 * 2 - 50, h // 3 * 2 - 50), width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 - 50, h // 3 + 50),
                                 (w // 3 + 50, h // 3 * 2 - 50), width=5)
            if w // 3 * 2 < x_pos < w and h // 3 < y_pos < h // 3 * 2 and b % 2 != 0 and not win and not circle6 \
                    or cross6:
                cross6 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 + 50, h // 3 + 50),
                                 (w - 50, h // 3 * 2 - 50),
                                 width=5)
                pygame.draw.line(screen, (255, 255, 255), (w - 50, h // 3 + 50),
                                 (w // 3 * 2 + 50, h // 3 * 2 - 50),
                                 width=5)
            if 0 < x_pos < w // 3 and h // 3 * 2 < y_pos < h and b % 2 != 0 and not win and not circle7 or cross7:
                cross7 = True
                pygame.draw.line(screen, (255, 255, 255), (50, h // 3 * 2 + 50),
                                 (w // 3 - 50, h - 50), width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 - 50, h // 3 * 2 + 50),
                                 (50, h - 50), width=5)
            if w // 3 < x_pos < w // 3 * 2 and h // 3 * 2 < y_pos < h and b % 2 != 0 and not win and not circle8 or cross8:
                cross8 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 + 50, h // 3 * 2 + 50),
                                 (w // 3 * 2 - 50, h - 50),
                                 width=5)
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 - 50, h // 3 * 2 + 50),
                                 (w // 3 + 50, h - 50),
                                 width=5)
            if w // 3 * 2 < x_pos < w and h // 3 * 2 < y_pos < h and b % 2 != 0 and not win and not circle9 or cross9:
                cross9 = True
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 + 50, h // 3 * 2 + 50),
                                 (w - 50, h - 50),
                                 width=5)
                pygame.draw.line(screen, (255, 255, 255), (w - 50, h // 3 * 2 + 50),
                                 (w // 3 * 2 + 50, h - 50),
                                 width=5)
            if circle1 and circle2 and circle3:
                pygame.draw.line(screen, (255, 255, 255), (0, h // 3 // 2), (w, h // 3 // 2),
                                 width=3)
                win = True
                o_win = True
            if circle4 and circle5 and circle6:
                pygame.draw.line(screen, (255, 255, 255), (0, h // 3 * 2 - h // 3 // 2),
                                 (w, h // 3 * 2 - h // 3 // 2),
                                 width=3)
                win = True
                o_win = True
            if circle7 and circle8 and circle9:
                pygame.draw.line(screen, (255, 255, 255), (0, h - h // 3 // 2),
                                 (w, h - h // 3 // 2), width=3)
                win = True
                o_win = True
            if circle1 and circle4 and circle7:
                pygame.draw.line(screen, (255, 255, 255), (w // 3 // 2, 0), (w // 3 // 2, h),
                                 width=3)
                win = True
            if circle2 and circle5 and circle8:
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 - w // 3 // 2, 0),
                                 (w // 3 * 2 - w // 3 // 2, h),
                                 width=3)
                win = True
                o_win = True
            if circle3 and circle6 and circle9:
                pygame.draw.line(screen, (255, 255, 255), (w - w // 3 // 2, 0),
                                 (w - w // 3 // 2, h), width=3)
                win = True
                o_win = True
            if circle1 and circle5 and circle9:
                pygame.draw.line(screen, (255, 255, 255), (0, 0), (w, h), width=3)
                win = True
                o_win = True
            if circle3 and circle5 and circle7:
                pygame.draw.line(screen, (255, 255, 255), (0, w), (h, 0), width=3)
                win = True
                o_win = True
            if cross1 and cross2 and cross3:
                pygame.draw.line(screen, (255, 255, 255), (0, h // 3 // 2), (w, h // 3 // 2),
                                 width=3)
                win = True
                x_win = True
            if cross4 and cross5 and cross6:
                pygame.draw.line(screen, (255, 255, 255), (0, h // 3 * 2 - h // 3 // 2),
                                 (w, h // 3 * 2 - h // 3 // 2),
                                 width=3)
                win = True
                x_win = True
            if cross7 and cross8 and cross9:
                pygame.draw.line(screen, (255, 255, 255), (0, h - h // 3 // 2),
                                 (w, h - h // 3 // 2), width=3)
                win = True
                x_win = True
            if cross1 and cross4 and cross7:
                pygame.draw.line(screen, (255, 255, 255), (w // 3 // 2, 0), (w // 3 // 2, h),
                                 width=3)
                win = True
            if cross2 and cross5 and cross8:
                pygame.draw.line(screen, (255, 255, 255), (w // 3 * 2 - w // 3 // 2, 0),
                                 (w // 3 * 2 - w // 3 // 2, h),
                                 width=3)
                win = True
                x_win = True
            if cross3 and cross6 and cross9:
                pygame.draw.line(screen, (255, 255, 255), (w - w // 3 // 2, 0),
                                 (w - w // 3 // 2, h), width=3)
                win = True
                x_win = True
            if cross1 and cross5 and cross9:
                pygame.draw.line(screen, (255, 255, 255), (0, 0), (w, h), width=3)
                win = True
                x_win = True
            if cross3 and cross5 and cross7:
                pygame.draw.line(screen, (255, 255, 255), (0, w), (h, 0), width=3)
                win = True
                x_win = True
            if win:
                if x_win:
                    pygame.draw.rect(screen, pygame.Color('blue4'),
                                     pygame.Rect(w // 3 - 100, h // 3 + 100, w // 2 + 60,
                                                 h // 10 - 15))
                    fontObj = pygame.font.Font(None, 50)
                    textSurfaceObj = fontObj.render('Х - победили!', True, 'white')
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (w // 2, h // 2)
                    screen.blit(textSurfaceObj, textRectObj)
                else:
                    pygame.draw.rect(screen, pygame.Color('blue4'),
                                     pygame.Rect(w // 3 - 100, h // 3 + 100, w // 2 + 60,
                                                 h // 10 - 15))
                    fontObj = pygame.font.Font(None, 50)
                    textSurfaceObj = fontObj.render('0 - победили!', True, 'white')
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (w // 2, h // 2)
                    screen.blit(textSurfaceObj, textRectObj)
            if b == 9 and not win:
                pygame.draw.rect(screen, pygame.Color('blue4'),
                                 pygame.Rect(w // 3 - 15, h // 3 + 100, w // 2 - 100, h // 10 - 15))
                fontObj = pygame.font.Font(None, 50)
                textSurfaceObj = fontObj.render('Ничья!', True, 'white')
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (w // 2, h // 2)
                screen.blit(textSurfaceObj, textRectObj)
        pygame.display.flip()
    pygame.quit()
