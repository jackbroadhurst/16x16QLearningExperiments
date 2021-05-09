import numpy as np
from random import randint as r
import pygame
import random
pygame.init()
n = 16
colors = [(51, 51, 51) for i in range(16**2)]
reward = np.zeros((16, 16))
terminals = []
scrx = 16* 50
scry = 16* 50
screen = pygame.display.set_mode((scrx, scry))
font = pygame.font.SysFont('arial',45)

def layout(current_position, colors):
    colors[0] = (0, 0, 255)
    c = 0
    for i in range(0, scrx, 50):
        for j in range(0, scry, 50):
            pygame.draw.rect(screen, (255, 255, 255), (j, i, j + 50, i + 50), 0)
            pygame.draw.rect(screen, colors[c], (j + 10, i + 10, j + 45, i + 45), 0)
            c += 1
            pygame.draw.circle(screen, (255, 255, 0), (current_position[1] * 50 + 29, current_position[0] * 50 + 29),15, 0)

def overlay():
    text1 = font.render("1", True, (0, 0, 0))
    rect1 = text1.get_rect()
    rect1.center = ((7 * 50 + 25), (7 * 50 + 25))
    screen.blit(text1, rect1)
    text2 = font.render("2", True, (0, 0, 0))
    rect2 = text2.get_rect()
    rect2.center = ((12 * 50 + 25), (5 * 50 + 25))
    screen.blit(text2, rect2)
    text3 = font.render("3", True, (0, 0, 0))
    rect3 = text3.get_rect()
    rect3.center = ((15 * 50 + 25), (9 * 50 + 25))
    screen.blit(text3, rect3)
    text4 = font.render("4", True, (0, 0, 0))
    rect4 = text4.get_rect()
    rect4.center = ((0 * 50 + 25), (13 * 50 + 25))
    screen.blit(text4, rect4)

def overlayAlt():
    text1 = font.render("1", True, (0, 0, 0))
    rect1 = text1.get_rect()
    rect1.center = ((9 * 50 + 25), (0 * 50 + 25))
    screen.blit(text1, rect1)
    text2 = font.render("2", True, (0, 0, 0))
    rect2 = text2.get_rect()
    rect2.center = ((12 * 50 + 25), (5 * 50 + 25))
    screen.blit(text2, rect2)
    text3 = font.render("3", True, (0, 0, 0))
    rect3 = text3.get_rect()
    rect3.center = ((15 * 50 + 25), (9 * 50 + 25))
    screen.blit(text3, rect3)
    text4 = font.render("4", True, (0, 0, 0))
    rect4 = text4.get_rect()
    rect4.center = ((0 * 50 + 25), (13 * 50 + 25))
    screen.blit(text4, rect4)

