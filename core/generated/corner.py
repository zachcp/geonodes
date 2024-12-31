from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Corner(Socket):

    @classmethod
    def accumulate_field(cls, value=None, group_id=None):
        """ > Class Method <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'MATRIX': 'TRANSFORM'}, 'Corner.accumulate_field', 'value')
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain='CORNER')
        return node._out

    def attribute_statistic(self, attribute=None):
        """ > Method <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Corner.attribute_statistic', 'attribute')
        node = Node('Attribute Statistic', sockets={'Geometry': self, 'Selection': self._sel, 'Attribute': attribute}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    @property
    def edges(cls, corner_index=None):
        """ > Property Get <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - node [next_edge_index (Integer), previous_edge_index (Integer)]
        """
        node = Node('Edges of Corner', sockets={'Corner Index': corner_index})
        return node

    @classmethod
    @property
    def next_edge_index(cls, corner_index=None):
        """ > Property Get <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - next_edge_index
        """
        node = Node('Edges of Corner', sockets={'Corner Index': corner_index})
        return node.next_edge_index

    @classmethod
    @property
    def previous_edge_index(cls, corner_index=None):
        """ > Property Get <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - previous_edge_index
        """
        node = Node('Edges of Corner', sockets={'Corner Index': corner_index})
        return node.previous_edge_index

    @classmethod
    @property
    def face(cls, corner_index=None):
        """ > Property Get <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - node [face_index (Integer), index_in_face (Integer)]
        """
        node = Node('Face of Corner', sockets={'Corner Index': corner_index})
        return node

    @classmethod
    @property
    def face_index(cls, corner_index=None):
        """ > Property Get <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - face_index
        """
        node = Node('Face of Corner', sockets={'Corner Index': corner_index})
        return node.face_index

    @classmethod
    @property
    def index_in_face(cls, corner_index=None):
        """ > Property Get <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - index_in_face
        """
        node = Node('Face of Corner', sockets={'Corner Index': corner_index})
        return node.index_in_face

    @classmethod
    def evaluate_at_index(cls, index=None, value=None):
        """ > Class Method <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.evaluate_at_index', 'value')
        node = Node('Evaluate at Index', sockets={'Index': index, 'Value': value}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None):
        """ > Class Method <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.evaluate_on_domain', 'value')
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def offset_in_face(cls, corner_index=None, offset=None):
        """ > Class Method <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Integer
        """
        node = Node('Offset Corner in Face', sockets={'Corner Index': corner_index, 'Offset': offset})
        return node._out

    def sample_index(self, value=None, index=None, clamp=False):
        """ > Method <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.sample_index', 'value')
        node = Node('Sample Index', sockets={'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='CORNER')
        return node._out

    def sample_nearest(self, sample_position=None):
        """ > Method <&Node Sample Nearest>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Nearest', sockets={'Geometry': self, 'Sample Position': sample_position}, domain='CORNER')
        return node._out

    def store_named_attribute(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.store_named_attribute', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.store', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store_uv(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : 'FLOAT2'
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Vector) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type='FLOAT2', domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def pack_uv_islands(cls, uv=None, margin=None, rotate=None):
        """ > Class Method <&Node Pack UV Islands>

        Information
        -----------
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (id: UV)
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', sockets={'UV': uv, 'Selection': self._sel, 'Margin': margin, 'Rotate': rotate})
        return node._out

    @classmethod
    def uv_unwrap(cls, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """ > Class Method <&Node UV Unwrap>

        Information
        -----------
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (str): parameter 'method' in ('ANGLE_BASED', 'CONFORMAL')

        Returns
        -------
        - Vector
        """
        node = Node('UV Unwrap', sockets={'Selection': self._sel, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes}, method=method)
        return node._out

    @classmethod
    def vertex(cls, corner_index=None):
        """ > Class Method <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer
        """
        node = Node('Vertex of Corner', sockets={'Corner Index': corner_index})
        return node._out

    def viewer(self, value=None):
        """ > Method <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Corner.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='CORNER')
        return

