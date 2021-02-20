from data_retrieval import retrieve_df_list
from simulation_filter import sep_by_sim
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df_list = retrieve_df_list(file="default")
    processed_df_list = list()

    for df in df_list:
        processed_df_list.append(sep_by_sim(df))

    # Sheet 0, Simulation 0
    sheet_id = 0
    simulation_id = 0

    hist = processed_df_list[sheet_id][simulation_id].hist(column='Turn Taking', \
                                            bins=int(processed_df_list[sheet_id][simulation_id]['Turn Taking'].max()))
    plt.ylabel("Frequency")
    plt.xlabel("Person ID")

    plt.show()
    print("f")


