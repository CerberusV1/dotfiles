from libqtile.lazy import lazy


wp_colors = []

cache='/home/cerberus/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            wp_colors.append(file.readline().strip())
    wp_colors.append('#ffffff')
    lazy.reload()
load_colors(cache)
