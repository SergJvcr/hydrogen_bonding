import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# DATA LOADING
df = pd.read_csv('hydrogen_bonding\\data_for_hydrogen_bonding.csv')
# df.insert(0, 'index', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], True) # add column for index

# DATA ANALYSIS
print(df.head(3))
print(df.info())
print(df.describe(include='all'))
print(df['compound'])

# CREATING A PLOT FOR HYDROGEN COMPOUNDS OF 14TH GROUP OF ELEMENTS
# get only compounds with elem from the 14th group
df_four_group = df.mask(df['group_of_element'] > 14)
print(df_four_group)
# sns.set_theme(style="whitegrid") - optional, if you need a special style
plt.figure(figsize=(7, 5)) # set the size for the plot
fig = sns.lineplot(
                   x=df_four_group['compound'], 
                   y=df_four_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='#66ccee'
                   )
fig.spines[['right', 'top']].set_visible(False) # avoid unnecessary boundaries on the plot

# label points on the plot only if they are higher than the mean
# for x, y in zip(df_four_group['index'], df_four_group['boiling_temperature_celsious']):
#     plt.text(x = x, # x-coordinate position of data label
#     y = y+2, # y-coordinate position of data label, adjusted to be 2 above the data point
#     s = x, # data label
#     color = 'black') # set colour of line

# Loop for annotation of all points 
name_for_four_group = df_four_group['compound']

for i in range(len(df_four_group)): 
    plt.annotate(name_for_four_group[i], 
                 (df_four_group['compound'][i], 
                  df_four_group['boiling_temperature_celsious'][i] + 15)) 

# set apropriate labels and plot decorating
plt.title('Boiling points for Hydrogen compounds\n of Chemical elements of the 14th (4th) group', 
          loc='center', 
          fontdict = {'fontsize' : 14, 'fontweight': 'bold'})
plt.xlabel('Hydrogen compounds of chemical elements of the 14th group', loc='center')
plt.xticks([])
plt.ylabel('Temperature, C', loc='center')
plt.yticks(np.arange(-200, 130, step=40))
plt.show()

# CREATING 4 SUBPLOTS FOR HYDROGEN COMPOUNDS OF 14TH-17TH GROUPS OF ELEMENTS
fig, axes = plt.subplots(2, 2, layout=None, figsize=(14,7))
fig.suptitle('Boiling points for Hydrogen compounds of Chemical elements of the 14-17th groups',
             fontsize=14, fontweight='bold')

# 1st plot
df_four_group = df.mask(df['group_of_element'] > 14) # to get only elem from that group
gr1 = sns.lineplot(
                   x=df_four_group['compound'], 
                   y=df_four_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='#66ccee', ax=axes[0,0]
                   )
# Loop for annotation of all points 
name_for_four_group = df_four_group['compound']
for i in range(len(df_four_group)): 
    gr1.annotate(name_for_four_group[i], 
                 (df_four_group['compound'][i], 
                  df_four_group['boiling_temperature_celsious'][i] + 15))

# 2nd plot
df_five_group = df.mask((df['group_of_element'] > 15) | (df['group_of_element'] < 15))
gr2 = sns.lineplot(
                   x=df_five_group['compound'], 
                   y=df_five_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='#ffb000', ax=axes[0,1]
                   )
name_for_five_group = df_five_group['compound']
for i in range(len(name_for_five_group)): 
    gr2.annotate(name_for_five_group[i], 
                 (df_five_group['compound'][i], 
                  df_five_group['boiling_temperature_celsious'][i] + 15)) 

# 3rd plot
df_six_group = df.mask((df['group_of_element'] > 16) | (df['group_of_element'] < 16))
gr3 = sns.lineplot(
                   x=df_six_group['compound'], 
                   y=df_six_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='#dc267f', ax=axes[1,0]
                   )
name_for_seven_group = df_six_group['compound']
for i in range(len(df_six_group)): 
    gr3.annotate(name_for_seven_group[i], 
                 (df_six_group['compound'][i], 
                  df_six_group['boiling_temperature_celsious'][i] + 15))

# 4th plot
df_seven_group = df.mask(df['group_of_element'] < 17)
gr4 = sns.lineplot(
                   x=df_seven_group['compound'], 
                   y=df_seven_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='#228833', ax=axes[1,1]
                   ) 
