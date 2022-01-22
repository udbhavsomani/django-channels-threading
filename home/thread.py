import json
import random
import threading
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Student

from faker import Faker
fake = Faker()


class CreateStudentData(threading.Thread):

    def __init__(self, count):
        self.count = count
        threading.Thread.__init__(self)

    def run(self):
        try:
            print("Executing Thread")
            channel_layer = get_channel_layer()
            for i in range(self.count):
                # print(i)
                obj = Student.objects.create(
                    name=fake.name(),
                    email=fake.email(),
                    address=fake.address(),
                    age=random.randint(10, 30)
                )
                data = {
                    'current_total': i+1,
                    'total': self.count,
                    'name': obj.name,
                    'email': obj.email,
                    'address': obj.address,
                    'age': obj.age
                }
                # print(data)
                async_to_sync(channel_layer.group_send)(
                    'data_consumer_group',
                    {
                        'type': 'send_data',
                        'student_data': json.dumps(data)
                    }
                )

        except Exception as e:
            print(e)
