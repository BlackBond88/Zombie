import pygame as pg


def load_image(weapon, action, n_image):
    a = 2.8  # уменьшаем картинку в А раз TODO
    images = []
    for i in range(n_image):
        name = 'Images/Top_Down_Survivor/' + weapon + '/' + action + \
               '/survivor-' + action + '_' + weapon + '_' + str(i) + '.png'
        image = pg.image.load(name).convert_alpha()
        image = pg.transform.scale(image, (image.get_width() // a, image.get_height() // a))
        images.append(image)
    return images
