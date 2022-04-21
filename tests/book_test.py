import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("Mort", 1987, "Terry Pratchett")
    
    
    def test_book_has_title(self):
        self.assertEqual("Mort", self.book.title)
        
        
    def test_book_has_year_of_release(self):
        self.assertEqual(1987, self.book.release_year)
       
        
    def test_book_has_author(self):
        self.assertEqual("Terry Pratchett", self.book.author)
    
    
   
    
    
   