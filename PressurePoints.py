import pandas as pd
import matplotlib.pyplot as plt

# Load data from an Excel file
df = pd.read_excel('/content/Football_Championship_2023_Shots_With_Expected_Points_JSON.xlsx')

# Filtering relevant columns and focusing on blocked shots
blocked_shots = df[df['Action'] == 'blocked']

# Get unique opposition teams (teams that executed the block)
teams = blocked_shots['TeamName'].unique()

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

# Create a plot for each team
for team in teams:
    # Filter data for blocks executed by the current team
    team_data = blocked_shots[blocked_shots['TeamName'] == team]

    # Setup plot
    fig, ax = plt.subplots(figsize=(7.25, 8.8))
    ax.set_xlim(72.5, 145)  # Show only the right side of the pitch
    ax.set_ylim(0, 88)
    ax.set_title(f'Blocked Shots by {team}')
    plt.gca().invert_yaxis()  # Invert Y axis

    # Draw the pitch with updated colors
    draw_gaa_pitch(ax, line="white", pitch="#61bf56")  # Dark green grass color

    # Plotting block points
    ax.scatter(team_data['stand_x'], team_data['stand_y'], label='Block Point', s=50, color='blue', edgecolors='black', zorder=5)

    ax.set_xticks([])
    ax.set_yticks([])
    # ax.legend(title='Block Points', loc='upper right')

    # Save the figure before showing it
    plt.savefig(f'/content/{team}_block_points.png')  # Save each chart
    plt.show()  # Display the plot
    plt.close(fig)  # Close the current figure to free up memory

