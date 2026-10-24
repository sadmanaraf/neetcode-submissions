class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def type_out(keys):
            screen = []                 # start with an empty screen
            for key in keys:            # press each key in order
                if key == "#":          # Backspace
                    if screen:          # only if there's something to delete
                        screen.pop()    # remove the last letter
                else:                   # a normal letter
                    screen.append(key)  # add it to the end
            return screen               # what's left on the screen

        return type_out(s) == type_out(t)