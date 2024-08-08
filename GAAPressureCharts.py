import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset from Excel
df = pd.read_excel('/content/Football_Championship_2023_Shots_With_Expected_Points_JSON.xlsx')

# Filtering the data for only Galway
galway_data = df[df['Opposition'] == 'Galway']  # Assuming 'Team' is the column name


# Function to draw a GAA pitch on an existing axis
def draw_gaa_pitch(ax, line="black", pitch="#bada55", orientation="horizontal"):

        # side and goal lines #
        ly1 = [0,0,88,88,0]
        lx1 = [0,145,145,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)

            #goals#
        ly4 = [40.75,40.75,47.25,47.25]
        lx4 = [145,145.2,145.2,145]
        plt.plot(lx4,ly4,color=line,zorder=5)

        ly5 = [40.75,40.75,47.25,47.25]
        lx5 = [0,-0.2,-0.2,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        ly6 = [37,37,51,51]
        lx6 = [145,140.5,140.5,145]
        plt.plot(lx6,ly6,color=line,zorder=5)

        ly7 = [37,37,51,51]
        lx7 = [0,4.5,4.5,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #large rectangle
        ly88 = [34.5,34.5,53.5,53.5]
        lx88 = [145,131,131,145]
        plt.plot(lx88,ly88,color=line,zorder=5)

        ly87 = [34.5,34.5,53.5,53.5]
        lx87 = [0,14,14,0]
        plt.plot(lx87,ly87,color=line,zorder=5)


        #halfway small line
        ly97 = [39,49]
        lx97 = [72.5,72.5]
        plt.plot(lx97,ly97,color=line,zorder=5)

        #peno lines
        ly90 = [43.5,44.5]
        lx90 = [11,11]
        plt.plot(lx90,ly90,color=line,zorder=5)

        ly89 = [43.5,44.5]
        lx89 = [136,136]
        plt.plot(lx89,ly89,color=line,zorder=5)

        circle1 = plt.Circle((124,44), 13,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((21,44), 13,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((52, 34), 9.15,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)


        #14 yard line across the pitch
        ly94 = [0,88]
        lx94 = [14,14]
        plt.plot(lx94,ly94,color=line,zorder=5)

        ly99 = [0,88]
        lx99 = [131,131]
        plt.plot(lx99,ly99,color=line,zorder=5)

    #21 yard line
        ly98 = [0,88]
        lx98 = [124,124]
        plt.plot(lx98,ly98,color=line,zorder=5)

        ly93 = [0,88]
        lx93 = [21,21]
        plt.plot(lx93,ly93,color=line,zorder=5)

    #45 metre line
        ly96 = [0,88]
        lx96 = [100,100]
        plt.plot(lx96,ly96,color=line,zorder=5)

        ly91 = [0,88]
        lx91 = [45,45]
        plt.plot(lx91,ly91,color=line,zorder=5)

     #65 yard line
        ly95 = [0,88]
        lx95 = [80,80]
        plt.plot(lx95,ly95,color=line,zorder=5)

        ly92 = [0,88]
        lx92 = [65,65]
        plt.plot(lx92,ly92,color=line,zorder=5)

        ## Rectangles in boxes
        rec1 = plt.Rectangle((124,30), 124,30,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((0, 30), 21,30,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 147,90,ls='-',color=pitch, zorder=1,alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
       # ax.add_artist(circle3)

# Iterate over each unique team in the dataset
for team in df['Opposition'].unique():
    # Filter data for the current team
    team_data = df[df['Opposition'] == team]

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(7.25, 8.8))
    draw_gaa_pitch(ax)  # Draw the pitch

    # Set the heatmap parameters using the filtered team data
    # Adjust the range to take the other half of the pitch
    hist, xedges, yedges = np.histogram2d(
        team_data['stand_x'], team_data['stand_y'],
        bins=(4, 3),
        range=[[72.5, 145], [0, 88]]  # This now considers the right half of the pitch
    )

    # Normalize the histogram
    max_hist = np.max(hist)
    hist_norm = hist / max_hist if max_hist > 0 else hist

    # Adjust the colormap to a green gradient
    cmap = plt.cm.Greens

    # Plotting the heatmap on the right half of the pitch
    heatmap = ax.imshow(hist_norm.T, cmap=cmap, aspect='auto', origin='lower',
                        extent=[72.5, 145, 0, 88], zorder=2)  # Extent matches the range

    # Add color bar
    cbar = plt.colorbar(heatmap, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
    cbar.set_label('Pressure Intensity')

    # Customizing the color bar labels
    tick_values = [0, 0.25, 0.5, 0.75, 1]  # Positions for your custom labels
    tick_labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
    cbar.set_ticks(tick_values)
    cbar.set_ticklabels(tick_labels)

    # Remove the tick marks
    ax.set_xticks([])  # Remove x-axis tick marks
    ax.set_yticks([])  # Remove y-axis tick marks

    # Add titles and labels
    # ax.set_title(f'2D Pressure Map for {team}')
    # ax.set_xlabel('Pitch Length (m)')
    # ax.set_ylabel('Pitch Width (m)')

    plt.tight_layout()

    # Save the figure with the team name in the filename
    filename = f'{team}_Pressure_Map.png'
    plt.savefig(filename)
    plt.close(fig)  # Close the figure to free memory