name_for_seven_group = df_seven_group['compound']
for i in range(len(df_seven_group)): 
    gr4.annotate(name_for_seven_group[i], 
                 (df_seven_group['compound'][i], 
                  df_seven_group['boiling_temperature_celsious'][i] + 15))

# give the graphs good description
gr1.spines[['right', 'top']].set_visible(False)
# gr1.set_title('The boiling point for hydrogen compounds of the 14th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr1.set_xlabel('Hydrogen compounds of chemical elements of the 14th group')
gr1.set_xticks([])
gr1.set_ylabel('Temperature, C')
gr1.set_yticks(np.arange(-200, 130, step=40))

gr2.spines[['right', 'top']].set_visible(False)
# gr2.set_title('The boiling point for hydrogen compounds of the 15th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr2.set_xlabel('Hydrogen compounds of chemical elements of the 15th group')
gr2.set_xticks([])
gr2.set_ylabel('Temperature, C')
gr2.set_yticks(np.arange(-200, 130, step=40))

gr3.spines[['right', 'top']].set_visible(False)
# gr3.set_title('The boiling point for hydrogen compounds of the 16th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr3.set_xlabel('Hydrogen compounds of chemical elements of the 16th group')
gr3.set_xticks([])
gr3.set_ylabel('Temperature, C')
gr3.set_yticks(np.arange(-200, 130, step=40))

gr4.spines[['right', 'top']].set_visible(False)
# gr4.set_title('The boiling point for hydrogen compounds of the 17th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr4.set_xlabel('Hydrogen compounds of chemical elements of the 17th group')
gr4.set_xticks([])
gr4.set_ylabel('Temperature, C')
gr4.set_yticks(np.arange(-200, 130, step=40))
plt.show()

# CREATING THE COMMON PLOT FOR HYDROGEN COMPOUNDS OF 14TH-17TH GROUPS OF ELEMENTS
df.insert(3, 'period', [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4], True) # add column for period

plt.figure(figsize=(10, 5))

common_graph = sns.lineplot(data=df, x='period', y='boiling_temperature_celsious', 
                            hue='group_of_element',
                            linewidth=1.5, marker='o',
                            legend='auto', palette=['#66ccee', '#ffb000', '#dc267f', '#228833'])
common_graph.spines[['right', 'top']].set_visible(False)

plt.title('Boiling points for Hydrogen compounds \n of Chemical elements of the 14-17th groups', 
          loc='center', 
          fontdict = {'fontsize' : 14, 'fontweight': 'bold'})
# plt.legend(title='Groups of \n elements',
#            bbox_to_anchor=(1, 1), 
#            loc='upper left', 
#            borderaxespad=0)
plt.legend(title='Groups of \n elements',
           loc='lower right')
plt.xlabel('Hydrogen compounds of chemical elements of the 14-17th groups')
plt.xticks([])
plt.ylabel('Temperature, C')
plt.yticks(np.arange(-200, 130, step=40))

# Annotation for every dot on the plot 
# for i in range(len(df)): # - IT WORKS, but looks not too clear
#     common_graph.annotate(text=df['compound'][i], xy=(df['period'][i], df['boiling_temperature_celsious'][i]))

# Annotation for those dots that "broke the picture" 
plt.annotate('HF', xy =(0, 24))
plt.annotate('H2O', xy =(0, 104))
plt.annotate('NH3', xy =(0, -29))
plt.show()

# CREATING 4 SUBPLOTS FOR HYDROGEN COMPOUNDS 
# OF 14TH-17TH GROUPS OF ELEMENTS WITH DIFFERENT STYLE
fig, axes = plt.subplots(2, 2, layout=None, figsize=(14,7))
fig.suptitle('Boiling points for Hydrogen compounds of Chemical elements of the 14-17th groups',
             fontsize=14, fontweight='bold')

# 1st plot
df_four_group = df.mask(df['group_of_element'] > 14)
gr1 = sns.lineplot(
                   x=df_four_group['compound'], 
                   y=df_four_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='black', ax=axes[0,0]
                   )
# Loop for annotation of all points 
name_for_four_group = df_four_group['compound']
for i in range(len(df_four_group)): 
    gr1.annotate(name_for_four_group[i], 
                 (df_four_group['compound'][i], 
                  df_four_group['boiling_temperature_celsious'][i] + 15))
gr1.grid(linestyle='--', alpha=0.5)

