import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from time_service import TimeService

style.use('ggplot')


class GraphingService:
    def get_graph_dataframe(self, data_dict):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        sorted_dataframe = pd.DataFrame.from_dict(data_dict, orient='index', columns=['sentiment']).sort_index()
        return sorted_dataframe

    def plot_graph(self, data_dict, username):
        graph_df = self.get_graph_dataframe(data_dict)
        print(graph_df)
        y_values = graph_df['sentiment'].values
        x_values = []
        for index in graph_df.index:
            x_values.append(TimeService().get_string_from_timestamp(index))

        print(x_values)
        print(y_values)

        plt.plot(x_values, y_values, 'c')

        plt.title(f'Sentiment of @{username} based on recent tweets')
        plt.xlabel('Days')
        plt.ylabel('Sentiment')
        # plt.legend()

        plt.grid(True, color='k')

        plt.show()
