from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.core.audio import SoundLoader

class ScaleChordApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Dropdown for choosing chord/scale
        self.spinner = Spinner(
            text='Select Scale or Chord',
            values=('C Major', 'A Minor', 'G Major'),  # Add more scales/chords
            size_hint=(1, 0.1)
        )
        self.spinner.bind(text=self.on_spinner_select)
        self.add_widget(self.spinner)

        # Image area for chord/scale diagram
        self.image = Image(source='assets/images/placeholder.png')  # Placeholder image
        self.add_widget(self.image)

        # Play button
        self.play_button = Button(text='Play Sound', size_hint=(1, 0.1))
        self.play_button.bind(on_press=self.play_sound)
        self.add_widget(self.play_button)

        self.sound = None

    def on_spinner_select(self, spinner, text):
        # Update image and sound based on selection
        self.image.source = f'assets/images/{text.lower().replace(" ", "_")}.png'
        self.sound = SoundLoader.load(f'assets/audio/{text.lower().replace(" ", "_")}.wav')

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()

class GuitarImproveApp(App):
    def build(self):
        return ScaleChordApp()

if __name__ == '__main__':
    GuitarImproveApp().run()