# 2nd plot
df_five_group = df.mask((df['group_of_element'] > 15) | (df['group_of_element'] < 15))
gr2 = sns.lineplot(
                   x=df_five_group['compound'], 
                   y=df_five_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='black', ax=axes[0,1]
                   )
name_for_five_group = df_five_group['compound']
for i in range(len(name_for_five_group)): 
    gr2.annotate(name_for_five_group[i], 
                 (df_five_group['compound'][i], 
                  df_five_group['boiling_temperature_celsious'][i] + 17)) 
gr2.grid(linestyle='--', alpha=0.5)
gr2.plot(0, -33, 'o', lw=1, color='red')

# 3rd plot
df_six_group = df.mask((df['group_of_element'] > 16) | (df['group_of_element'] < 16))
gr3 = sns.lineplot(
                   x=df_six_group['compound'], 
                   y=df_six_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='black', ax=axes[1,0]
                   )
name_for_seven_group = df_six_group['compound']
for i in range(len(df_six_group)): 
    gr3.annotate(name_for_seven_group[i], 
                 (df_six_group['compound'][i], 
                  df_six_group['boiling_temperature_celsious'][i] + 15))
gr3.grid(linestyle='--', alpha=0.5)
gr3.plot(0, 100, 'o', lw=1, color='red')

# 4th plot
df_seven_group = df.mask(df['group_of_element'] < 17)
gr4 = sns.lineplot(
                   x=df_seven_group['compound'], 
                   y=df_seven_group['boiling_temperature_celsious'], 
                   linewidth=1.5, marker='o', color='black', ax=axes[1,1]
                   ) 
name_for_seven_group = df_seven_group['compound']
for i in range(len(df_seven_group)): 
    gr4.annotate(name_for_seven_group[i], 
                 (df_seven_group['compound'][i], 
                  df_seven_group['boiling_temperature_celsious'][i] + 15))
gr4.grid(linestyle='--', alpha=0.5)
gr4.plot(0, 20, 'o', lw=1, color='red')

# give the graphs good description
gr1.spines[['right', 'top']].set_visible(False)
# gr1.set_title('The boiling point for hydrogen compounds of the 14th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr1.set_xlabel('HYDROGEN COMPOUNDS OF CHEMICAL ELEMENTS OF THE 14th GROUP', loc='left', color='gray')
gr1.set_xticks([])
gr1.tick_params(axis='both', labelcolor='gray')
gr1.set_ylabel('TEMPERATURE, C', loc='top', color='gray')
gr1.set_yticks(np.arange(-200, 130, step=40))

gr2.spines[['right', 'top']].set_visible(False)
# gr2.set_title('The boiling point for hydrogen compounds of the 15th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr2.set_xlabel('HYDROGEN COMPOUNDS OF CHEMICAL ELEMENTS OF THE 15th GROUP', loc='left', color='gray')
gr2.set_xticks([])
gr2.tick_params(axis='both', labelcolor='gray')
gr2.set_ylabel('TEMPERATURE, C', loc='top', color='gray')
gr2.set_yticks(np.arange(-200, 130, step=40))

gr3.spines[['right', 'top']].set_visible(False)
# gr3.set_title('The boiling point for hydrogen compounds of the 16th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr3.set_xlabel('HYDROGEN COMPOUNDS OF CHEMICAL ELEMENTS OF THE 16th GROUP', loc='left', color='gray')
gr3.set_xticks([])
gr3.tick_params(axis='both', labelcolor='gray')
gr3.set_ylabel('TEMPERATURE, C', loc='top', color='gray')
gr3.set_yticks(np.arange(-200, 130, step=40))

gr4.spines[['right', 'top']].set_visible(False)
gr4.spines[['left', 'bottom']].set_color('gray')
# gr4.set_title('The boiling point for hydrogen compounds of the 17th group', 
#           loc='center', 
#           fontdict = {'fontsize' : 10})
gr4.set_xlabel('HYDROGEN COMPOUNDS OF CHEMICAL ELEMENTS OF THE 17th GROUP', loc='left', color='gray')
gr4.set_xticks([])
gr4.tick_params(axis='both', labelcolor='gray')
gr4.set_ylabel('TEMPERATURE, C', loc='top', color='gray')
gr4.set_yticks(np.arange(-200, 130, step=40))
plt.show()