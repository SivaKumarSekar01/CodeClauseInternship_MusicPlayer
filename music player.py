import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption("Music Player")
        self.clock = pygame.time.Clock()
        self.music_directory = "path/to/your/music/directory"
        self.playlist = []
        self.current_index = 0

    def load_music(self):
        for file in os.listdir(self.music_directory):
            if file.endswith(".mp3"):
                self.playlist.append(os.path.join(self.music_directory, file))
    
    def play_music(self):
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def prev_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()

    def run(self):
        self.load_music()
        self.play_music()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.pause()
                    elif event.key == pygame.K_n:
                        self.next_song()
                    elif event.key == pygame.K_p:
                        self.prev_song()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
