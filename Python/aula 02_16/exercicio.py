import pyautogui as p

# Abrindo o google chrome
p.moveTo(x=41, y=444, duration=1)
p.click(x=41, y=444)
p.click(x=41, y=444)

# Selecionando a barra de navegação
p.moveTo(x=583, y=51, duration=1)
p.click(x=583, y=51)

# Abrindo a page do Github
p.typewrite('github')
p.hotkey('enter')
p.sleep(3)
p.moveTo(x=1306, y=109, duration=1)
p.click(x=1306, y=109)
p.sleep(4)

# Digitando Usuario e Senha
p.typewrite('marcioalbertoo.lourenco@gmail.com')
p.hotkey('Tab')
p.typewrite('031060@mA')
p.hotkey('enter')

# Abrindo Repositorio
p.sleep(3)
p.moveTo(x=1531, y=100, duration=1)
p.click(x=1531, y=100)
p.moveTo(x=1436, y=225, duration=1)
p.click(x=1436, y=225)
p.sleep(3)
p.moveTo(x=700, y=179, duration=1)
p.click(x=700, y=179)
p.moveTo(x=1360, y=235, duration=1)
p.click(x=1360, y=235)

# Criando Repositorio
p.sleep(3)
p.moveTo(x=695, y=331, duration=1)
p.click(x=695, y=331)
p.typewrite('Automacao Python')
p.hotkey('Tab')
p.typewrite('Criando repositorio com automacao em python')
p.moveTo(x=446, y=669, duration=1)
p.click(x=446, y=669)
p.scroll(-250)
p.moveTo(x=530, y=572, duration=1)
p.click(x=530, y=572)
p.sleep(2)
p.typewrite('python')
p.moveTo(x=514, y=692, duration=1)
p.click(x=514, y=692)
p.moveTo(x=522, y=815, duration=1)
p.click(x=522, y=815)

#Clonando o Repositorio
p.sleep(3)
p.moveTo(x=1038, y=284, duration=1)
p.click(x=1038, y=284)
p.moveTo(x=1041, y=458, duration=1)
p.click(x=1041, y=458)
p.moveTo(x=464, y=878, duration=1)
p.click(x=464, y=878)
p.moveTo(x=104, y=190, duration=1)
p.click(x=104, y=190)
p.moveTo(x=186, y=877, duration=1)
p.click(x=186, y=877)
p.typewrite('cmd')
p.hotkey('Enter')
p.sleep(3)
p.typewrite('cd documents')
p.hotkey('Enter')
p.typewrite('git clone ')
p.hotkey('ctrl', 'v')
p.hotkey('Enter')

#Abrindo o repositorio pelo VSCode
p.sleep(8)
p.typewrite('cd Automacao-Python')
p.hotkey('Enter')
p.typewrite('code .')
p.hotkey('Enter')
p.sleep(6)
p.moveTo(x=420, y=141, duration=1)
p.click(x=420, y=141)
p.typewrite('automacao.py')
p.hotkey('Enter')
