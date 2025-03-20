
import matplotlib.pyplot as plt

def create_health_bar(current_health, max_health, bar_width=0.8, bar_color='green', bg_color='red', border_color='black'):
    """
    Creates and displays a health bar using Matplotlib.

    Args:
        current_health (int): The current health value.
        max_health (int): The maximum health value.
        bar_width (float, optional): The width of the health bar. Defaults to 0.8.
        bar_color (str, optional): The color of the health bar. Defaults to 'green'.
        bg_color (str, optional): The background color of the health bar. Defaults to 'red'.
        border_color (str, optional): The border color of the health bar. Defaults to 'black'.
    """
    health_percentage = current_health / max_health
    
    fig, ax = plt.subplots(figsize=(5, 1))
    
    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Draw background bar
    ax.barh(0.5, 1, bar_width, color=bg_color, edgecolor=border_color)
    
    # Draw health bar
    ax.barh(0.5, health_percentage, bar_width, color=bar_color)
    
    plt.show()

if __name__ == '__main__':
    create_health_bar(75, 100)  # Example: 75 health out of 100
    create_health_bar(30, 100)  # Example: 30 health out of 100