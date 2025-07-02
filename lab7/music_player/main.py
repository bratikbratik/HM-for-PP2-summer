import os
import pygame

pygame.init()
pygame.mixer.init()

w, h = 600, 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

FONT = pygame.font.SysFont("Type42", 42)
SMALL_FONT = pygame.font.SysFont("Type42", 24)

clock = pygame.time.Clock()
end_event = pygame.USEREVENT + 1

class Button:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_surf = SMALL_FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

class MusicPlayer:
    def __init__(self):
        self._songs = [f for f in os.listdir("music_player/music") if f.endswith(('.mp3', '.wav'))]
        self._current = 0
        self._is_paused = False
        pygame.mixer.music.set_endevent(end_event)

    def play(self):
        if pygame.mixer.music.get_busy():
            self._is_paused = True
            pygame.mixer.music.pause()
        else:
            if self._is_paused:
                self._is_paused = False
                pygame.mixer.music.unpause()
            else:
                self.load_current()
                pygame.mixer.music.play()

    def stop(self):
        self._is_paused = False
        pygame.mixer.music.stop()

    def next(self):
        self._current = (self._current + 1) % len(self._songs)
        self._is_paused = False
        self.load_current()
        pygame.mixer.music.play()

    def previous(self):
        self._current = (self._current - 1) % len(self._songs)
        self._is_paused = False
        self.load_current()
        pygame.mixer.music.play()

    def load_current(self):
        song_path = os.path.join("music_player/music", self._songs[self._current])
        pygame.mixer.music.load(song_path)

    def get_current_song(self):
        return self._songs[self._current] if self._songs else "No songs found"

player = MusicPlayer()

buttons = [
    Button((50, 200, 100, 40), "Previous", player.previous),
    Button((170, 200, 100, 40), "Play/Pause", player.play),
    Button((290, 200, 100, 40), "Stop", player.stop),
    Button((410, 200, 100, 40), "Next", player.next),
]

running = True
while running:
    screen.fill((122, 197, 205))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == end_event:
            player.next()
        for button in buttons:
            button.handle_event(event)

    title_text = FONT.render("Music Player", True, BLACK)
    screen.blit(title_text, (w // 2 - title_text.get_width() // 2, 20))

    song_text = SMALL_FONT.render(f"Now playing: {player.get_current_song()}", True, BLACK)
    screen.blit(song_text, (w // 2 - song_text.get_width() // 2, 100))

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

