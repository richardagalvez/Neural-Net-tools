import matplotlib.pyplot as plt

def netdraw(ax, layer_sizes, left=0.1, right=0.9, bottom=0.1, top=0.9):
    '''
    Draw a neural network cartoon using matplotilb incorporating weights as opacities.

    :usage:
        >>> connections = []

        >>> nodes  = [2, 5, 15, 3, 5, 6, 1]
        >>> node_alphas = [np.random.rand(node) for node in nodes]

        >>> for n in range(len(nodes)-1):
                connections.append(np.random.rand(nodes[n]*nodes[n+1]))

        >>> netdraw(nodes, node_alphas, connections, 1.5)

    :parameters:
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
    '''
    fig = plt.figure(figsize=(10*scale, 10*scale))
    ax = fig.gca()
    ax.axis('off')
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)

    # Nodes

    for n, layer_size in enumerate(layer_sizes):

        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        if n == 0:
            ax.annotate('Input' , xy=(n*h_spacing + left - v_spacing/2., 1), fontsize=20)
        elif n == len(layer_sizes)-1:
            ax.annotate('Output', xy=(n*h_spacing + left - v_spacing/2., 1), fontsize=20)

        else:
            ax.annotate('%s' % n, xy=(n*h_spacing + left - v_spacing/4. , 1), fontsize=20)

        for m in range(layer_size):
            circle = plt.Circle((n*h_spacing + left, layer_top - m*v_spacing), v_spacing/3.,
                                color='r', ec='r', zorder=4, alpha = alpha_node[n][m])
            ax.add_artist(circle)

    # Edges

    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.

        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k', alpha = connections[n][(m+1)*(o+1)-1])
                ax.add_artist(line)
