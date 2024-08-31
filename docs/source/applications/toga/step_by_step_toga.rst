##################
Toga: step by step
##################

Step 1
======

.. code-block:: python
   :caption: Простое окно с заголовком

    class TogaApp(toga.App):
        """Simple Toga application."""

        def startup(self) -> None:
            """Construct and show the Toga application."""

            main_box = toga.Box()

            self.main_window = toga.MainWindow(title='Название приложения')
            self.main_window.content = main_box
            self.main_window.show()

    def main() -> toga.App:
        """Return Toga app."""
        return TogaApp()

Step 2
======

.. code-block:: python
   :caption: Два простых окна с переключением драг на друга

   class TogaApp(toga.App):
       """Simple Toga application."""

       main_box: toga.Box
       word_list_box: toga.Box

       def startup(self) -> None:
           """Construct and show the Toga application."""

           btn_switch_main_window = toga.Button(
               text='Главное окно',
               on_press=self.switch_main_window,
           )

           btn_switch_word_list_window = toga.Button(
               text='Англо-Русский словарь',
               on_press=self.switch_word_list_window,
           )

           self.main_box = toga.Box(children=[btn_switch_word_list_window])

           self.word_list_box = toga.Box()
           self.word_list_box.add(btn_switch_main_window)

           self.main_window = toga.MainWindow(title='Название приложения')
           self.main_window.content = self.main_box
           self.main_window.show()

       def switch_main_window(self, widget: Widget) -> None:
           """Switch to main window."""
           self.main_window.content = self.main_box


       def switch_word_list_window(self, widget: Widget) -> None:
           """Switch to word list window."""
           self.main_window.content = self.word_list_box

   def main() -> toga.App:
       """Return Toga app."""
       return TogaApp()

Step 3
======

.. code-block:: python
   :caption: Разбить класс на несколько

   class BaseWindow(toga.App):
       """Base window representation with MainWindow class.

       Inherit this class to create the new window representations.
       """

       main_box = toga.Box()

       def startup(self) -> None:
           """Construct and show the base main window."""
           self.main_window = toga.MainWindow(title='Название приложения')
           self.main_window.content = self.main_box
           self.main_window.show()

       def switch_main_window(self, widget: Widget) -> None:
           """Switch to main window."""
           self.main_window.content = self.main_box

       @property
       def btn_switch_main_window(self) -> toga.Button:
           """Button to switch to the main window."""
           return toga.Button(
               text='Главное окно',
               on_press=self.switch_main_window,
           )


   class WordListWindow(BaseWindow):
       """Word list window representation."""

       word_list_box = toga.Box()

       def startup(self) -> None:
           """Construct the word list window."""
           # Main window contain a switch button to this window.
           self.main_box.add(self.btn_switch_word_list_window)
           # This window contain a switch button to Main window.
           self.word_list_box.add(self.btn_switch_main_window)

           super().startup()

       def switch_word_list_window(self, widget: Widget) -> None:
           """Switch to word list window."""
           self.main_window.content = self.word_list_box

       @property
       def btn_switch_word_list_window(self) -> toga.Button:
           """Button to switch to the word list window."""
           return toga.Button(
               text='Англо-Русский словарь',
               on_press=self.switch_word_list_window,
           )


   class TogaApp(
       WordListWindow,
   ):
       """Simple Toga application."""


   def main() -> toga.App:
       """Return Toga app."""
       return TogaApp()
