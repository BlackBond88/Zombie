

def load_image(weapon, action, n_image):
    image_names = []
    for i in range(n_image):
        name = 'Images/Top_Down_Survivor/' + weapon + '/' + action + '/survivor-' + action + '_' + weapon + '_' + str(i) + '.png'
        image_names.append(name)
    return image_names