import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


class GraphingService:

    def plot_graph(self, data_dict, twitter_user):
        x_values = data_dict.keys()
        y_values = data_dict.values()

        plt.plot(x_values, y_values, 'c')

        plt.title(f'Mood of @{twitter_user}')
        plt.xlabel('Days')
        plt.ylabel('Sentiment')
        # plt.legend()

        plt.grid(True, color='k')

        plt.show()
