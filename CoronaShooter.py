import arcade
import random
ScreenWidth = 1000
ScreenHeight = 600
ScreenTitle = "Corona Shooter"
Scaling = 1.0

class FlyingSprite(arcade.Sprite):
    def update(self):
        super().update()
        if self.right < 0:
            self.remove_from_sprite_lists()
            
class otherFlyingSprite(arcade.Sprite):
    def update(self):
        super().update()
        if self.left > ScreenWidth:
            self.remove_from_sprite_lists()
            
class Shooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        #Loots e muitas outras variáveis a serem configuradas
        #como sons,imagens, valores referentes a quantidade de vida etc..
    
        self.inimigo_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.planeta_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.barradevida_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.pickup_list = arcade.SpriteList()
        self.colisaosound1 = arcade.load_sound("sons/explosion1.wav")
        self.colisaosound2 = arcade.load_sound("sons/explosion2.wav")
        self.bgmusic = arcade.load_sound("sons/space.wav")
        self.lasersound = arcade.load_sound("sons/laser.wav")
        self.titlemusic = arcade.load_sound("sons/title.wav")
        self.powerupsound = arcade.load_sound("sons/powerup.wav")
        self.lives = 3
        self.paused = bool()
        self.gamestarted = bool()
        self.gameover = bool()
        self.gamestarted = False
        self.pontos = int()
        self.highpontos = int()
        
        hipontosFile = open("arquivos/highpontos.txt")
        for value in hipontosFile:
            self.highpontos = int(value)
        hipontosFile.close()
       
    def add_inimigo(self, delta_time : float):
        inimigo = FlyingSprite("imagens/inimigo.png", 0.15)
        inimigo.left = random.randint(self.width, self.width + 80)
        inimigo.top = random.randint(10, self.height)
        inimigo.velocity = (random.randint(-13, -6), 0)
        #O atributo de velocidade de qualquer objeto tem um valor X e um Y
        self.inimigo_list.append(inimigo)
        self.all_sprites.append(inimigo)

    def add_star(self, delta_time : float):
        star = FlyingSprite("imagens/estrela.png", random.uniform(0.01, 0.0175))
        star.left = random.randint(self.width, self.width + 80)
        star.top = random.randint(10, self.height - 10)
        star.velocity = (random.randint(-12, -2), 0)
        #O atributo de velocidade de qualquer objeto tem um valor X e um Y
        self.star_list.append(star)
        self.all_sprites.append(star)
        
    def add_laser(self):
        if self.gamestarted==True:
            laser = otherFlyingSprite("imagens/laser.png", 0.025)
            laser.center_x = self.player.center_x + 5
            laser.center_y = self.player.center_y
            laser.velocity = (+10, 0)
            self.lasersound.play(volume = 0.050)
            self.laser_list.append(laser)
            self.all_sprites.append(laser)

    def add_pickup(self, delta_time : float):
        if self.lives != 3:
            pickup = FlyingSprite("imagens/VidaExtra.png", 0.09)
            pickup.left = random.randint(self.width, self.width + 80)
            pickup.top = random.randint(10, self.height)
            pickup.velocity = (-5, 0)
            #O atributo de velocidade de qualquer objeto tem um valor X e um Y
            self.pickup_list.append(pickup)
            self.all_sprites.append(pickup)
                    
    def planetasetup(self):
        planetanumber = random.randint(1, 4)
        if planetanumber == 1:
            planeta = FlyingSprite("imagens/planeta1.png", random.uniform(0.05, 0.125))
            return planeta
        elif planetanumber == 2:
            planeta = FlyingSprite("imagens/planeta2.png", random.uniform(0.05, 0.125))
            return planeta
        elif planetanumber == 3:
            planeta = FlyingSprite("imagens/planeta3.png", random.uniform(0.05, 0.125))
            return planeta
        else:
            planeta = FlyingSprite("imagens/planeta4.png", random.uniform(0.05, 0.125))
            return planeta
        
    def add_planeta(self, delta_time : float):
        planeta = self.planetasetup()
        planeta.left = random.randint(self.width, self.width + 80)
        planeta.top = random.randint(10, self.height - 10)
        planeta.velocity = (random.randint(-5, -1), 0)
        #O atributo de velocidade de qualquer objeto tem um valor X e um Y
        self.planeta_list.append(planeta)
        self.all_sprites.append(planeta)
        
    def barradevidasetup(self):
        self.life1 = arcade.Sprite("imagens/barradevida1.png", 1.5)
        self.life2 = arcade.Sprite("imagens/barradevida2.png", 1.5)
        self.life3 = arcade.Sprite("imagens/barradevida3.png", 1.5)
        self.life1.left = 0
        self.life2.left = 0
        self.life3.left = 0
        self.life1.bottom = 0
        self.life2.bottom = 0
        self.life3.bottom = 0
        
    def titlesetup(self):
        self.pontos = 0
        arcade.set_background_color(arcade.color.BLACK)
        self.title = arcade.Sprite("imagens/titulo.png", 1)
        self.all_sprites.append(self.title)
        self.title.center_x = self.width / 2 
        self.title.center_y = self.height / 2
        arcade.schedule(self.add_star, 0.1)
        arcade.schedule(self.add_planeta, 1.5)
        self.titlemusic.play(volume = 0.125)
        
    def setup(self):
        self.player = arcade.Sprite("imagens/player.png", 0.15)
        if self.gamestarted == True:
            self.lives = 3
            self.pontos = 0
            self.titlemusic.stop()
            self.all_sprites.append(self.player)
            self.barradevidasetup()
            self.player.center_y = self.height / 2
            self.player.left = 10
            arcade.schedule(self.add_inimigo, 0.35)
            arcade.schedule(self.add_pickup, 10)
            self.bgmusic.play(volume = 0.160)
        
    def on_draw(self):
        arcade.start_render()
        self.star_list.draw()
        self.planeta_list.draw()
        self.title.draw()
        self.inimigo_list.draw()
        self.pickup_list.draw()
        if self.gamestarted==True:
            self.laser_list.draw()
            self.player.draw()
            arcade.draw_text("PONTUACAO: " + str(self.pontos), 0, ScreenHeight, arcade.color.WHITE, 20, anchor_x = "left", anchor_y = "top", font_name = 'fontes/pontosfont2.ttf')
            arcade.draw_text("MAIOR PONTUACAO: " + str(self.highpontos), ScreenWidth, ScreenHeight, arcade.color.WHITE, 20, anchor_x = "right", anchor_y = "top", font_name = 'fonts/pontosfont2.ttf')
            if self.lives == 3:
                self.life3.draw()
            elif self.lives == 2:
                self.life2.draw()
            elif self.lives == 1:
                self.life1.draw()
        if self.gameover == True:
            self.gameovertext.draw()
            
    def on_key_press(self, keypressed, modifier):
        if keypressed==arcade.key.W or keypressed==arcade.key.UP:
            self.player.change_y = 5
        if keypressed==arcade.key.S or keypressed==arcade.key.DOWN:
            self.player.change_y = -5
        if keypressed==arcade.key.A or keypressed==arcade.key.LEFT:
            self.player.change_x = -5
        if keypressed==arcade.key.D or keypressed==arcade.key.RIGHT:
            self.player.change_x = 5
            
        if keypressed==arcade.key.Q:
            arcade.close_window()
        if keypressed==arcade.key.P:
            if self.paused == False:
                arcade.unschedule(self.add_inimigo)
                arcade.unschedule(self.add_star)
                arcade.unschedule(self.add_planeta)
                arcade.unschedule(self.add_pickup)
            else:
                arcade.schedule(self.add_inimigo, 0.35)
                arcade.schedule(self.add_star, 0.1)
                arcade.schedule(self.add_planeta, 1.5)
                arcade.schedule(self.add_pickup, 10)
            self.paused = not self.paused
            
        if keypressed == arcade.key.SPACE:
            self.add_laser()
        
        if self.gamestarted == False:
            if keypressed==arcade.key.ENTER:
                self.gamestarted = True
                self.title.remove_from_sprite_lists()
                self.setup()
                
        if self.gameover == True:
            if keypressed == arcade.key.ENTER:
                self.gameover = False
                self.gameovertext.remove_from_sprite_lists()
                self.setup()
            if keypressed == arcade.key.ESCAPE:
                arcade.close_window()
    
    def on_update(self, delta_time):
        if self.paused:
            return
        
        if self.gamestarted == True:
            colisaolist = self.player.collides_with_list(self.inimigo_list)
            
            if colisaolist:
                for thing in colisaolist:
                    thing.remove_from_sprite_lists()
                self.lives = self.lives - 1
                colisaodecider = random.randint(1,2)
                if colisaodecider == 1:
                    self.colisaosound1.play(volume = 0.05)
                else:
                    self.colisaosound2.play(volume = 0.05)
                if self.lives == 0:
                    self.player.remove_from_sprite_lists()
                    self.bgmusic.stop()
                    hipontos = open("arquivos/highpontos.txt", 'w')
                    hipontos.write(str(self.highpontos))
                    hipontos.close()
                    self.game_over()
                    
                    
            pickupcolisao = self.player.collides_with_list(self.pickup_list)
                    
            if pickupcolisao:
                self.powerupsound.play(volume = 0.1)
                for pickup in pickupcolisao:
                    pickup.remove_from_sprite_lists()
                if self.lives != 3:
                    self.lives = self.lives + 1
                    
                    
            
            for laser in self.laser_list:
                lasercolisao = laser.collides_with_list(self.inimigo_list)
                if lasercolisao:
                    for thing in lasercolisao:
                        thing.remove_from_sprite_lists()
                    colisaodecider = random.randint(1,2)
                    if colisaodecider == 1:
                        self.colisaosound1.play(volume = 0.05)
                    else:
                        self.colisaosound2.play(volume = 0.05)
                    laser.remove_from_sprite_lists()
                    self.pontos = self.pontos + 100
                    
            if self.pontos >= self.highpontos:
                self.highpontos = self.pontos
            
        self.all_sprites.update()
        
        if self.gamestarted == True:
            if self.player.top > self.height:
                self.player.top = self.height
            if self.player.bottom < 0:
                self.player.bottom = 0
            if self.player.right > self.width:
                self.player.right = self.width
            if self.player.left < 0:
                self.player.left = 0
            
    def on_key_release(self, keypressed, modifier):
        if keypressed==arcade.key.W or keypressed==arcade.key.UP or keypressed==arcade.key.S or keypressed==arcade.key.DOWN:
            self.player.change_y = 0
        if keypressed==arcade.key.A or keypressed==arcade.key.LEFT or keypressed==arcade.key.D or keypressed==arcade.key.RIGHT:
            self.player.change_x = 0
            
    def game_over(self):
        self.gameover = True
        self.gameovertext = arcade.Sprite("imagens/gameover.png", 0.75)
        self.all_sprites.append(self.gameovertext)
        self.gameovertext.center_x = self.width / 2 
        self.gameovertext.center_y = self.height / 2
        arcade.unschedule(self.add_inimigo)
        arcade.unschedule(self.add_pickup)
        
app = Shooter(ScreenWidth, ScreenHeight, ScreenTitle)
app.titlesetup()
arcade.run()