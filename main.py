import pygame

pygame.init()

ANCHO = 1000
ALTO = 700

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dante - Mascota Virtual de Informática")

reloj = pygame.time.Clock()

# Variables de estado
energia = 80
animo = 80
bugs = 20


# colores del colegio
BORDO = (128, 0, 32)
AMARILLO = (255, 200, 0)
ROJO = (180, 30, 30)
BLANCO = (255, 255, 255)

# cargar imágenes
delfi_feliz = pygame.image.load("Imagenes/Dante_feliz.PNG").convert_alpha()
delfi_programando = pygame.image.load("Imagenes/Dante_programando.PNG").convert_alpha()
delfi_cansado = pygame.image.load("Imagenes/Dante_cansado.PNG").convert_alpha()
delfi_bugs = pygame.image.load("Imagenes/Dante_con_Errores.PNG").convert_alpha()

escudo = pygame.image.load("Imagenes/Escudo.png").convert_alpha()

# cambiar tamaño de las imágenes
delfi_feliz = pygame.transform.scale(delfi_feliz, (300, 300))
delfi_programando = pygame.transform.scale(delfi_programando, (300, 300))
delfi_cansado = pygame.transform.scale(delfi_cansado, (300, 300))
delfi_bugs = pygame.transform.scale(delfi_bugs, (300, 300))

escudo = pygame.transform.scale(escudo, (100, 100))


# Función para dibujar las barras
def dibujar_barra(pantalla, x, y, valor, color, nombre):
    # Fondo de la barra
    pygame.draw.rect(pantalla, (220, 220, 220), (x, y, 250, 30))

    # Parte llena de la barra
    pygame.draw.rect(pantalla, color, (x, y, valor * 2.5, 30))

    # Texto
    fuente = pygame.font.Font(None, 28)
    texto = fuente.render(nombre + ": " + str(valor), True, (0, 0, 0))
    pantalla.blit(texto, (x, y - 30))

# Botones
boton_alimentar = pygame.Rect(50, 450, 180, 60)
boton_programar = pygame.Rect(250, 450, 180, 60)
boton_jugar = pygame.Rect(50, 530, 180, 60)
boton_bugs = pygame.Rect(250, 530, 180, 60)


ultimo_desgaste = pygame.time.get_ticks()
programando_hasta = 0

ejecutando = True

while ejecutando:

   for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        ejecutando = False

    if evento.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = evento.pos

    

        # Alimentar
        if boton_alimentar.collidepoint(mouse_x, mouse_y):
            energia = min(100, energia + 15)
            animo = min(100, animo + 5)

       # Programar
        if boton_programar.collidepoint(mouse_x, mouse_y):
            energia = max(0, energia - 10)
            animo = min(100, animo + 5)
            bugs = min(100, bugs + 10)
            programando_hasta = pygame.time.get_ticks() + 2000

        # Jugar
        if boton_jugar.collidepoint(mouse_x, mouse_y):
            energia = max(0, energia - 10)
            animo = min(100, animo + 20)

        # Reparar bugs
        if boton_bugs.collidepoint(mouse_x, mouse_y):
            energia = max(0, energia - 5)
            bugs = max(0, bugs - 10)
            animo = max(0, animo - 15)

            
        # Desgaste automatico cada 5 segundos
        tiempo_actual = pygame.time.get_ticks()

        if tiempo_actual - ultimo_desgaste >= 5000:
            energia = max(0, energia - 2)
            animo = max(0, animo - 1)
            bugs = min(100, bugs + 2)

            ultimo_desgaste = tiempo_actual

    # Fondo
    pantalla.fill(BLANCO)

    # Encabezado bordó
    pygame.draw.rect(pantalla, BORDO, (0, 0, ANCHO, 100))

    # Título
    fuente_titulo = pygame.font.Font(None, 45)
    titulo = fuente_titulo.render(
        "DANTE - MASCOTA VIRTUAL DE INFORMÁTICA",
        True,
        BLANCO
    )

    pantalla.blit(titulo, (180, 30))

    # Escudo
    pantalla.blit(escudo, (40, 0))

    # Elegir imagen según el estado de Dante
    if energia <= 25:
        delfi_actual = delfi_cansado
    elif bugs >= 70:
        delfi_actual = delfi_bugs
    elif pygame.time.get_ticks() < programando_hasta:
        delfi_actual = delfi_programando
    else:
        delfi_actual = delfi_feliz

    # Dante
    pantalla.blit(delfi_actual, (350, 130))

    # Barras de estado
    dibujar_barra(pantalla, 50, 180, energia, (255, 200, 0), "Energia")
    dibujar_barra(pantalla, 50, 270, animo, (180, 30, 30), "Animo")
    dibujar_barra(pantalla, 50, 360, 100 - bugs, (128, 0, 32), "Bugs")

    # Dibujar botones
    pygame.draw.rect(pantalla, AMARILLO, boton_alimentar)
    pygame.draw.rect(pantalla, BORDO, boton_programar)
    pygame.draw.rect(pantalla, ROJO, boton_jugar)
    pygame.draw.rect(pantalla, BORDO, boton_bugs)

    # Texto de los botones
    fuente_botones = pygame.font.Font(None, 28)

    texto = fuente_botones.render("Alimentar", True, (0, 0, 0))
    pantalla.blit(texto, (boton_alimentar.x + 45, boton_alimentar.y + 20))

    texto = fuente_botones.render("Programar", True, BLANCO)
    pantalla.blit(texto, (boton_programar.x + 45, boton_programar.y + 20))

    texto = fuente_botones.render("Jugar", True, BLANCO)
    pantalla.blit(texto, (boton_jugar.x + 65, boton_jugar.y + 20))

    texto = fuente_botones.render("Reparar Bugs", True, BLANCO)
    pantalla.blit(texto, (boton_bugs.x + 25, boton_bugs.y + 20))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()