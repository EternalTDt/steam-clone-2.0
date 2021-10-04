from django.test import TestCase
from mainpage.models import Product, Company, Category
from users.models import Profile
from django.utils import timezone
from django.urls import reverse

# models test
class ProductTest(TestCase):

    def create_product(self, name="only a test", slug="only-a-test", price=59.99, description="yes, this is only a test"):
        return Product.objects.create(name=name, slug=slug, price=price, description=description, release_date=timezone.now())

    def test_product_creation(self):
        w = self.create_product()
        self.assertTrue(isinstance(w, Product))
        self.assertEqual(w.name, "only a test")


class CompanyTest(TestCase):

    def create_company(
        self, 
        name="Ubisoft", 
        year_of_foundation=1996, 
        slug="only-a-test", 
        ceo="Ahikimi Neoyaro", 
        foundation_country="Belarus",
        employees_num=10300):

        return Company.objects.create(
            name=name, 
            year_of_foundation=year_of_foundation, 
            slug=slug, 
            ceo=ceo, 
            foundation_country=foundation_country, 
            employees_num=employees_num)

    def test_company_creation(self):
        w = self.create_company()
        self.assertTrue(isinstance(w, Company))
        self.assertEqual(w.name, "Ubisoft")


class CategoryTest(TestCase):

    def create_category(
        self, 
        name="Adventure",
        slug="only-a-test"):

        return Category.objects.create(
            name=name,
            slug=slug)

    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.name, "Adventure")


class ProfileTest(TestCase):

    def create_profile(
        self, 
        phone="test",
        address="test",
        city="test"):

        return Profile.objects.create(
            phone=phone,
            address=address,
            city=city)

    def test_profile_creation(self):
        w = self.create_profile()
        self.assertTrue(isinstance(w, Profile))
        self.assertEqual(w.phone, "test")