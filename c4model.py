from pydot import Node, Dot, Edge, Cluster

GRAY = '#959595'
BLUE = '#4682B4'
DARK_BLUE = '#104376'
DARK_GRAY = '#6c6c6c'
DARKER_GRAY = '#4c4c4c'

FONT_NAME = 'Verdana'


def _create_name(name, node_type, description):
    return f'"{name}\n[{node_type}]\n\n{description}"'


_default_node_kwargs = {
    'shape': "rectangle",
    'style': 'filled',
    'fontcolor': 'white',
    'color': DARK_GRAY,
    'fontsize': 10,
    'fontname': FONT_NAME,
}


class Model(Dot):
    def __init__(self, graph_type='digraph', name='c1', fontname=FONT_NAME, **kwargs):
        super().__init__(
            graph_type=graph_type,
            fontname=fontname,
            **kwargs,
        )
        self.name = name

    def add_relationship(self, relationship):
        self.add_edge(relationship)
        return self

    def add_box(self, box):
        self.add_node(box)
        return self

    def add_submodel(self, submodel):
        self.add_subgraph(submodel)
        return self

    def save(self):
        self.write_png(f'{self.name}.png')
        return self


class Submodel(Cluster):
    def __init__(self, name='', **kwargs):
        super().__init__(
            style='dashed',
            color=DARK_GRAY,
            graph_name=name,
            **kwargs,
        )

    def add_relationship(self, relationship):
        self.add_edge(relationship)
        return self

    def add_box(self, box):
        self.add_node(box)
        return self


class Relationship(Edge):
    def __init__(self,
                 from_node,
                 to_node,
                 description='',
                 directional=True,
                 **kwargs):
        dir = 'forward' if directional else 'none'
        super().__init__(from_node,
                         to_node,
                         dir=dir,
                         label=description,
                         color=DARK_GRAY,
                         fontcolor=DARKER_GRAY,
                         fontsize=9,
                         fontname=FONT_NAME,
                         **kwargs)


class Box(Node):
    def __init__(self, **kwargs):
        super().__init__(**{**_default_node_kwargs, **kwargs}, )


class Person(Box):
    def __init__(self, name='', description='', color=DARK_BLUE, **kwargs):
        super().__init__(
            name=_create_name(name, 'Person', description),
            fillcolor=color,
            **kwargs,
        )


def _get_software_box_color(kwargs, is_external):
    return kwargs.get('color', GRAY if is_external else BLUE)


class SoftwareSystem(Box):
    def __init__(self, name='', description='', is_external=False, **kwargs):
        super().__init__(name=_create_name(name, 'Software System',
                                           description),
                         fillcolor=_get_software_box_color(
                             kwargs, is_external),
                         **kwargs)


class Container(Box):
    def __init__(self,
                 name='',
                 container_description='',
                 description='',
                 is_external=False,
                 **kwargs):
        super().__init__(
            name=_create_name(name, f'Container: {container_description}',
                              description),
            fillcolor=_get_software_box_color(kwargs, is_external),
            **kwargs)
