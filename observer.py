
class DataSource(object):

    def __init__(self, data):
        self.data = data 
        self.observers = []

    def change_data(self, data):
        self.data = data
        for observer in self.observers:
            observer.render(self)

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

class Observer(object):

    def render(object):
        raise NotImplementedError()

class PieChart(Observer):

    def render(self, data_source):
        print('rendering piechart with data {}'.format(data_source.data))

class BarChart(Observer):
  
    def render(self, data_source):
        print('rendering barchart with data {}'.format(data_source.data))


if __name__ == '__main__':
    data_source = DataSource(data=[])
    pie_chart_observer = PieChart()
    bar_chart_observer = BarChart()
    data_source.attach(pie_chart_observer)
    data_source.attach(bar_chart_observer)
    data_source.change_data(data=[1,2,3])
    data_source.change_data(data=[4,5,6])

    data_source.detach(pie_chart_observer)
    data_source.change_data(data=[7,8,9])
