import pygame
import random

pygame.init()

def ajouter_mot():
    nouveau_mot = input("voulez vous rajoutez un mot ? allez y: Sinon marquer non ")
    if not nouveau_mot:
        return

    with open("mot.txt", "a") as file:
        if nouveau_mot == "non":
            print("Lancement du jeu")
            return
        else:
            file.write(nouveau_mot + "\n")
            print("Mot rajouté UwU bonne game")
ajouter_mot()

fond = (0, 0, 0)


fenetre = pygame.display.set_mode((600, 500))
pygame.display.set_caption("jeudupendu")


font = pygame.font.Font(None, 36)
font_bouton = pygame.font.Font(None, 24)


with open("mot.txt", "r") as file:
    mot = file.readlines()


def dessiner_bouton(surface, x, y, largeur, hauteur, couleur, message):
    pygame.draw.rect(surface, couleur, (x, y, largeur, hauteur))
    text = font_bouton.render(message, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (x + largeur // 2, y + hauteur // 2)
    surface.blit(text, text_rect)

def relancer():
    global erreur
    global lettrecorrect
    global motatrouver
    erreur = 0
    lettrecorrect = []
    motatrouver = random.choice(mot).strip().lower()

erreur = 0
lettrecorrect = []
motatrouver = random.choice(mot).strip().lower()


jeu = True
while jeu:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha() and len(event.unicode) == 1:
                letter = event.unicode.lower()
                if letter in motatrouver:
                    lettrecorrect.append(letter)
                else:
                    erreur += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 150 <= pos[0] <= 250 and 400 <= pos[1] <= 450:
                relancer()

    fenetre.fill((255, 255, 255))
    dessiner_bouton(fenetre, 150, 400, 100, 50, fond, "Relancer")


    if erreur >= 1:
        pygame.draw.line(fenetre, fond, [100, 400], [100, 50], 5)
    if erreur >= 2:
        pygame.draw.line(fenetre, fond, [100, 50], [200, 50], 5)
    if erreur >= 3:
        pygame.draw.line(fenetre, fond, [200, 50], [200, 75], 5)
    if erreur >= 4:
        pygame.draw.circle(fenetre, fond, [200, 95], 20)
    if erreur >= 5:
        pygame.draw.line(fenetre, fond, [200, 115], [200, 200], 5)
    if erreur >= 6:
        pygame.draw.line(fenetre, fond, [200, 145], [175, 125], 5)
        pygame.draw.line(fenetre, fond, [200, 145], [225, 125], 5)
    if erreur >= 7:
        pygame.draw.line(fenetre, fond, [200, 200], [175, 250], 5)
        pygame.draw.line(fenetre, fond, [200, 200], [225, 250], 5)

    x = 150
    for lettre in motatrouver:
        if lettre in lettrecorrect:
            text = font.render(lettre, True, fond)
            fenetre.blit(text, [x, 300])
            x += 30
        else:
            text = font.render("_", True, fond)
            fenetre.blit(text, [x, 300])
            x += 30

    pygame.display.update()

    if erreur >= 7 or set(lettrecorrect) == set(motatrouver):
        jeu = False
        if set(lettrecorrect) == set(motatrouver):
            print("Bien joué !")
        else:
            print("Désolé, tu as perdu :c Tente ta chance en relançant")



pygame.quit()