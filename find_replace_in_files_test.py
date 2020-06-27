import unittest
from find_replace_in_files import filetype_matches, make_replacements

# test find file type
# should be able to specify a filetype and only make find/replacements in that type
class MyTestCase(unittest.TestCase):
    def test_filetype_matches(self):
        file = r"C:\Users\Chris\Desktop\Python Scripts\find_replace_in_files\test files\TV.Cooney.01.html"
        self.assertEqual(filetype_matches(file, ".html"), True)

    def test_filetype_matches(self):
        file = r"C:\Users\Chris\Desktop\Python Scripts\find_replace_in_files\test files\New Picture.BMP"
        self.assertEqual(filetype_matches(file, ".html"), False)

# test replacement in file type
# should be able to make the replacement and output a report of the file, location, where the replacement was made
    def test_make_replacements(self):
        file = r"C:\Users\Chris\Desktop\Python Scripts\find_replace_in_files\test files\TV.Cooney.01.html"
        replacements = {'http://vjs.zencdn.net/ie8/1.1.0/videojs-ie8.min.js':
                            'https://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js',
                        'http://vjs.zencdn.net/5.0.2/video.js': 'https://vjs.zencdn.net/7.8.2/video.js'}
        self.assertEqual(make_replacements(file, replacements), True)

if __name__ == '__main__':
    unittest.main()
