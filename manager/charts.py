from collections import Counter
import random
from django.contrib.auth.models import User
from jchart import Chart
from jchart.config import DataSet

from .models import ModelTrain, Collection

class ManufacturerChart(Chart):
    chart_type = 'pie'

    responsive = False

    def set_owner(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

        self.manufacturer_list = self.models.values_list('manufacturer', flat=True)[::1]

    def get_labels(self, *args, **kwargs):
        # Convert the query set to a list
        return self.manufacturer_list

    def get_datasets(self, *args, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: random_colour(), data))

        # Convert the query set to a list
        return [DataSet(data=data, backgroundColor=colours)]

    def generate_data(self):
        return calculate_percentage(self.manufacturer_list)

class TractionChart(Chart):
    chart_type = 'pie'

    responsive = False

    def set_owner(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

        self.traction_list = self.models.values_list('traction', flat=True)[::1]

    def get_labels(self, *args, **kwargs):
        # Get the tuple, remove duplicates and convert to list
        return list(set(sum(ModelTrain.TRACTION_TYPES, ())))

    def get_datasets(self, *args, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: random_colour(), data))

        # Convert the query set to a list
        return [DataSet(data=data, backgroundColor=colours)]

    def generate_data(self):
        return calculate_percentage(self.traction_list)

class ScaleChart(Chart):
    chart_type = 'pie'

    responsive = False

    def set_owner(self, owner):
        self.models = ModelTrain.objects.filter(owner=owner)

    def get_labels(self, *args, **kwargs):
        # Get the tuple, remove duplicates and convert to list
        return list(set(sum(ModelTrain.SCALES, ())))

    def get_datasets(self, *args, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: random_colour(), data))

        # Convert the query set to a list
        return [DataSet(data=data, backgroundColor=colours)]

    def generate_data(self):
        list_of_scales = self.models.values_list('scale', flat=True)[::1]

        return calculate_percentage(list_of_scales)

class CollectionChart(Chart):
    chart_type = 'bar'

    def set_owner(self, owner):
        self.collections = Collection.objects.filter(owner=owner)

        self.collections_list = self.collections.values_list('name', flat=True)[::1]

    def get_labels(self, *args, **kwargs):
        return self.collections_list

    def get_datasets(self, **kwargs):
        data = self.generate_data()

        colours = list(map(lambda col: random_colour(), data))

        # Convert the query set to a list
        return [DataSet(label='Number of Models Per Collection', data=data, backgroundColor=colours)]

    def generate_data(self):
        return list(map(lambda collec: collec.trains.count(), self.collections))

def calculate_percentage(items):
    counted = Counter(items)

    counted_values = counted.values()

    sum_of_counted = sum(counted_values) 

    return list(map(lambda value: value * 100.0 / sum_of_counted, counted_values))


def random_colour():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))