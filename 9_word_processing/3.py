class paragraph:
    def __init__(self, width = 100):
        self.width = width

    def headline(self, _text = ''):
        if (_text != ''):
            return(_text.center(self.width))
        else:
            return 'Given empty headline.'

    def formatting(self, _text = ''):
        if (_text != ''):
            _returned = ''
            _firstLine = True
            for line in _text.split('\n'):
                if (_firstLine):
                    _returned = '    ' + line.capitalize() + '\n'
                    _firstLine = False
                else:
                    _returned += line.capitalize() + '\n'
            return _returned
        else:
            return 'Given empty paragraph.'