import pyautogui as p

# Abrindo o google chrome
p.moveTo(x=41, y=444, duration=1)
p.click(x=41, y=444)
p.click(x=41, y=444)

# Selecionando a barra de navegação
p.moveTo(x=583, y=51, duration=1)
p.click(x=583, y=51)

# Abrindo a page do Python
p.typewrite('python')
p.hotkey('enter')
p.sleep(3)
p.moveTo(x=363, y=308, duration=1)
p.click(x=363, y=308)
p.sleep(3)

# Fazendo pesquisa aleatoria
p.moveTo(x=583, y=51, duration=1)
p.click(x=583, y=51)
p.typewrite('julio cocorico')
p.hotkey('enter')