class Mazes():
    def __init__(self):
        self.colors = colors
        self.terminals = terminals
        self.reward = reward

    def reset(self):
        global colors
        for i in range(8):
            for j in range(8):
                reward[(i, j)] = 0
        colors = [(51, 51, 51) for i in range(8** 2)]
        terminals.clear()

    def getMaze3Rewards(self):
        reward[0, 4] = -10
        reward[0, 8] = -10
        reward[0, 12] = -10
        reward[1, 0] = -10
        reward[1, 1] = -10
        reward[1, 2] = -10
        reward[1, 4] = -10
        reward[1, 5] = -10
        reward[1, 6] = -10
        reward[1, 8] = -10
        reward[1, 9] = -10
        reward[1, 10] = -10
        reward[1, 12] = -10
        reward[1, 13] = -10
        reward[1, 14] = -10
        reward[2, 1] = -10
        reward[2, 4] = -10
        reward[2, 12] = -10
        reward[3, 1] = -10
        reward[3, 2] = -10
        reward[3, 4] = -10
        reward[3, 5] = -10
        reward[3, 7] = -10
        reward[3, 9] = -10
        reward[3, 10] = -10
        reward[3, 15] = -10
        reward[4, 2] = -10
        reward[4, 4] = -10
        reward[4, 10] = -10
        reward[4, 12] = -10
        reward[4, 13] = -10
        reward[4, 15] = -10
        reward[5, 0] = -10
        reward[5, 2] = -10
        reward[5, 6] = -10
        reward[5, 8] = -10
        reward[5, 10] = -10
        reward[5, 13] = -10
        reward[6, 0] = -10
        reward[6, 4] = -10
        reward[6, 6] = -10
        reward[6, 8] = -10
        reward[6, 10] = -10
        reward[6, 12] = -10
        reward[6, 13] = -10
        reward[7, 1] = -10
        reward[7, 0] = -10
        reward[7, 2] = -10
        reward[7, 3] = -10
        reward[7, 4] = -10
        reward[7, 6] = -10
        reward[7, 8] = -10
        reward[8, 2] = -10
        reward[8, 9] = -10
        reward[8, 11] = -10
        reward[8, 13] = -10
        reward[8, 14] = -10
        reward[8, 15] = -10
        reward[9, 0] = -10
        reward[9, 2] = -10
        reward[9, 4] = -10
        reward[9, 5] = -10
        reward[9, 6] = -10
        reward[9, 7] = -10
        reward[9, 9] = -10
        reward[9, 10] = -10
        reward[9, 11] = -10
        reward[9, 13] = -10
        reward[9, 14] = -10
        reward[10, 0] = -10
        reward[10, 2] = -10
        reward[10, 4] = -10
        reward[10, 5] = -10
        reward[10, 6] = -10
        reward[10, 7] = -10
        reward[10, 9] = -10
        reward[10, 10] = -10
        reward[10, 14] = -10
        reward[11, 5] = -10
        reward[11, 6] = -10
        reward[11, 12] = -10
        reward[11, 14] = -10
        reward[12, 0] = -10
        reward[12, 1] = -10
        reward[12, 2] = -10
        reward[12, 3] = -10
        reward[12, 5] = -10
        reward[12, 6] = -10
        reward[12, 8] = -10
        reward[12, 10] = -10
        reward[12, 12] = -10
        reward[12, 13] = -10
        reward[12, 14] = -10
        reward[13, 3] = -10
        reward[13, 8] = -10
        reward[13, 10] = -10
        reward[13, 12] = -10
        reward[14, 0] = -10
        reward[14, 1] = -10
        reward[14, 3] = -10
        reward[14, 5] = -10
        reward[14, 7] = -10
        reward[14, 8] = -10
        reward[14, 10] = -10
        reward[14, 12] = -10
        reward[14, 14] = -10
        reward[15, 5] = -10
        reward[15, 8] = -10
        reward[15, 10] = -10
        reward[15, 14] = -10

        reward[7,7] = 10
        reward[5,12] = 15
        reward[9,15] = 20
        reward[13,0] = 25
        return reward

    def getMaze3Colours(self):
        colors[16 * 0 + 4] = (255, 0, 0)
        colors[16 * 0 + 8] = (255, 0, 0)
        colors[16 * 0 + 12] = (255, 0, 0)
        colors[16 * 1 + 0] = (255, 0, 0)
        colors[16 * 1 + 1] = (255, 0, 0)
        colors[16 * 1 + 2] = (255, 0, 0)
        colors[16 * 1 + 4] = (255, 0, 0)
        colors[16 * 1 + 5] = (255, 0, 0)
        colors[16 * 1 + 6] = (255, 0, 0)
        colors[16 * 1 + 8] = (255, 0, 0)
        colors[16 * 1 + 9] = (255, 0, 0)
        colors[16 * 1 + 10] = (255, 0, 0)
        colors[16 * 1 + 12] = (255, 0, 0)
        colors[16 * 1 + 13] = (255, 0, 0)
        colors[16 * 1 + 14] = (255, 0, 0)
        colors[16 * 2 + 1] = (255, 0, 0)
        colors[16 * 2 + 4] = (255, 0, 0)
        colors[16 * 2 + 12] = (255, 0, 0)
        colors[16 * 3 + 1] = (255, 0, 0)
        colors[16 * 3 + 2] = (255, 0, 0)
        colors[16 * 3 + 4] = (255, 0, 0)
        colors[16 * 3 + 5] = (255, 0, 0)
        colors[16 * 3 + 7] = (255, 0, 0)
        colors[16 * 3 + 9] = (255, 0, 0)
        colors[16 * 3 + 10] = (255, 0, 0)
        colors[16 * 3 + 15] = (255, 0, 0)
        colors[16 * 4 + 2] = (255, 0, 0)
        colors[16 * 4 + 4] = (255, 0, 0)
        colors[16 * 4 + 10] = (255, 0, 0)
        colors[16 * 4 + 12] = (255, 0, 0)
        colors[16 * 4 + 13] = (255, 0, 0)
        colors[16 * 4 + 15] = (255, 0, 0)
        colors[16 * 5 + 0] = (255, 0, 0)
        colors[16 * 5 + 2] = (255, 0, 0)
        colors[16 * 5 + 6] = (255, 0, 0)
        colors[16 * 5 + 8] = (255, 0, 0)
        colors[16 * 5 + 10] = (255, 0, 0)
        colors[16 * 5 + 13] = (255, 0, 0)
        colors[16 * 6 + 0] = (255, 0, 0)
        colors[16 * 6 + 4] = (255, 0, 0)
        colors[16 * 6 + 6] = (255, 0, 0)
        colors[16 * 6 + 8] = (255, 0, 0)
        colors[16 * 6 + 10] = (255, 0, 0)
        colors[16 * 6 + 12] = (255, 0, 0)
        colors[16 * 6 + 13] = (255, 0, 0)
        colors[16 * 7 + 1] = (255, 0, 0)
        colors[16 * 7 + 0] = (255, 0, 0)
        colors[16 * 7 + 2] = (255, 0, 0)
        colors[16 * 7 + 3] = (255, 0, 0)
        colors[16 * 7 + 4] = (255, 0, 0)
        colors[16 * 7 + 6] = (255, 0, 0)
        colors[16 * 7 + 8] = (255, 0, 0)
        colors[16 * 8 + 2] = (255, 0, 0)
        colors[16 * 8 + 9] = (255, 0, 0)
        colors[16 * 8 + 11] = (255, 0, 0)
        colors[16 * 8 + 13] = (255, 0, 0)
        colors[16 * 8 + 14] = (255, 0, 0)
        colors[16 * 8 + 15] = (255, 0, 0)
        colors[16 * 9 + 0] = (255, 0, 0)
        colors[16 * 9 + 2] = (255, 0, 0)
        colors[16 * 9 + 4] = (255, 0, 0)
        colors[16 * 9 + 5] = (255, 0, 0)
        colors[16 * 9 + 6] = (255, 0, 0)
        colors[16 * 9 + 7] = (255, 0, 0)
        colors[16 * 9 + 9] = (255, 0, 0)
        colors[16 * 9 + 10] = (255, 0, 0)
        colors[16 * 9 + 11] = (255, 0, 0)
        colors[16 * 9 + 13] = (255, 0, 0)
        colors[16 * 9 + 14] = (255, 0, 0)
        colors[16 * 10 + 0] = (255, 0, 0)
        colors[16 * 10 + 2] = (255, 0, 0)
        colors[16 * 10 + 4] = (255, 0, 0)
        colors[16 * 10 + 5] = (255, 0, 0)
        colors[16 * 10 + 6] = (255, 0, 0)
        colors[16 * 10 + 7] = (255, 0, 0)
        colors[16 * 10 + 9] = (255, 0, 0)
        colors[16 * 10 + 10] = (255, 0, 0)
        colors[16 * 10 + 14] = (255, 0, 0)
        colors[16 * 11 + 5] = (255, 0, 0)
        colors[16 * 11 + 6] = (255, 0, 0)
        colors[16 * 11 + 12] = (255, 0, 0)
        colors[16 * 11 + 14] = (255, 0, 0)
        colors[16 * 12 + 0] = (255, 0, 0)
        colors[16 * 12 + 1] = (255, 0, 0)
        colors[16 * 12 + 2] = (255, 0, 0)
        colors[16 * 12 + 3] = (255, 0, 0)
        colors[16 * 12 + 5] = (255, 0, 0)
        colors[16 * 12 + 6] = (255, 0, 0)
        colors[16 * 12 + 8] = (255, 0, 0)
        colors[16 * 12 + 10] = (255, 0, 0)
        colors[16 * 12 + 12] = (255, 0, 0)
        colors[16 * 12 + 13] = (255, 0, 0)
        colors[16 * 12 + 14] = (255, 0, 0)
        colors[16 * 13 + 3] = (255, 0, 0)
        colors[16 * 13 + 8] = (255, 0, 0)
        colors[16 * 13 + 10] = (255, 0, 0)
        colors[16 * 13 + 12] = (255, 0, 0)
        colors[16 * 14 + 0] = (255, 0, 0)
        colors[16 * 14 + 1] = (255, 0, 0)
        colors[16 * 14 + 3] = (255, 0, 0)
        colors[16 * 14 + 5] = (255, 0, 0)
        colors[16 * 14 + 7] = (255, 0, 0)
        colors[16 * 14 + 8] = (255, 0, 0)
        colors[16 * 14 + 10] = (255, 0, 0)
        colors[16 * 14 + 12] = (255, 0, 0)
        colors[16 * 14 + 14] = (255, 0, 0)
        colors[16 * 15 + 5] = (255, 0, 0)
        colors[16 * 15 + 8] = (255, 0, 0)
        colors[16 * 15 + 10] = (255, 0, 0)
        colors[16 * 15 + 14] = (255, 0, 0)

        colors[16 * 0 + 9] = (0, 255, 0)
        colors[16 * 5 + 12] = (0, 255, 0)
        colors[16 * 9 + 15] = (0, 255, 0)
        colors[16 * 13 + 0] = (0, 255, 0)
        return colors

    def getMaze3altRewards(self):
        reward[0, 4] = -10
        reward[0, 8] = -10
        reward[0, 12] = -10
        reward[1, 0] = -10
        reward[1, 1] = -10
        reward[1, 2] = -10
        reward[1, 4] = -10
        reward[1, 5] = -10
        reward[1, 6] = -10
        reward[1, 8] = -10
        reward[1, 9] = -10
        reward[1, 10] = -10
        reward[1, 12] = -10
        reward[1, 13] = -10
        reward[1, 14] = -10
        reward[2, 1] = -10
        reward[2, 4] = -10
        reward[2, 12] = -10
        reward[3, 1] = -10
        reward[3, 2] = -10
        reward[3, 4] = -10
        reward[3, 5] = -10
        reward[3, 7] = -10
        reward[3, 9] = -10
        reward[3, 10] = -10
        reward[3, 15] = -10
        reward[4, 2] = -10
        reward[4, 4] = -10
        reward[4, 10] = -10
        reward[4, 12] = -10
        reward[4, 13] = -10
        reward[4, 15] = -10
        reward[5, 0] = -10
        reward[5, 2] = -10
        reward[5, 6] = -10
        reward[5, 8] = -10
        reward[5, 10] = -10
        reward[5, 13] = -10
        reward[6, 0] = -10
        reward[6, 4] = -10
        reward[6, 6] = -10
        reward[6, 8] = -10
        reward[6, 10] = -10
        reward[6, 12] = -10
        reward[6, 13] = -10
        reward[7, 1] = -10
        reward[7, 0] = -10
        reward[7, 2] = -10
        reward[7, 3] = -10
        reward[7, 4] = -10
        reward[7, 6] = -10
        reward[7, 8] = -10
        reward[8, 2] = -10
        reward[8, 9] = -10
        reward[8, 11] = -10
        reward[8, 13] = -10
        reward[8, 14] = -10
        reward[8, 15] = -10
        reward[9, 0] = -10
        reward[9, 2] = -10
        reward[9, 4] = -10
        reward[9, 5] = -10
        reward[9, 6] = -10
        reward[9, 7] = -10
        reward[9, 9] = -10
        reward[9, 10] = -10
        reward[9, 11] = -10
        reward[9, 13] = -10
        reward[9, 14] = -10
        reward[10, 0] = -10
        reward[10, 2] = -10
        reward[10, 4] = -10
        reward[10, 5] = -10
        reward[10, 6] = -10
        reward[10, 7] = -10
        reward[10, 9] = -10
        reward[10, 10] = -10
        reward[10, 14] = -10
        reward[11, 5] = -10
        reward[11, 6] = -10
        reward[11, 12] = -10
        reward[11, 14] = -10
        reward[12, 0] = -10
        reward[12, 1] = -10
        reward[12, 2] = -10
        reward[12, 3] = -10
        reward[12, 5] = -10
        reward[12, 6] = -10
        reward[12, 8] = -10
        reward[12, 10] = -10
        reward[12, 12] = -10
        reward[12, 13] = -10
        reward[12, 14] = -10
        reward[13, 3] = -10
        reward[13, 8] = -10
        reward[13, 10] = -10
        reward[13, 12] = -10
        reward[14, 0] = -10
        reward[14, 1] = -10
        reward[14, 3] = -10
        reward[14, 5] = -10
        reward[14, 7] = -10
        reward[14, 8] = -10
        reward[14, 10] = -10
        reward[14, 12] = -10
        reward[14, 14] = -10
        reward[15, 5] = -10
        reward[15, 8] = -10
        reward[15, 10] = -10
        reward[15, 14] = -10

        reward[0, 9] = 10
        reward[5, 12] = 15
        reward[9, 15] = 20
        reward[13, 0] = 25
        return reward

    def getMaze3altColours(self):
        colors[16 * 0 + 4] = (255, 0, 0)
        colors[16 * 0 + 8] = (255, 0, 0)
        colors[16 * 0 + 12] = (255, 0, 0)
        colors[16 * 1 + 0] = (255, 0, 0)
        colors[16 * 1 + 1] = (255, 0, 0)
        colors[16 * 1 + 2] = (255, 0, 0)
        colors[16 * 1 + 4] = (255, 0, 0)
        colors[16 * 1 + 5] = (255, 0, 0)
        colors[16 * 1 + 6] = (255, 0, 0)
        colors[16 * 1 + 8] = (255, 0, 0)
        colors[16 * 1 + 9] = (255, 0, 0)
        colors[16 * 1 + 10] = (255, 0, 0)
        colors[16 * 1 + 12] = (255, 0, 0)
        colors[16 * 1 + 13] = (255, 0, 0)
        colors[16 * 1 + 14] = (255, 0, 0)
        colors[16 * 2 + 1] = (255, 0, 0)
        colors[16 * 2 + 4] = (255, 0, 0)
        colors[16 * 2 + 12] = (255, 0, 0)
        colors[16 * 3 + 1] = (255, 0, 0)
        colors[16 * 3 + 2] = (255, 0, 0)
        colors[16 * 3 + 4] = (255, 0, 0)
        colors[16 * 3 + 5] = (255, 0, 0)
        colors[16 * 3 + 7] = (255, 0, 0)
        colors[16 * 3 + 9] = (255, 0, 0)
        colors[16 * 3 + 10] = (255, 0, 0)
        colors[16 * 3 + 15] = (255, 0, 0)
        colors[16 * 4 + 2] = (255, 0, 0)
        colors[16 * 4 + 4] = (255, 0, 0)
        colors[16 * 4 + 10] = (255, 0, 0)
        colors[16 * 4 + 12] = (255, 0, 0)
        colors[16 * 4 + 13] = (255, 0, 0)
        colors[16 * 4 + 15] = (255, 0, 0)
        colors[16 * 5 + 0] = (255, 0, 0)
        colors[16 * 5 + 2] = (255, 0, 0)
        colors[16 * 5 + 6] = (255, 0, 0)
        colors[16 * 5 + 8] = (255, 0, 0)
        colors[16 * 5 + 10] = (255, 0, 0)
        colors[16 * 5 + 13] = (255, 0, 0)
        colors[16 * 6 + 0] = (255, 0, 0)
        colors[16 * 6 + 4] = (255, 0, 0)
        colors[16 * 6 + 6] = (255, 0, 0)
        colors[16 * 6 + 8] = (255, 0, 0)
        colors[16 * 6 + 10] = (255, 0, 0)
        colors[16 * 6 + 12] = (255, 0, 0)
        colors[16 * 6 + 13] = (255, 0, 0)
        colors[16 * 7 + 1] = (255, 0, 0)
        colors[16 * 7 + 0] = (255, 0, 0)
        colors[16 * 7 + 2] = (255, 0, 0)
        colors[16 * 7 + 3] = (255, 0, 0)
        colors[16 * 7 + 4] = (255, 0, 0)
        colors[16 * 7 + 6] = (255, 0, 0)
        colors[16 * 7 + 8] = (255, 0, 0)
        colors[16 * 8 + 2] = (255, 0, 0)
        colors[16 * 8 + 9] = (255, 0, 0)
        colors[16 * 8 + 11] = (255, 0, 0)
        colors[16 * 8 + 13] = (255, 0, 0)
        colors[16 * 8 + 14] = (255, 0, 0)
        colors[16 * 8 + 15] = (255, 0, 0)
        colors[16 * 9 + 0] = (255, 0, 0)
        colors[16 * 9 + 2] = (255, 0, 0)
        colors[16 * 9 + 4] = (255, 0, 0)
        colors[16 * 9 + 5] = (255, 0, 0)
        colors[16 * 9 + 6] = (255, 0, 0)
        colors[16 * 9 + 7] = (255, 0, 0)
        colors[16 * 9 + 9] = (255, 0, 0)
        colors[16 * 9 + 10] = (255, 0, 0)
        colors[16 * 9 + 11] = (255, 0, 0)
        colors[16 * 9 + 13] = (255, 0, 0)
        colors[16 * 9 + 14] = (255, 0, 0)
        colors[16 * 10 + 0] = (255, 0, 0)
        colors[16 * 10 + 2] = (255, 0, 0)
        colors[16 * 10 + 4] = (255, 0, 0)
        colors[16 * 10 + 5] = (255, 0, 0)
        colors[16 * 10 + 6] = (255, 0, 0)
        colors[16 * 10 + 7] = (255, 0, 0)
        colors[16 * 10 + 9] = (255, 0, 0)
        colors[16 * 10 + 10] = (255, 0, 0)
        colors[16 * 10 + 14] = (255, 0, 0)
        colors[16 * 11 + 5] = (255, 0, 0)
        colors[16 * 11 + 6] = (255, 0, 0)
        colors[16 * 11 + 12] = (255, 0, 0)
        colors[16 * 11 + 14] = (255, 0, 0)
        colors[16 * 12 + 0] = (255, 0, 0)
        colors[16 * 12 + 1] = (255, 0, 0)
        colors[16 * 12 + 2] = (255, 0, 0)
        colors[16 * 12 + 3] = (255, 0, 0)
        colors[16 * 12 + 5] = (255, 0, 0)
        colors[16 * 12 + 6] = (255, 0, 0)
        colors[16 * 12 + 8] = (255, 0, 0)
        colors[16 * 12 + 10] = (255, 0, 0)
        colors[16 * 12 + 12] = (255, 0, 0)
        colors[16 * 12 + 13] = (255, 0, 0)
        colors[16 * 12 + 14] = (255, 0, 0)
        colors[16 * 13 + 3] = (255, 0, 0)
        colors[16 * 13 + 8] = (255, 0, 0)
        colors[16 * 13 + 10] = (255, 0, 0)
        colors[16 * 13 + 12] = (255, 0, 0)
        colors[16 * 14 + 0] = (255, 0, 0)
        colors[16 * 14 + 1] = (255, 0, 0)
        colors[16 * 14 + 3] = (255, 0, 0)
        colors[16 * 14 + 5] = (255, 0, 0)
        colors[16 * 14 + 7] = (255, 0, 0)
        colors[16 * 14 + 8] = (255, 0, 0)
        colors[16 * 14 + 10] = (255, 0, 0)
        colors[16 * 14 + 12] = (255, 0, 0)
        colors[16 * 14 + 14] = (255, 0, 0)
        colors[16 * 15 + 5] = (255, 0, 0)
        colors[16 * 15 + 8] = (255, 0, 0)
        colors[16 * 15 + 10] = (255, 0, 0)
        colors[16 * 15 + 14] = (255, 0, 0)

        colors[16 * 0 + 9] = (0, 255, 0)
        colors[16 * 5 + 12] = (0, 255, 0)
        colors[16 * 9 + 15] = (0, 255, 0)
        colors[16 * 13 + 0] = (0, 255, 0)
        return colors

    def getMaze3Terminals(self):
        terminals.append(16 * 0 + 4)
        terminals.append(16 * 0 + 8)
        terminals.append(16 * 0 + 12)
        terminals.append(16 * 1 + 0)
        terminals.append(16 * 1 + 1)
        terminals.append(16 * 1 + 2)
        terminals.append(16 * 1 + 4)
        terminals.append(16 * 1 + 5)
        terminals.append(16 * 1 + 6)
        terminals.append(16 * 1 + 8)
        terminals.append(16 * 1 + 9)
        terminals.append(16 * 1 + 10)
        terminals.append(16 * 1 + 12)
        terminals.append(16 * 1 + 13)
        terminals.append(16 * 1 + 14)
        terminals.append(16 * 2 + 1)
        terminals.append(16 * 2 + 4)
        terminals.append(16 * 2 + 12)
        terminals.append(16 * 3 + 1)
        terminals.append(16 * 3 + 2)
        terminals.append(16 * 3 + 4)
        terminals.append(16 * 3 + 5)
        terminals.append(16 * 3 + 7)
        terminals.append(16 * 3 + 9)
        terminals.append(16 * 3 + 10)
        terminals.append(16 * 3 + 15)
        terminals.append(16 * 4 + 2)
        terminals.append(16 * 4 + 4)
        terminals.append(16 * 4 + 10)
        terminals.append(16 * 4 + 12)
        terminals.append(16 * 4 + 13)
        terminals.append(16 * 4 + 15)
        terminals.append(16 * 5 + 0)
        terminals.append(16 * 5 + 2)
        terminals.append(16 * 5 + 6)
        terminals.append(16 * 5 + 8)
        terminals.append(16 * 5 + 10)
        terminals.append(16 * 5 + 13)
        terminals.append(16 * 6 + 0)
        terminals.append(16 * 6 + 4)
        terminals.append(16 * 6 + 6)
        terminals.append(16 * 6 + 8)
        terminals.append(16 * 6 + 10)
        terminals.append(16 * 6 + 12)
        terminals.append(16 * 6 + 13)
        terminals.append(16 * 7 + 1)
        terminals.append(16 * 7 + 0)
        terminals.append(16 * 7 + 2)
        terminals.append(16 * 7 + 3)
        terminals.append(16 * 7 + 4)
        terminals.append(16 * 7 + 6)
        terminals.append(16 * 7 + 8)
        terminals.append(16 * 8 + 2)
        terminals.append(16 * 8 + 9)
        terminals.append(16 * 8 + 11)
        terminals.append(16 * 8 + 13)
        terminals.append(16 * 8 + 14)
        terminals.append(16 * 8 + 14)
        terminals.append(16 * 9 + 0)
        terminals.append(16 * 9 + 2)
        terminals.append(16 * 9 + 4)
        terminals.append(16 * 9 + 5)
        terminals.append(16 * 9 + 6)
        terminals.append(16 * 9 + 7)
        terminals.append(16 * 9 + 9)
        terminals.append(16 * 9 + 10)
        terminals.append(16 * 9 + 11)
        terminals.append(16 * 9 + 13)
        terminals.append(16 * 9 + 14)
        terminals.append(16 * 10 + 0)
        terminals.append(16 * 10 + 2)
        terminals.append(16 * 10 + 4)
        terminals.append(16 * 10 + 5)
        terminals.append(16 * 10 + 6)
        terminals.append(16 * 10 + 7)
        terminals.append(16 * 10 + 9)
        terminals.append(16 * 10 + 10)
        terminals.append(16 * 10 + 14)
        terminals.append(16 * 11 + 5)
        terminals.append(16 * 11 + 6)
        terminals.append(16 * 11 + 12)
        terminals.append(16 * 11 + 14)
        terminals.append(16 * 12 + 0)
        terminals.append(16 * 12 + 1)
        terminals.append(16 * 12 + 2)
        terminals.append(16 * 12 + 5)
        terminals.append(16 * 12 + 6)
        terminals.append(16 * 12 + 8)
        terminals.append(16 * 12 + 10)
        terminals.append(16 * 12 + 12)
        terminals.append(16 * 12 + 13)
        terminals.append(16 * 12 + 14)
        terminals.append(16 * 13 + 3)
        terminals.append(16 * 13 + 8)
        terminals.append(16 * 13 + 10)
        terminals.append(16 * 13 + 12)
        terminals.append(16 * 14 + 0)
        terminals.append(16 * 14 + 1)
        terminals.append(16 * 14 + 3)
        terminals.append(16 * 14 + 5)
        terminals.append(16 * 14 + 7)
        terminals.append(16 * 14 + 8)
        terminals.append(16 * 14 + 10)
        terminals.append(16 * 14 + 12)
        terminals.append(16 * 14 + 14)
        terminals.append(16 * 15 + 5)
        terminals.append(16 * 15 + 8)
        terminals.append(16 * 15 + 10)
        terminals.append(16 * 15 + 14)
        return terminals