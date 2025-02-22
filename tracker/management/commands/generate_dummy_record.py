import random

from django.core.management.base import BaseCommand

from tracker.models import Tag, User, Record
from faker import Faker



class Command(BaseCommand):
    help = "Generate fake transaction record for testing purpose."

    def handle(self, *args, **options):

        Faker.seed("rethr us ")
        fake = Faker()

        
        tags = [ "Hunter", "Entertainment", "Learning", "Fording", "Hunting", "Life", "Bills", "Utilities", "Misc" ]

        for tag in tags:
            Tag.objects.get_or_create(name=tag)
        print("Tag is created...")

        user = User.objects.filter(username="raven").first()
        
        if user is None:
            user = User.objects.create_superuser(username="raven", password="test")

        tags = Tag.objects.all()
        

        user_id = user

        for _ in range(20):
            record = Record.objects.create(
                user=user_id,
                comment=fake.sentence(200),
                amount=random.uniform(1, 25000),
                date=fake.date_between(start_date="-1y"),
                transaction_type=random.choice(Record.TRANSACTION_TYPE_CHOICES)[0],
            )
            record.save()
            
            for tag in (random.choices(k=random.randint(1, len(tags) - 3), population=tags)):
                print(record.id, tag)
                record.tags.add(tag)








