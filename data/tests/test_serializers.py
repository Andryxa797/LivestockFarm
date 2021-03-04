from django.test import TestCase, Client
from rest_framework.authtoken.admin import User

from data.models import DataBeforeProcess
from data.serializers import DataBeforeProcessSerializer

# class DataBeforeProcessSerializersTestCase(TestCase):
#     def test_ok(self):
#         self.user = User.objects.create(username="Andrey", password="2222")
#         self.user.save()
#        data_1 = DataBeforeProcess.objects.create(BatteryStation='3.30', NewPost=True, user=User.objects.all().first())
#        data_2 = DataBeforeProcess.objects.create(BatteryStation='3.40', NewPost=True, user=User.objects.all().first())
#         data_time_1 = DataBeforeProcess.objects.get(pk=1).DataTimeCreate
#         data_time_2 = DataBeforeProcess.objects.get(pk=2).DataTimeCreate
#         serializers_data = DataBeforeProcessSerializer([data_1, data_2], many=True).data
#         exception_data = [{
#             "Cepstral": "",
#             "BatteryStation": "3.30",
#             "NewPost": True,
#             'DataTimeCreate': data_time_1,
#         },
#             {
#                 "Cepstral": "",
#                 "BatteryStation": "3.40",
#                 "NewPost": True,
#                 'DataTimeCreate': data_time_2,
#                 "user": User.objects.all().first()
#             }]
#         print(serializers_data)
#         print(exception_data)
#         self.assertEqual(serializers_data, exception_data)
