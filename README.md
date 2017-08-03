# dervish
Dervishes are scythe-wielding holy warriors who can attack multiple enemies at once. The Dervish has combat-related Enchantments, some inherent healing, and protection abilities. Their greatest power, however, is to evoke the power of the gods.
<h2>Basic Help</h2>
  <p>
    To advance through the game, <tt>left-click</tt> or press the <tt>space</tt> or <tt>enter</tt> keys. When at a menu,
    <tt>left-click</tt> to make a choice, or use the arrow keys to select a choice and <tt>enter</tt> to activate it.
  </p>

  <h3>Game Menu</h3>
  <p>
    When playing a game, <tt>right-click</tt> or press the <tt>escape</tt> key to enter the game menu. The game menu
    gives the following choices:
  </p>

  <dl>
    <dt>Return</dt>
    <dd>Returns to the game.</dd>
    <dt>Save Game</dt>
    <dd>Allows you to save a game by clicking on a save slot.</dd>
    <dt>Load Game</dt>
    <dd>Allows you to load a game by clicking on a save slot. Clicking on "Auto" accesses the automatic save slots.</dd>
    <dt>Preferences</dt>
    <dd>
      Changes the game preferences (options/configuration):
      <dl>
        <dt>Display</dt>
        <dd>Switches between fullscreen and windowed mode.</dd>
        <dt>Transitions</dt>
        <dd>Controls the display of transitions between game screens.</dd>
        <dt>Text Speed</dt>
        <dd>Controls the rate at which text displays. The further to the right this slider is, the faster the text
          will display. All the way to the right causes text to be shown instantly.</dd>
        <dt>Joystick</dt>
        <dd>Lets you control the game using a joystick.</dd>
        <dt>Skip</dt>
        <dd>Chooses between skipping messages that have been already seen (in any play through the game), and
          skipping all messages.</dd>
        <dt>Begin Skipping</dt>
        <dd>Returns to the game, while skipping.</dd>
        <dt>After Choices</dt>
        <dd>Controls if skipping stops upon reaching a menu.</dd>
        <dt>Auto-Forward Time</dt>
        <dd>Controls automatic advance. The further to the left this slider is, the shorter the amount of time
          before the game advances. All the way to the right means text will never auto-forward.</dd>
        <dt>Music, Sound, and Voice Volume</dt>
        <dd>Controls the volume of the Music, Sound effect, and Voice channels, respectively. The further to the
          right these are, the louder the volume.</dd>
      </dl>
    </dd>
    <dt>Main Menu</dt>
    <dd>Returns to the main menu, ending the current game.</dd>
    <dt>Help</dt>
    <dd>Shows this help screen.</dd>
    <dt>Quit</dt>
    <dd>Exits the game; the game will be closed and ended.</dd>
  </dl>

  <h3>Key and Mouse Bindings</h3>
  <dl>
    <dt>Left-click, Enter</dt>
    <dd>Advances through the game, activates menu choices, buttons, and sliders.</dd>
    <dt>Space</dt>
    <dd>Advances through the game, but does not activate choices.</dd>
    <dt>Arrow Keys</dt>
    <dd>Navigates between menu choices, buttons, and sliders.</dd>
    <dt>Ctrl</dt>
    <dd>Causes skipping to occur while the ctrl key is held down.</dd>
    <dt>Tab</dt>
    <dd>Toggles skipping, causing it to occur until tab is pressed again.</dd>
    <dt>Mousewheel-Up, PageUp</dt>
    <dd>Causes rollback to occur. Rollback reverses the game back in time, showing prior text and even allowing
      menu choices to be changed.</dd>
    <dt>Mousewheel-Down, PageDown</dt>
    <dd>Causes rollforward to occur, canceling out a previous rollback.</dd>
    <dt>Right-click, Escape</dt>
    <dd>Enters the game menu. When in the game menu, returns to the game.</dd>
    <dt>Middle-click, H</dt>
    <dd>Hides the text window and other transient displays.</dd>
    <dt>F</dt>
    <dd>Toggles fullscreen mode</dd>
    <dt>S</dt>
    <dd>Takes a screenshot, saving it in a file named screenshotxxxx.png, where xxxx is a serial number.</dd>
    <dt>Alt-M, Command-H</dt>
    <dd>Hides (iconifies) the window.</dd>
    <dt>Alt-F4, Command-Q</dt>
    <dd>Quits the game.</dd>
    <dt>Delete</dt>
    <dd>When a save slot is selected, deletes that save slot.</dd>
    <dt>v</dt>
    <dd>
      Toggles self-voicing mode, which reads text to the user using an os-supplied speech synthesizer. For more
      information, please read the <a href="http://www.renpy.org/doc/html/self_voicing.html">self-voicing</a>
      documentation.
    </dd>
    <dt>Shift+C</dt>
    <dd>Toggles clipboard-voicing mode, which copies text to the clipboard so it can be read by a screen reader.</dd>
  </dl>

  <h3>Controller Support and Bindings</h3>

  <p>
    This game should automatically detect and use game controllers supported by
    SDL2. Other controllers can be configured using third-party configuration tools
    like the <a href="http://www.generalarcade.com/gamepadtool/">SDL2 Gampad Tool</a>
  </p>

  <p>
    A small number of systems may have problems using detected game controllers. Should
    that happen, hold down shift as the game starts, and disable the controller support.
  </p>

  <p>The following bindings are used:</p>

  <dl>
    <dt>Right Trigger, A (Bottom Button)</dt>
    <dd>Advances through the game, activates menu choices, buttons, and sliders.</dd>

    <dt>Guide, Start</dt>
    <dd>Enters the game menu. When in the game menu, returns to the game.</dd>

    <dt>Directional Pad, Analog Sticks</dt>
    <dd>Navigates between menu choices, buttons, and sliders.</dd>

    <dt>Left Trigger, Left Shoulder, Back</dt>
    <dd>Causes rollback to occur. Rollback reverses the game back in time, showing prior text and even allowing
      menu choices to be changed.</dd>

    <dt>Right Shoulder</dt>
    <dd>Causes rollforward to occur, canceling out a previous rollback.</dd>

    <dt>Y (Top Button)</dt>
    <dd>Hides the text window and other transient displays.</dd>

  </dl>

  <h2>Legal Notice</h2>
  <p>
    This program contains free software licensed.
  </p>
Copyright (c) 2017 Munis Isazade

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

