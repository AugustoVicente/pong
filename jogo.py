# -*- coding: utf-8 -*-
from pyprocessing import *
posicao_x_inicial = 50 # posicao y bola no inicio
posicao_y_inicial = 50 # posicao y bola no inicio
raio = 20 # raio da bola
velocidadeX = -5 # velocidade x da bola
velocidadeY = 5 # velocidade y da bola
barra_x = 225   # posição x da barra
barra_y = 450  # posição y da barra
larg_barra = 150 # largura da barra
alt_barra = 10 # altura da barra
vel = 5 # velocidade da barra
vidas = 3 # vidas
vivo = True
pts = 0 # contador de pontos
def setup():
	size(700, 500)
	textSize(30)
	text(str(pts), 10, 30)
def detecta_tecla():	
    global barra_x, vel
    if key.pressed: # detecta alguma tecla pressionada
        if key.code == LEFT:
			if barra_x > 0:
				barra_x -= vel
        elif key.code == RIGHT:
            if barra_x < 570:
                barra_x += vel
def draw():
	global posicao_x_inicial, posicao_y_inicial, raio, velocidadeX, velocidadeY, pts # declarando escopo
	background(60, 47, 47) # cor de fundo
	text(str(pts), 30, 70)
	verificar_contato()
	if vivo == True:
		ellipse(posicao_x_inicial, posicao_y_inicial, raio, raio) # desenhar o circulo
		posicao_x_inicial = posicao_x_inicial + velocidadeX
		posicao_y_inicial = posicao_y_inicial + velocidadeY
		fill(255,255,255)
		rect(barra_x, barra_y, larg_barra, alt_barra) # desenhando barra
		detecta_tecla()
	else:
		text("Fim de jogo, voce fez "+str(pts)+" pontos, parabens", 150, 150)
		textSize(20)
		text("clique na tela para recomecar", 150, 250)
def mouseClicked(): 
	global pts, vivo, posicao_y_inicial, posicao_x_inicial
	if vivo == False:
		pts = 0
		vivo = True
		posicao_x_inicial = 50 # resetar a posicao y bola no inicio
		posicao_y_inicial = 50 # resetar a posicao y bola no inicio
def verificar_contato():
	global posicao_x_inicial, posicao_y_inicial, barra_x, barra_y, larg_barra, alt_barra, raio, velocidadeX, velocidadeY, pts, vivo
	if vivo == True:
		if posicao_x_inicial >= 700 - raio/2: # relou na parede direita
			velocidadeX = velocidadeX * -1
		elif posicao_x_inicial <= raio/2: # relou na parede esquerda
			velocidadeX = velocidadeX * -1
		if posicao_y_inicial >= (barra_y + alt_barra) - raio:
			if posicao_x_inicial > (barra_x) and posicao_x_inicial < (barra_x + larg_barra): # relou na barra
				pts = pts + 1
				velocidadeY = velocidadeY  * -1
			else: # derrota
				vivo = False
		elif posicao_y_inicial <= raio/2: # bateu no teto
			velocidadeY = velocidadeY * -1
run()
  