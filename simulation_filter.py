def sep_by_sim(df):
    # each scenario contains multiple simulations
    # search sheet for row # seperating individual simulations
    # return nested dictionary object: {scenario_id : {'simid' : 'val'}}
    # Input: Dataframe with multiple simulation values
    # Output: Dictionary object that seperates each dataframe into smaller dataframes that describe individual
    # simulations within the scenario
    sim_dict = dict()
    # print(df_with_multiple_simulations)
    prev_sim_id = None
    j = 0
    for i, sim_id in enumerate(df['Simulation']):
        if i == 0:
            prev_sim_id = sim_id
        if sim_id != prev_sim_id:
            sim_dict[int(prev_sim_id)] = df[j:i]
            prev_sim_id = sim_id
            j = i
        elif i == df['Simulation'].__len__() - 1: # end of list
            sim_dict[int(prev_sim_id)] = df[j:]

    return sim_dict